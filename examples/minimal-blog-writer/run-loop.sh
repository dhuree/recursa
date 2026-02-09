#!/bin/bash
set -e

# Self-improving loop runner for Recursa-based systems
# Runs Claude Code in a Docker sandbox to iterate on any domain
# Usage: ./run-loop.sh [N]  (default N=5)

N=${1:-5}
DIR="$(cd "$(dirname "$0")" && pwd)"
LOG_DIR="$DIR/logs"
IMAGE_NAME="recursa-sandbox"
CONTAINER_NAME="recursa-loop"

mkdir -p "$LOG_DIR"

# The iteration prompt - customize for your domain
PROMPT="Run one iteration of the self-improving loop.

1. First, read system/SOUL.md to understand your identity
2. Read docs/LOOP.md to understand the iteration process
3. Read docs/LEARNING.md for accumulated knowledge
4. Check docs/METRICS.md for current performance trends

Then execute one complete iteration:
- Prepare: Choose what to work on based on priorities
- Execute: Do the work (write content, code, etc.)
- Evaluate: Rate your output honestly using the quality scale
- Capture: Update LEARNING.md with discoveries
- Improve: Note what to do differently next time

Log your reflection in journal/reflections/ with today's date.
Update docs/METRICS.md with this iteration's results.

Focus on LEARNING over perfection. Every iteration should teach something new."

cd "$DIR"

# Clean up old logs (keep last 50)
ls -t "$LOG_DIR"/*.log 2>/dev/null | tail -n +51 | xargs -r rm -f
ls -t "$LOG_DIR"/*.json 2>/dev/null | tail -n +51 | xargs -r rm -f

# Build the sandbox image if it doesn't exist
if ! docker image inspect "$IMAGE_NAME" &>/dev/null; then
    echo "Building sandbox image..."
    docker build -t "$IMAGE_NAME" -f Dockerfile.sandbox .
fi

echo "Starting $N iteration(s) of the self-improving loop..."
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
    DOCKER_ARGS+=(-v "$DIR:/workspace")
    DOCKER_ARGS+=(-v "$HOME/.claude:/home/node/.claude:ro")
    DOCKER_ARGS+=(-v "$HOME/.config/claude:/home/node/.config/claude:ro")
    DOCKER_ARGS+=(-w /workspace)

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
echo "Check docs/METRICS.md for performance trends."
