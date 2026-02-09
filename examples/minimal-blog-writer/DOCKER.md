# Running in Docker

This guide explains how to run the self-improving system in a Docker container for automated iteration loops.

## Why Docker?

Running in Docker provides:
- **Isolation**: Each iteration runs in a clean environment
- **Reproducibility**: Same environment every time
- **Safety**: Sandboxed execution limits potential damage
- **Automation**: Run unattended iteration loops

## Prerequisites

1. Docker installed and running
2. Claude Code CLI credentials configured (`~/.claude` and `~/.config/claude`)
3. This project directory

## Quick Start

```bash
# Make the script executable
chmod +x run-loop.sh

# Run 5 iterations (default)
./run-loop.sh

# Run a specific number of iterations
./run-loop.sh 10
```

## Files

### Dockerfile.sandbox

Minimal Docker image with:
- Node.js 22 (slim)
- Claude Code CLI
- Git, curl, jq for basic operations

Customize this if your domain needs additional tools:
```dockerfile
# Example: Add Python for a coding-focused system
RUN apt-get update && apt-get install -y python3 python3-pip
```

### run-loop.sh

The iteration runner script. Key components:

```bash
# Number of iterations (default 5)
N=${1:-5}

# The prompt sent to Claude each iteration
PROMPT="Run one iteration of the self-improving loop..."
```

**Customize the PROMPT** for your specific domain:

```bash
# Example for a blog writing system
PROMPT="Write one blog post following docs/LOOP.md.
Topic: Choose from the backlog or explore something new.
After writing, rate it using docs/METRICS.md criteria.
Update docs/LEARNING.md with what you learned."

# Example for a code review system
PROMPT="Review one pull request following docs/LOOP.md.
Select from the queue in tasks/queued/.
Document findings and update LEARNING.md."
```

## Directory Structure After Running

```
minimal-blog-writer/
├── logs/                    # Created automatically
│   ├── loop-20240115-143022.log   # Human-readable log
│   └── loop-20240115-143022.json  # Raw JSON output
├── journal/
│   └── reflections/
│       └── 2024-01-15.md    # Created by Claude
└── docs/
    ├── LEARNING.md          # Updated with discoveries
    └── METRICS.md           # Updated with results
```

## Monitoring

### Watch logs in real-time

```bash
# Follow the latest log file
tail -f logs/loop-*.log | head -1 | xargs tail -f

# Or watch for new files
watch -n 5 'ls -lt logs/*.log | head -5'
```

### Check iteration results

```bash
# View latest reflection
cat journal/reflections/$(ls -t journal/reflections/ | head -1)

# Check metrics trend
cat docs/METRICS.md
```

## Customization

### Adjust iteration timing

Edit `run-loop.sh` to change the delay between iterations:

```bash
# Current: 5 seconds between iterations
[ $i -lt $N ] && sleep 5

# For longer iterations, increase delay
[ $i -lt $N ] && sleep 60
```

### Add volume mounts

If your system needs access to external resources:

```bash
# In run-loop.sh, add to DOCKER_ARGS:
DOCKER_ARGS+=(-v "/path/to/data:/data:ro")
DOCKER_ARGS+=(-v "/path/to/output:/output")
```

### Environment variables

Pass environment variables to the container:

```bash
DOCKER_ARGS+=(-e "OPENAI_API_KEY=$OPENAI_API_KEY")
DOCKER_ARGS+=(-e "DEBUG=true")
```

## Troubleshooting

### Container fails to start

```bash
# Check if image exists
docker images | grep recursa-sandbox

# Rebuild the image
docker build -t recursa-sandbox -f Dockerfile.sandbox .
```

### Permission errors

```bash
# Ensure credentials are readable
ls -la ~/.claude ~/.config/claude

# Fix ownership if needed
sudo chown -R $(id -u):$(id -g) ~/.claude ~/.config/claude
```

### Out of disk space

```bash
# Clean up old logs
rm -f logs/*.log logs/*.json

# Remove old Docker images
docker system prune -f
```

## Production Considerations

For long-running automated loops:

1. **Log rotation**: The script keeps the last 50 logs. Adjust as needed.
2. **Monitoring**: Set up alerts for container failures
3. **Resource limits**: Add Docker resource constraints:
   ```bash
   DOCKER_ARGS+=(--memory="4g" --cpus="2")
   ```
4. **Backup**: Regularly backup the docs/ and memory/ directories

## Security Notes

- Credentials are mounted read-only (`:ro`)
- The container runs as non-root user (node)
- Network access is enabled (required for Claude API)
- Consider using Docker secrets for sensitive data in production
