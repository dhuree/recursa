# Bootstrapping Guide

How to use Recursa to create a new self-improving system for any domain.

---

## Overview

Recursa is a **meta-framework**. You don't use Recursa directly—you use it to **bootstrap** new self-improving projects. This guide explains how.

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                         BOOTSTRAPPING FLOW                                  │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│   ┌──────────────┐     ┌──────────────┐     ┌──────────────┐               │
│   │   RECURSA    │     │  INTERVIEW   │     │ YOUR PROJECT │               │
│   │  (templates) │ ──→ │  (discover)  │ ──→ │ (customized) │               │
│   └──────────────┘     └──────────────┘     └──────────────┘               │
│                                                                             │
│   You have this        Claude asks          You get a fully                │
│   framework            about your           configured self-               │
│                        domain               improving system               │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## Prerequisites

Before bootstrapping:

1. **Have a target folder** - Where your new project will live
2. **Know your domain** - What kind of work you're improving
3. **Have an AI assistant** - Claude Code, Cursor, Windsurf, Cline, or similar

---

## Quick Start (5 Minutes)

For the fastest possible setup, use the **minimal bootstrap**:

```
Create a minimal Recursa system at ~/my-project
```

This creates only the essential files:
- `system/SOUL.md` - Core identity
- `docs/LOOP.md` - Iteration process
- `docs/LEARNING.md` - Knowledge capture
- `docs/METRICS.md` - Quality tracking

**You'll answer just 6 questions:**
1. What is this system for?
2. What is one cycle of work?
3. How long does an iteration take?
4. What makes output excellent?
5. What qualities can never be compromised?
6. What actions need your approval?

That's it. You can add more components later as needed.

---

## Standard Quick Start

### Step 1: Start Your AI Assistant in Recursa

```bash
cd /path/to/recursa
# Start your AI assistant (Claude Code, Cursor, Windsurf, Cline, etc.)
```

### Step 2: Request Bootstrap

Tell Claude:

```
Bootstrap a new self-improving project at /path/to/my-project
```

Or more specifically:

```
Create a Recursa-based self-improving system for blog writing at ~/blog-system
```

### Step 3: Answer Questions

Claude will ask about:
- What your system is for
- What one iteration of work looks like
- How you measure success
- What can be learned
- What safety constraints exist

### Step 4: Review Generated Files

Claude will create customized documents in your target folder. Review them and adjust as needed.

### Step 5: Start Iterating

Use your new system! Follow the LOOP.md in your project.

---

## Detailed Walkthrough

### Phase 1: Preparation

**Before you start, know:**

| Question | Example Answer |
|----------|----------------|
| What is this system for? | "Improving my technical blog writing" |
| What is one iteration? | "Writing and publishing one blog post" |
| How do you measure success? | "Reader engagement, clarity of explanation" |
| What should never happen? | "Publishing with factual errors" |

Having rough answers speeds up the interview.

**Prepare target directory:**

```bash
# Create your project folder
mkdir -p ~/my-project

# Initialize git (recommended)
cd ~/my-project && git init
```

### Phase 2: The Interview

Claude will ask questions to customize the system. Be specific!

**Good answers:**
- "A 5/5 blog post explains a complex topic so a beginner can understand it, includes working code examples, and has been reviewed for accuracy"
- "One iteration is writing, editing, and publishing one post, typically 4-6 hours"

**Vague answers (avoid):**
- "Good quality"
- "It depends"

### Phase 3: Document Generation

Claude creates these files in your project:

```
your-project/
├── system/                     # Identity & governance
│   ├── SOUL.md                 # Who the system is
│   ├── CONSTITUTION.md         # Inviolable rules
│   └── IDENTITY.md             # Name, personality
│
├── docs/                       # Operational guides
│   ├── LOOP.md                 # Iteration process
│   ├── MEMORY.md               # How memory works
│   ├── LEARNING.md             # Accumulated knowledge
│   ├── METRICS.md              # Tracking & evaluation
│   └── EVOLUTION.md            # Self-improvement
│
├── guardrails/                 # Safety infrastructure
│   ├── GUARDRAILS.md           # Safety policies
│   ├── policies/               # Specific rules
│   └── audit/                  # Action logs
│
├── memory/                     # Knowledge storage
│   ├── long_term/
│   └── scratchpad.md
│
├── journal/                    # Reflections & evolution
│   ├── reflections/
│   └── metrics/
│
├── skills/                     # Capabilities
├── tasks/                      # Work management
├── deliverables/               # Outputs
└── config/                     # Configuration
```

### Phase 4: Customization

After generation, review and adjust:

1. **SOUL.md** - Does the personality feel right?
2. **LOOP.md** - Does the workflow match how you work?
3. **METRICS.md** - Are the metrics meaningful?
4. **CONSTITUTION.md** - Are safety rules appropriate?

### Phase 5: First Iteration

Start using the system:

1. Read `docs/LOOP.md` for your iteration process
2. Do one iteration of work
3. Evaluate your output using `docs/METRICS.md`
4. Capture learnings in `docs/LEARNING.md`
5. Reflect in `journal/reflections/`

---

## Example Bootstrapping Sessions

### Example 1: Technical Blog Writing

```
User: Bootstrap a self-improving blog system at ~/tech-blog

Claude: I'll help you create a self-improving technical blog writing system.
        Let me ask a few questions to customize it.

[Questions about blog topics, writing process, quality standards]

User: - I write about software engineering topics
      - One iteration = one blog post
      - Takes about 4-6 hours per post
      - Success = clear explanation + working code examples
      - Never publish with errors or untested code

Claude: Creating your tech blog system...

[Creates files]

Claude: Done! Your system includes:
        - SOUL.md focused on technical clarity
        - LOOP.md with writing → code-testing → editing workflow
        - METRICS.md tracking explanation quality and code accuracy
        - LEARNING.md with categories for topics, techniques, anti-patterns

        Start with: Read docs/LOOP.md, then write your first post!
```

### Example 2: Fitness Training

```
User: Create a Recursa system for tracking my fitness progress at ~/fitness

Claude: I'll help you build a self-improving fitness tracking system.

[Questions about workout types, goals, metrics]

User: - I do strength training 4x/week
      - One iteration = one workout session
      - Success = progressive overload, good form
      - Never train through injury signals

Claude: Creating your fitness system...

[Creates files with workout-specific customization]
```

### Example 3: Software Project

```
User: Bootstrap a self-improving dev workflow for my project at ~/myapp/workflow

Claude: I'll create a self-improving development workflow system.

[Questions about codebase, quality standards, process]

User: - Building a web application
      - One iteration = one feature or bug fix
      - Success = passing tests, code review approved
      - Never push broken code to main

Claude: Creating your dev workflow system...

[Creates files with software development focus]
```

---

## Customization Options

### Minimal Bootstrap

For simple systems, request:

```
Create a minimal Recursa system at ~/project
```

This creates only:
- `system/SOUL.md`
- `docs/LOOP.md`
- `docs/LEARNING.md`
- `docs/METRICS.md`

### Full Bootstrap

For comprehensive systems:

```
Create a full Recursa system at ~/project with all components
```

This includes:
- Complete directory structure
- All templates customized
- Safety infrastructure
- Audit logging setup

### Domain-Specific Bootstrap

Request domain focus:

```
Bootstrap a Recursa system optimized for [domain] at ~/project
```

Examples:
- "optimized for creative writing"
- "optimized for software development"
- "optimized for research"
- "optimized for sales"

---

## Running Automated Loops (Optional)

For unattended iteration, you can run the system in Docker:

```bash
# In your bootstrapped project directory
./run-loop.sh 10  # Run 10 iterations
```

This requires:
- Docker installed
- `Dockerfile.sandbox` and `run-loop.sh` in your project

See `examples/minimal-blog-writer/DOCKER.md` for setup instructions.

---

## After Bootstrapping

### Week 1: Learn the System

- Read all docs in order: SOUL → LOOP → METRICS → LEARNING → EVOLUTION
- Do 3-5 iterations following the loop strictly
- Capture learnings even if they feel obvious

### Week 2-4: Build Habits

- Follow LOOP.md for every iteration
- Update LEARNING.md after each session
- Do your first retrospective after 5 iterations

### Month 2+: Let It Evolve

- Propose updates to SOUL.md based on patterns
- Track metrics trends
- Refine the process based on experience

---

## Troubleshooting

### "The generated docs don't quite fit my needs"

This is expected! The generated docs are a starting point. Edit them:
- Adjust LOOP.md to match your actual workflow
- Refine quality criteria in METRICS.md
- Add domain-specific knowledge to LEARNING.md

### "The interview was too long/short"

Tell Claude your preference:
- "Quick bootstrap with minimal questions"
- "Comprehensive interview, I want full customization"

### "I want to change the structure"

The directory structure is flexible. Adjust it:
- Rename folders to match your mental model
- Add domain-specific directories
- Remove components you won't use

### "How do I migrate an existing project?"

Options:
1. Bootstrap alongside: Create Recursa docs in your existing project folder
2. Gradual adoption: Start with just SOUL.md and LOOP.md
3. Full integration: Bootstrap then merge existing content

---

## Best Practices

### During Bootstrap

1. **Be specific** - Vague answers create generic systems
2. **Give examples** - Concrete examples help customization
3. **Think ahead** - Consider what you want to learn

### After Bootstrap

1. **Commit immediately** - Version control from day one
2. **Follow the loop** - Discipline creates improvement
3. **Capture everything** - Over-document at first, prune later
4. **Review regularly** - Monthly retrospectives minimum

### Ongoing

1. **Trust the process** - Benefits compound over iterations
2. **Evolve the system** - It should change as you learn
3. **Measure honestly** - Don't game your own metrics

---

## Getting Help

### Within Your AI Assistant

Ask:
- "How should I use [document]?"
- "Help me with my first iteration"
- "What should I capture in LEARNING.md?"

### Modifying Your System

Ask:
- "Update my LOOP.md to include [step]"
- "Add a new category to LEARNING.md"
- "Refine my quality criteria in METRICS.md"

### Meta-Improvement

Ask:
- "Review my system for improvements"
- "Analyze my LEARNING.md for patterns"
- "Suggest updates to my SOUL.md based on my reflections"
