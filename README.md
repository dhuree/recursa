# Recursa

**A blueprint for building self-improving systems in any domain.**

Recursa (from Latin *recursus* - "a running back") is a framework for creating intelligent systems that learn from their own operation, preserve knowledge across iterations, and continuously improve their capabilities.

---

## How to Use

Recursa is a **meta-framework**. You don't use it directly—you use it to **bootstrap** new self-improving projects for any domain.

It works with any agentic AI tool that can read files and have a conversation: Claude Code, Cowork, Cursor, Windsurf, Cline, Codex, or similar tools.

**Step 1: Clone and open this repository with your AI tool**

```bash
git clone https://github.com/yourusername/recursa.git
cd recursa
# Start your preferred AI assistant here
```

**Step 2: Ask your AI to bootstrap a project**

Give a prompt like:
- "Bootstrap a self-improving blogging system at ~/my-blog"
- "Create a research project at ~/research"
- "Set up a self-improving fitness coaching system at ~/fitness"
- "Bootstrap a content creation workflow at ~/youtube-channel"
- "Create a language learning system at ~/spanish-practice"
- "Set up a self-improving sales outreach system at ~/sales"

**Step 3: Answer the interview questions**

Your AI will ask about your domain, workflow, quality criteria, and goals to customize the system for your needs.

**Step 4: Navigate to your new project and start the loop**

```bash
cd ~/my-blog  # or wherever you bootstrapped
# Start your AI assistant and begin your first iteration
```

Your bootstrapped project will contain customized documentation guiding you through each iteration cycle.

### What Happens

1. **The AI reads** the templates and interview structure
2. **The AI asks** questions about your domain (purpose, workflow, metrics, etc.)
3. **The AI generates** customized versions of all documents in your target folder
4. **You review** and adjust the generated system
5. **You iterate** using your new self-improving system

### Detailed Guides

- `BOOTSTRAPPING_GUIDE.md` - Full walkthrough for users
- `AGENT.md` - Instructions for AI assistants
- `INTERVIEW.md` - Question bank for domain discovery

### Manual Setup (Without AI)

If you prefer to set up manually:

1. **Read** `ARCHITECTURE.md` to understand the patterns
2. **Follow** `BOOTSTRAP.md` step-by-step
3. **Copy** templates from `templates/` to your project
4. **Customize** each template for your domain
5. **Create** directory structure per `DIRECTORY_STRUCTURE.md`

---

## The Core Insight

Any system that iteratively produces outputs can be made self-improving through seven architectural layers:

1. **Foundation** - Core reasoning capability (human, AI, or hybrid)
2. **Identity** - Values, principles, and behavioral guidelines (SOUL.md)
3. **Memory** - Tiered knowledge: long-term, episodic, semantic
4. **Tools** - Extensible capabilities, including the ability to create new tools
5. **Reflection** - Self-evaluation, failure analysis, feedback generation
6. **Orchestration** - Coordination for complex or multi-component systems
7. **Safety** - Guardrails, audit, permissions, rollback

These layers transform a static process into a living, learning, self-improving entity.

---

## What Makes a System Self-Improving?

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                     THE SELF-IMPROVING SYSTEM                               │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│   Traditional System:                                                       │
│                                                                             │
│      Input ──→ Process ──→ Output                                           │
│                   │                                                         │
│                   × (no learning)                                           │
│                                                                             │
│   ─────────────────────────────────────────────────────────────────────     │
│                                                                             │
│   Self-Improving System:                                                    │
│                                                                             │
│      Input ──→ Process ──→ Output                                           │
│                   │            │                                            │
│                   │            ▼                                            │
│                   │      ┌──────────┐                                       │
│                   │      │ Evaluate │                                       │
│                   │      └────┬─────┘                                       │
│                   │           │                                             │
│                   │           ▼                                             │
│                   │      ┌──────────┐                                       │
│                   │      │  Learn   │                                       │
│                   │      └────┬─────┘                                       │
│                   │           │                                             │
│                   │           ▼                                             │
│                   │      ┌──────────┐                                       │
│                   ◀──────│ Improve  │                                       │
│                          └──────────┘                                       │
│                                                                             │
│   The difference: outputs inform future process improvement.                │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## Key Principles

### 1. Everything Teaches

Every iteration—success or failure—contains information. A self-improving system extracts and preserves that information systematically.

### 2. Knowledge Compounds

Learning from iteration 50 should benefit from all 49 previous iterations. Knowledge must be structured to enable accumulation, not just collection.

### 3. Honest Self-Assessment

The system must evaluate itself without bias. Uncomfortable truths are more valuable than comfortable illusions.

### 4. Meta-Improvement

The ultimate capability: improving how the system improves. The learning process itself evolves.

### 5. Anti-Fragility

Failures don't just get recorded—they strengthen the system. Stress and challenge create growth.

---

## The Refinement Loops

Self-improvement happens through nested feedback loops operating at different timescales:

| Loop | Timescale | Purpose |
|------|-----------|---------|
| **Task** | Minutes | Execute → Evaluate → Reflect → Retry |
| **Session** | Hours | Complete → Summarize → Update memory |
| **Skill** | Days | Encounter pattern → Abstract → Test → Register |
| **Identity** | Weeks | Analyze patterns → Propose updates → Human review |
| **Architecture** | Months | Meta-analysis → Test new patterns → Evolve structure |

The **Ratchet Principle**: Improvements accumulate, failures don't. Every change goes through a testing gate. Successful modifications commit; failed ones rollback.

---

## The Recursa Architecture

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                         RECURSA ARCHITECTURE                                │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│                        ┌─────────────────┐                                  │
│                        │    EVOLUTION    │  Meta-layer                      │
│                        │  (improves the  │  "How do I improve               │
│                        │   improvement)  │   how I improve?"                │
│                        └────────┬────────┘                                  │
│                                 │                                           │
│          ┌──────────────────────┼──────────────────────┐                    │
│          │                      │                      │                    │
│          ▼                      ▼                      ▼                    │
│   ┌─────────────┐       ┌─────────────┐       ┌─────────────┐               │
│   │   MEMORY    │       │   METRICS   │       │ EVALUATION  │               │
│   │ (knowledge) │       │ (tracking)  │       │ (judgment)  │               │
│   └──────┬──────┘       └──────┬──────┘       └──────┬──────┘               │
│          │                     │                     │                      │
│          └─────────────────────┼─────────────────────┘                      │
│                                │                                            │
│                                ▼                                            │
│                        ┌─────────────────┐                                  │
│                        │      LOOP       │  Core process                    │
│                        │  (iteration     │  "What do I do                   │
│                        │   cycle)        │   each iteration?"               │
│                        └────────┬────────┘                                  │
│                                 │                                           │
│          ┌──────────────────────┼──────────────────────┐                    │
│          │                      │                      │                    │
│          ▼                      ▼                      ▼                    │
│   ┌─────────────┐       ┌─────────────┐       ┌─────────────┐               │
│   │  LEARNING   │       │   OUTPUTS   │       │   ISSUES    │               │
│   │(discoveries)│       │  (results)  │       │ (problems)  │               │
│   └─────────────┘       └─────────────┘       └─────────────┘               │
│                                                                             │
│                         Domain-Specific                                     │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## Documents in This Repository

### Usage Guides
| Document | Purpose |
|----------|---------|
| `AGENT.md` | Instructions for AI assistants on how to bootstrap projects |
| `BOOTSTRAPPING_GUIDE.md` | Detailed user guide for the bootstrapping process |
| `INTERVIEW.md` | Question bank for domain discovery |

### Core Philosophy
| Document | Purpose |
|----------|---------|
| `README.md` | This document: overview and principles |
| `ARCHITECTURE.md` | Seven layers, document stack, refinement loops |
| `DIRECTORY_STRUCTURE.md` | Comprehensive file organization |
| `BOOTSTRAP.md` | Step-by-step manual instantiation guide |

### Templates

**Identity & Governance**:
| Template | Purpose |
|----------|---------|
| `templates/ORIGIN.template.md` | Bootstrap context, interview answers, foundational purpose |
| `templates/SOUL.template.md` | Behavioral philosophy, values, identity |
| `templates/CONSTITUTION.template.md` | Inviolable rules, hard boundaries |
| `templates/GUARDRAILS.template.md` | Safety infrastructure, audit, rollback |

**Operational**:
| Template | Purpose |
|----------|---------|
| `templates/LOOP.template.md` | Core iteration cycle |
| `templates/MEMORY.template.md` | Knowledge preservation system |
| `templates/METRICS.template.md` | Quantitative tracking framework |
| `templates/LEARNING.template.md` | Discovery accumulation |
| `templates/EVOLUTION.template.md` | Self-improvement meta-system |
| `templates/GOALS.template.md` | Current objectives and priorities |
| `templates/EXPERIMENTS.template.md` | Hypothesis testing framework |
| `templates/STYLE.template.md` | Communication and formatting standards |
| `templates/IDENTITY.template.md` | Name, personality, presentation |

**Multi-Agent**:
| Template | Purpose |
|----------|---------|
| `templates/ORCHESTRATION.template.md` | Multi-agent coordination patterns |

### Tools

| Tool | Purpose |
|------|---------|
| `tools/recursa.py` | CLI for init, validate, status, log, migrate |
| `tools/validate.py` | Project structure validation |

```bash
# Initialize a new project
python tools/recursa.py init ~/my-project

# Validate project structure
python tools/recursa.py validate ~/my-project

# Check project status
python tools/recursa.py status ~/my-project

# Log an action
python tools/recursa.py log ~/my-project -a "edit" -m "Updated SOUL.md"

# Check for migrations
python tools/recursa.py migrate ~/my-project
```

### Research
| Document | Purpose |
|----------|---------|
| `references/Self_Improving_Agentic_Systems_Research_Report.md` | Comprehensive research on the field |

### Examples

Working examples demonstrating Recursa in different domains:

| Example | Domain | Description |
|---------|--------|-------------|
| `examples/minimal-blog-writer/` | Content Creation | Blog writing with quality tracking |
| `examples/code-review-system/` | Software Development | PR review with learning from feedback |
| `examples/research-assistant/` | Knowledge Work | Literature review and synthesis |
| `examples/personal-crm/` | Relationships | Contact management with outreach optimization |
| `examples/learning-tracker/` | Education | Study optimization with spaced repetition |

Each example includes customized SOUL.md, LOOP.md, LEARNING.md, and METRICS.md for its domain.

---

## Version & Migration

Recursa uses semantic versioning. Check your project version:

```bash
cat .recursa-version
```

Migrate existing projects to the latest framework:

```bash
python tools/recursa.py migrate ~/my-project --apply
```

See `MIGRATION.md` for detailed migration guides.

---

## The Promise

A Recursa-based system:

- **Gets better at getting better**
- **Compounds knowledge across iterations**
- **Learns from every failure**
- **Improves its own improvement process**
- **Approaches mastery asymptotically**

The goal: systems that become more capable with every cycle, forever.
