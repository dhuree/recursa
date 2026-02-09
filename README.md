# Recursa

**A blueprint for building self-improving systems in any domain.**

Recursa (from Latin *recursus* - "a running back") is a framework for creating intelligent systems that learn from their own operation, preserve knowledge across iterations, and continuously improve their capabilities.

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
| `CLAUDE.md` | Instructions for Claude Code on how to bootstrap projects |
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

### Research
| Document | Purpose |
|----------|---------|
| `references/Self_Improving_Agentic_Systems_Research_Report.md` | Comprehensive research on the field |

---

## How to Use Recursa

Recursa is a **meta-framework**. You don't use it directly—you use it to **bootstrap** new self-improving projects.

### Quick Start with Claude Code

```bash
# 1. Start Claude Code in the Recursa folder
cd /path/to/recursa
claude

# 2. Tell Claude to bootstrap a new project
> Bootstrap a self-improving project at /path/to/my-project

# 3. Answer Claude's questions about your domain
# 4. Review the generated files
# 5. Start using your new system!
```

### What Happens

1. **Claude reads** the templates and interview structure
2. **Claude asks** questions about your domain (purpose, workflow, metrics, etc.)
3. **Claude generates** customized versions of all documents in your target folder
4. **You review** and adjust the generated system
5. **You iterate** using your new self-improving system

### Example Commands

```
> Bootstrap a self-improving blog writing system at ~/blog

> Create a Recursa system for my fitness training at ~/fitness

> Set up a self-improving dev workflow at ~/myapp/workflow

> Bootstrap a minimal system for personal learning at ~/learning
```

### Detailed Guides

- `BOOTSTRAPPING_GUIDE.md` - Full walkthrough for users
- `CLAUDE.md` - Instructions for Claude Code
- `INTERVIEW.md` - Question bank for domain discovery

---

## Manual Setup (Without AI)

If you prefer to set up manually:

1. **Read** `ARCHITECTURE.md` to understand the patterns
2. **Follow** `BOOTSTRAP.md` step-by-step
3. **Copy** templates from `templates/` to your project
4. **Customize** each template for your domain
5. **Create** directory structure per `DIRECTORY_STRUCTURE.md`

---

## Origin

Recursa was extracted from a self-improving creative system for generating album art. That system demonstrated that structured memory, honest metrics, and systematic self-evaluation could transform a simple generation loop into a continuously improving intelligence.

The patterns proved to be domain-agnostic. This repository captures those patterns for application to any domain where iterative improvement is possible.

---

## The Promise

A Recursa-based system:

- **Gets better at getting better**
- **Compounds knowledge across iterations**
- **Learns from every failure**
- **Improves its own improvement process**
- **Approaches mastery asymptotically**

The goal: systems that become more capable with every cycle, forever.
