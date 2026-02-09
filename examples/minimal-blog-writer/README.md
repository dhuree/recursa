# Minimal Blog Writer Example

This is a minimal example of a bootstrapped Recursa system for technical blog writing.

## What's Included

This minimal setup includes only the essential files:

```
minimal-blog-writer/
├── system/
│   ├── SOUL.md          # Who the system is
│   ├── CONSTITUTION.md  # Inviolable rules
│   └── IDENTITY.md      # Name and personality
├── docs/
│   ├── LOOP.md          # Writing iteration process
│   ├── LEARNING.md      # Accumulated knowledge
│   └── METRICS.md       # Quality tracking
├── memory/
│   └── scratchpad.md    # Working notes
├── journal/
│   └── reflections/     # Post-iteration reflections
├── skills/              # Writing techniques
└── guardrails/          # Safety policies
```

## The Domain

- **What**: Technical blog writing about software engineering
- **Iteration**: One blog post = one iteration
- **Duration**: 4-6 hours per post
- **Success**: Clear explanations + working code examples

## How to Use

1. Read `system/SOUL.md` to understand the system's identity
2. Follow `docs/LOOP.md` for each writing iteration
3. Track quality with `docs/METRICS.md`
4. Capture learnings in `docs/LEARNING.md`

## Running Automated Loops

This example includes Docker infrastructure for running automated iteration loops:

```bash
# Make executable
chmod +x run-loop.sh

# Run 5 iterations
./run-loop.sh

# Run 10 iterations
./run-loop.sh 10
```

See `DOCKER.md` for full documentation on:
- Customizing the iteration prompt
- Monitoring logs
- Production considerations

## Customizing This Example

This is a starting point. Adjust based on your needs:

- Edit `SOUL.md` to match your voice and values
- Modify `LOOP.md` to fit your writing process
- Update `METRICS.md` with your quality criteria
- Add categories to `LEARNING.md` for your topics
