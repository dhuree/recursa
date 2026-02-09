#!/bin/bash
set -e

# Self-improving loop runner for Recursa-based systems
# Runs Claude Code in a Docker sandbox to iterate on any domain
#
# Features:
#   - Loads core Recursa documents (SOUL, CONSTITUTION, LOOP, LEARNING)
#   - Tracks total iteration count across runs
#   - Triggers meso retrospectives every 5 iterations
#   - Triggers macro reviews every 20 iterations
#   - Archives logs instead of deleting them
#
# Usage: ./run-loop.sh [N]  (default N=5)

N=${1:-5}
DIR="$(cd "$(dirname "$0")" && pwd)"
LOG_DIR="$DIR/logs"
IMAGE_NAME="recursa-sandbox"
CONTAINER_NAME="recursa-loop"
ITERATION_FILE="$DIR/.iteration_count"

mkdir -p "$LOG_DIR"

# Track iteration count across runs for meso/macro cycles
if [ -f "$ITERATION_FILE" ]; then
    TOTAL_ITERATIONS=$(cat "$ITERATION_FILE")
else
    TOTAL_ITERATIONS=0
fi

# Recursa-aligned prompt for self-improving loop
read -r -d '' PROMPT << 'EOF' || true
You are a self-improving system following the Recursa framework.

## Startup (Every Iteration)
1. Read system/SOUL.md for identity and values
2. Read system/CONSTITUTION.md for constraints (NEVER violate)
3. Read docs/LOOP.md for the iteration process
4. Check memory/scratchpad.md for context from previous iteration
5. Consult docs/LEARNING.md for accumulated knowledge

## This Iteration
Run one complete iteration cycle: PREPARE → EXECUTE → EVALUATE → CAPTURE → IMPROVE

**Emphasis**: LEARNING over perfection. Every iteration should teach something new.
- Choose what to work on based on priorities and recent learnings
- Execute the work (write content, create output, etc.)
- Rate your output honestly using docs/METRICS.md criteria
- Log discoveries to docs/LEARNING.md with proper level markers
- Note what to do differently next time

## Documentation Requirements
- Update docs/LEARNING.md with discoveries
- Rate outputs honestly in journal/reflections/
- Update docs/METRICS.md with iteration stats
- Use memory/scratchpad.md for working notes and context for next iteration

## Review Cycles
- Every 5th iteration: Meso retrospective (review last 5 iterations)
- Every 20th iteration: Macro review (comprehensive strategy review)

## End of Iteration
Before finishing:
1. Update scratchpad.md with context for next iteration
2. Verify all documentation updated
3. Commit any changes if appropriate
EOF

cd "$DIR"

# Archive old logs instead of deleting
ARCHIVE_DIR="$LOG_DIR/archive"
mkdir -p "$ARCHIVE_DIR"
if ls "$LOG_DIR"/*.log "$LOG_DIR"/*.json 1>/dev/null 2>&1; then
    ARCHIVE_DATE=$(date +%Y%m%d-%H%M%S)
    ARCHIVE_FILE="$ARCHIVE_DIR/logs-$ARCHIVE_DATE.tar.gz"
    tar -czf "$ARCHIVE_FILE" -C "$LOG_DIR" --exclude='archive' *.log *.json 2>/dev/null || true
    rm -f "$LOG_DIR"/*.log "$LOG_DIR"/*.json
    echo "Archived previous logs to $ARCHIVE_FILE"
fi

# Clean up archives older than 30 days
find "$ARCHIVE_DIR" -name "*.tar.gz" -mtime +30 -delete 2>/dev/null || true

# Build the sandbox image if it doesn't exist
if ! docker image inspect "$IMAGE_NAME" &>/dev/null; then
    echo "Building sandbox image..."
    docker build -t "$IMAGE_NAME" -f Dockerfile.sandbox .
fi

echo "Starting $N iteration(s) of the self-improving loop..."
echo "Total iterations to date: $TOTAL_ITERATIONS"
echo "Logs will be written to: $LOG_DIR"
echo ""

for ((i=1; i<=N; i++)); do
    # Increment total iteration count
    TOTAL_ITERATIONS=$((TOTAL_ITERATIONS + 1))
    echo "$TOTAL_ITERATIONS" > "$ITERATION_FILE"

    # Determine cycle type
    CYCLE_TYPE="micro"
    CYCLE_PROMPT=""
    if ((TOTAL_ITERATIONS % 20 == 0)); then
        CYCLE_TYPE="macro"
        CYCLE_PROMPT="

## MACRO REVIEW CYCLE (Iteration #$TOTAL_ITERATIONS)
This is a MACRO review iteration. Before regular work:
1. Perform comprehensive 20-iteration review
2. Analyze trends in docs/METRICS.md
3. Consolidate knowledge in docs/LEARNING.md
4. Assess and update strategy
5. Write major review in journal/reflections/
6. Then proceed with normal iteration"
    elif ((TOTAL_ITERATIONS % 5 == 0)); then
        CYCLE_TYPE="meso"
        CYCLE_PROMPT="

## MESO RETROSPECTIVE (Iteration #$TOTAL_ITERATIONS)
This is a MESO retrospective iteration. Before regular work:
1. Review last 5 iterations in journal/reflections/
2. Update docs/METRICS.md dashboard
3. Promote observations to patterns in LEARNING.md if warranted
4. Then proceed with normal iteration"
    fi

    # Build iteration-specific prompt
    ITER_PROMPT="$PROMPT

## Current State
- Session iteration: $i of $N
- Total iterations: #$TOTAL_ITERATIONS
- Cycle type: $CYCLE_TYPE$CYCLE_PROMPT"

    TIMESTAMP=$(date +%Y%m%d-%H%M%S)
    LOG="$LOG_DIR/loop-$TIMESTAMP.log"
    LOG_JSON="$LOG_DIR/loop-$TIMESTAMP.json"
    touch "$LOG_JSON"

    echo "=== Iteration $i of $N (Total: #$TOTAL_ITERATIONS, Cycle: $CYCLE_TYPE) ===" | tee -a "$LOG"
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

    CLAUDE_ARGS=(-p "$ITER_PROMPT" --dangerously-skip-permissions --verbose --output-format stream-json)

    # Run container in detached mode
    CONTAINER_ID=$(docker run "${DOCKER_ARGS[@]}" "$IMAGE_NAME" "${CLAUDE_ARGS[@]}" 2>&1)

    if [ -z "$CONTAINER_ID" ] || ! docker ps -q --filter "id=$CONTAINER_ID" | grep -q .; then
        echo "ERROR: Container failed to start: $CONTAINER_ID" >> "$LOG"
        kill $PARSER_PID 2>/dev/null || true
        sleep 10
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
echo "Total iterations to date: $TOTAL_ITERATIONS"
echo "Next meso retrospective: iteration #$(( (TOTAL_ITERATIONS / 5 + 1) * 5 ))"
echo "Next macro review: iteration #$(( (TOTAL_ITERATIONS / 20 + 1) * 20 ))"
echo "Review logs in: $LOG_DIR"
echo "Check docs/METRICS.md for performance trends."
