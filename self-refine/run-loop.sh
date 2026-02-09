#!/bin/bash
set -e

# Self-improving loop runner for Recursa framework development
# Runs Claude Code in a Docker sandbox to iterate on the framework itself
# Usage: ./run-loop.sh [N]  (default N=5)

N=${1:-5}
DIR="$(cd "$(dirname "$0")" && pwd)"
RECURSA_DIR="$(dirname "$DIR")"
LOG_DIR="$DIR/logs"
IMAGE_NAME="recursa-self-refine"
CONTAINER_NAME="recursa-self-refine-loop"
PLAYGROUND_DIR="$(dirname "$RECURSA_DIR")/recursa-playground"

mkdir -p "$LOG_DIR"
mkdir -p "$PLAYGROUND_DIR"

# The iteration prompt for self-refinement of the Recursa framework
PROMPT="Run one self-refinement iteration on the Recursa framework through experimentation.

Recursa improves itself by creating and learning from real projects. The playground at $PLAYGROUND_DIR is your experimental space.

## Your Iteration Cycle

1. **Survey**: Check the playground for existing projects. Review any previous iteration logs in self-refine/logs/ for context.

2. **Decide**: Choose one of these actions:
   - Create a new project: Bootstrap a fresh Recursa-based system for a domain you want to explore
   - Evolve an existing project: Run an iteration on a playground project, improve it, observe what works
   - Harvest learnings: Analyze completed projects for patterns that should improve Recursa itself

3. **Execute**: Carry out your chosen action:
   - For new projects: Use the bootstrapping workflow to create in the playground
   - For running projects: Execute their iteration loop, monitor behavior, note friction points
   - For harvesting: Extract concrete improvements from project experiences

4. **Learn**: Based on what you observed:
   - What worked well? What was awkward or missing?
   - Did templates provide what was needed? Were instructions clear?
   - What would have made this project more successful?

5. **Refine**: Apply learnings to improve Recursa:
   - Update templates based on real usage friction
   - Clarify documentation where confusion arose
   - Add patterns that proved valuable in practice

## Freedom & Judgment

You have full autonomy to:
- Choose which domains to explore (practical, creative, technical, experimental)
- Decide project scope and complexity
- Determine when a project has taught enough to harvest
- Balance creation vs refinement based on what Recursa needs most

## Constraints

- Work within the playground for experiments
- Keep Recursa changes grounded in actual project experience
- One focused action per iteration (create OR run OR harvest, not all three)"

cd "$RECURSA_DIR"

# Clean up old logs (keep last 50)
ls -t "$LOG_DIR"/*.log 2>/dev/null | tail -n +51 | xargs -r rm -f
ls -t "$LOG_DIR"/*.json 2>/dev/null | tail -n +51 | xargs -r rm -f

# Build the sandbox image if it doesn't exist
if ! docker image inspect "$IMAGE_NAME" &>/dev/null; then
    echo "Building sandbox image..."
    docker build -t "$IMAGE_NAME" -f "$DIR/Dockerfile.sandbox" "$DIR"
fi

echo "Starting $N self-refinement iteration(s) on Recursa..."
echo "Logs will be written to: $LOG_DIR"
echo ""

for ((i=1; i<=N; i++)); do
    TIMESTAMP=$(date +%Y%m%d-%H%M%S)
    LOG="$LOG_DIR/loop-$TIMESTAMP.log"
    LOG_JSON="$LOG_DIR/loop-$TIMESTAMP.json"
    touch "$LOG_JSON"

    echo "=== Iteration $i of $N ===" | tee -a "$LOG"
    echo "Started at $(date)" >> "$LOG"

    # Start background parser that tails the raw JSON and writes readable output
    (
        tail -f "$LOG_JSON" 2>/dev/null | while IFS= read -r line; do
            # Extract assistant text messages
            text=$(echo "$line" | jq -r 'select(.type=="assistant") | .message.content[]? | select(.type=="text") | .text // empty' 2>/dev/null)
            [ -n "$text" ] && echo "$text" >> "$LOG"
            # Extract tool calls (truncated for readability)
            tool=$(echo "$line" | jq -r 'select(.type=="assistant") | .message.content[]? | select(.type=="tool_use") | "[\(.name)] \(.input | tostring | .[0:200])"' 2>/dev/null)
            [ -n "$tool" ] && echo "$tool" >> "$LOG"
        done
    ) &
    PARSER_PID=$!

    # Force remove any previous container before starting new one
    docker rm -f "$CONTAINER_NAME" 2>/dev/null || true

    # Build docker args as an array
    DOCKER_ARGS=(-d --name "$CONTAINER_NAME" --network host)
    # Mount parent workspace so container can access sibling projects
    # Use same path inside container as on host for consistency
    WORKSPACE_ROOT="$(dirname "$RECURSA_DIR")"
    DOCKER_ARGS+=(-v "$WORKSPACE_ROOT:$WORKSPACE_ROOT")
    DOCKER_ARGS+=(-v "$HOME/.claude:/home/node/.claude")
    DOCKER_ARGS+=(-v "$HOME/.config/claude:/home/node/.config/claude")
    DOCKER_ARGS+=(-w "$RECURSA_DIR")

    CLAUDE_ARGS=(-p "$PROMPT" --dangerously-skip-permissions --verbose --output-format stream-json)

    # Run container in detached mode
    CONTAINER_ID=$(docker run "${DOCKER_ARGS[@]}" "$IMAGE_NAME" "${CLAUDE_ARGS[@]}" 2>&1)

    if [ -z "$CONTAINER_ID" ] || ! docker ps -q --filter "id=$CONTAINER_ID" | grep -q .; then
        echo "ERROR: Container failed to start: $CONTAINER_ID" >> "$LOG"
        kill $PARSER_PID 2>/dev/null || true
        sleep 5
        continue
    fi

    echo "Container started: ${CONTAINER_ID:0:12}" >> "$LOG"

    # Stream container output to log file in background
    docker logs -f "$CONTAINER_NAME" >> "$LOG_JSON" 2>&1 &
    LOGS_PID=$!

    # Wait for container to finish
    EXIT_CODE=$(docker wait "$CONTAINER_ID" 2>&1)
    echo "Container exited with code: $EXIT_CODE" >> "$LOG"

    # Stop the log streaming and parser
    kill $LOGS_PID 2>/dev/null || true
    kill $PARSER_PID 2>/dev/null || true

    # Clean up container
    docker rm -f "$CONTAINER_NAME" 2>/dev/null || true

    echo "Completed at $(date)" >> "$LOG"
    echo "Iteration $i complete. Log: $LOG"
    echo ""

    # Brief pause between iterations
    [ $i -lt $N ] && sleep 5
done

echo "All $N iterations complete."
echo "Review logs in: $LOG_DIR"
