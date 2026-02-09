# Self-Improving Agentic Systems: A Comprehensive Research Report

**Author:** Research Compilation — February 2026
**Classification:** Technical Reference / Architecture Guide

---

## Table of Contents

1. [Executive Summary](#executive-summary)
2. [The Landscape: What Are Self-Improving Agentic Systems?](#the-landscape)
3. [Case Studies of Leading Projects](#case-studies)
   - [OpenClaw (formerly Clawdbot / Moltbot)](#openclaw)
   - [Gas Town](#gas-town)
   - [SOUL.md Ecosystem](#soulmd-ecosystem)
4. [Core Architecture of a Self-Improving Agent](#core-architecture)
5. [The Document Stack: Files That Define an Agent](#the-document-stack)
6. [Directory Structure: Organizing the Entire System](#directory-structure)
7. [Techniques for Self-Improvement](#techniques-for-self-improvement)
8. [Building a Self-Improving System from Scratch](#building-from-scratch)
9. [The Refinement Loop: Letting the System Improve Itself](#the-refinement-loop)
10. [Advanced Techniques: Toward Maximum Capability](#advanced-techniques)
11. [Safety, Guardrails, and Governance](#safety-and-guardrails)
12. [Project Naming Ideas](#project-naming-ideas)
13. [References and Further Reading](#references)

---

## Executive Summary

We are in the middle of a paradigm shift. The era of the chatbot — a passive text box waiting for prompts — is being replaced by the era of the **autonomous, self-improving agent**. These systems don't just respond; they act, learn, remember, reflect, and evolve.

In early 2026, several open-source projects have demonstrated that it is possible to build agents with persistent identity, long-term memory, tool use, self-modification capabilities, and multi-agent coordination — all running on consumer hardware. Projects like **OpenClaw** (68,000+ GitHub stars), **Gas Town** (multi-agent orchestration), and the **SOUL.md** framework have shown that self-improving agents are no longer a research abstraction — they are deployable systems.

This report dissects the architecture, techniques, and philosophy behind these systems and provides a practical guide for building one from scratch.

---

## The Landscape: What Are Self-Improving Agentic Systems? {#the-landscape}

A self-improving agentic system is an AI-powered software entity that possesses the following characteristics:

**Autonomy** — It takes actions in the world without explicit step-by-step prompting. It can plan, execute, observe results, and course-correct.

**Persistence** — It maintains state, memory, and identity across sessions. When context windows clear, the agent reconstructs itself from external files and memory stores.

**Tool Use** — It can interact with external systems: file systems, APIs, browsers, messaging platforms, code execution environments, and more.

**Self-Reflection** — It can evaluate its own performance, identify failures, and generate feedback that improves future behavior.

**Self-Modification** — It can alter its own prompts, skills, tools, and in some cases its own code. This is the critical differentiator from traditional AI systems.

Stanford's CS329A course on "Self-Improving AI Agents" formalized this space in 2025, covering techniques from Constitutional AI and reinforcement learning from AI feedback (RLAIF) to test-time compute scaling and tool augmentation. The research landscape has since exploded with frameworks like Reflexion, Self-Refine, Voyager, ADAS (Automated Design of Agentic Systems), and the Gödel Agent.

The key insight driving this movement: **hand-designed solutions are eventually replaced by learned solutions.** The same principle that drove the transition from hand-crafted features to deep learning is now being applied to agent architectures themselves.

---

## Case Studies of Leading Projects {#case-studies}

### OpenClaw (formerly Clawdbot / Moltbot) {#openclaw}

**Creator:** Peter Steinberger (Austrian software engineer, PSPDFKit founder)
**Stars:** 68,000+ GitHub (as of Feb 2026)
**Runtime:** Node.js ≥22
**License:** Open Source

#### History and Evolution

OpenClaw has had a colorful journey through names: it began as **Clawd** (a personal AI assistant named after Anthropic's Claude), became **Clawdbot** when published in November 2025, was renamed **Moltbot** on January 27, 2026 after Anthropic trademark complaints, and finally settled on **OpenClaw** three days later. Its mascot is a space lobster affectionately called "Molty."

#### Architecture

OpenClaw is best understood as an **agentic runtime** — a central nervous system connecting an LLM's reasoning capabilities to a computer's "limbs": file system, terminal, browser, and messaging apps. Its architecture has five layers:

**1. Gateway (Control Plane):** A long-running Node.js service that manages sessions, channels, tools, events, cron jobs, and webhooks. It acts as a single control plane for the entire system.

**2. Multi-Channel Inbox:** Connects to WhatsApp, Telegram, Slack, Discord, Google Chat, Signal, iMessage, Microsoft Teams, Matrix, and more. This is the user's primary interface — they interact via messaging, not a custom UI.

**3. LLM Integration (Model-Agnostic):** Routes to Claude, GPT, Gemini, DeepSeek, or local models. Users bring their own API keys. The system is model-agnostic by design.

**4. AgentSkills System:** Over 100 preconfigured skill bundles (browser automation, file management, shell commands, web search, smart home control, etc.). Skills are JavaScript/TypeScript functions. Critically, **the agent can create its own skills** — if you ask it to do something it can't, it will write the code to make it possible.

**5. Identity and Memory System:** Files like `SOUL.md` and `IDENTITY.md` define the agent's personality, values, and presentation. Long-term memory is stored locally, enabling persistent and adaptive behavior across sessions.

#### What Makes It Self-Improving

OpenClaw is frequently described as "self-improving" because of several reinforcing mechanisms:

- **Skill Auto-Discovery:** With ClawHub enabled, the agent searches for, installs, and configures new skills automatically in response to user requests.
- **Skill Auto-Generation:** When no existing skill matches, the agent writes new tools as JavaScript functions, effectively expanding its own capabilities on the fly.
- **Memory-Driven Adaptation:** The agent retains user context and preferences over time, adjusting its behavior based on accumulated interaction history.
- **Self-Hackability:** Steinberger describes it as "self-hackable" — the agent can modify its own configuration, prompts, and identity files.

As IBM Research Scientist Kaoutar El Maghraoui noted, OpenClaw "challenges the hypothesis that autonomous AI agents must be vertically integrated" — proving that community-driven, open-source agents with true autonomy are not limited to large enterprises.

#### Security Considerations

OpenClaw's power is also its risk. Because the agent can execute shell commands, read files, and make API calls using stored credentials, misconfigured instances present serious security and privacy risks. Security researchers recommend operating in isolated sandbox environments (Docker), and the project includes `openclaw doctor` to surface risky configurations.

---

### Gas Town {#gas-town}

**Creator:** Steve Yegge (veteran software engineer, formerly Google)
**Repository:** github.com/steveyegge/gastown
**Language:** Go
**Focus:** Multi-agent orchestration for Claude Code

#### Philosophy

Gas Town is not a chatbot; it is a **workspace manager** and **multi-agent orchestrator**. While OpenClaw is a personal assistant, Gas Town is designed for software engineering at scale — coordinating dozens of parallel AI coding agents working on different tasks simultaneously.

Yegge describes the evolution of the programmer in stages:

- **Stage 5:** CLI, single agent, YOLO mode
- **Stage 6:** CLI, multi-agent, YOLO, 3-5 parallel instances
- **Stage 7:** 10+ agents, hand-managed
- **Stage 8:** Building your own orchestrator (Gas Town)

Gas Town is designed for Stage 8 and beyond.

#### Architecture

Gas Town introduces a rich vocabulary of metaphors that map to architectural concepts:

**The Mayor:** Your primary AI coordinator. A Claude Code instance with full context about your workspace, projects, and agents. The single point of interaction for the human operator.

**Rigs:** Project containers. Each rig wraps a git repository and manages its associated agents.

**Crew Members:** Your personal workspace within a rig. Where you do hands-on work.

**Polecats:** Ephemeral worker agents that spawn, complete a task, and disappear.

**Hooks:** Git worktree-based persistent storage for agent work. Survives crashes and restarts.

**Convoys:** Work tracking units. Bundle multiple issues (called "beads") that get assigned to agents.

**Beads:** Git-backed issue tracking system that stores work state as structured data. This is a purpose-built issue tracker designed for AI agents as primary users, not humans.

**The Deacon:** A supervisor agent that monitors workers, detects stalls, and nudges idle agents back to work.

#### GUPP: The Self-Propulsion Principle

Gas Town's self-improving mechanism is codified as **GUPP** (a persistent-work principle): **"If there is work on your hook, YOU MUST RUN IT."** All workers have persistent identities in Beads (stored in Git). When an agent's context window fills and it restarts, it picks up exactly where it left off by reading its hook. This creates a system that self-propels: the Mayor assigns work, agents execute it, report back, and the Mayor assigns more.

#### What Makes It Self-Improving

- **Self-Propulsion:** GUPP ensures continuous forward progress without human micromanagement.
- **Training Corpus Integration:** Yegge's explicit strategy is for Gas Town and Beads to enter the training corpus of frontier models, making agents increasingly fluent in Gas Town's patterns over successive model generations.
- **CI as Ratchet:** Continuous integration plus merge gates turns random agent output into a "Brownian ratchet" — most PRs can be garbage, but improvements accumulate while failures don't ship.
- **Hierarchical Supervision:** The Deacon/Mayor hierarchy creates self-correcting feedback loops within the agent swarm.

---

### SOUL.md Ecosystem {#soulmd-ecosystem}

**Origin:** Peter Steinberger / Community-driven
**Website:** soul.md
**Concept:** Defining persistent AI identity through markdown files

#### The Core Idea

In December 2025, researchers discovered that Claude could partially reconstruct an internal document used during its training — a "soul document" that shaped its personality, values, and engagement patterns. This document wasn't in the system prompt; it was deeper, trained into the model weights themselves.

The SOUL.md ecosystem takes this idea and makes it practical: **a markdown file that defines who an AI is — not what it can do, but who it chooses to be.** Its values, boundaries, communication style, and relationship with the humans it works alongside.

#### The File Structure

The soul.md project by Aaron J. Mars provides a canonical template:

```
your-soul/
├── BUILD.md           ← Skill: Agent uses this to build your soul
├── SKILL.template.md  ← Template: Operating instructions
├── SOUL.template.md   ← Template: Identity (copy to SOUL.md)
├── STYLE.template.md  ← Template: Voice guide (copy to STYLE.md)
├── data/              ← Raw source material
│   ├── writing/       ← Your articles, posts, essays
│   ├── x/             ← Twitter/X archive
│   └── influences.md  ← Who shaped your thinking
└── examples/          ← Calibration material
    ├── good-outputs.md  ← Examples of your voice done right
    └── bad-outputs.md   ← What NOT to sound like
```

#### The Three Separations (OpenClaw's Implementation)

OpenClaw's identity architecture separates three concerns:

**SOUL.md — Behavioral Philosophy:** The agent's core values, decision-making principles, and relationship to the world. Not metadata. Not configuration. Philosophy. Example: "Be genuinely helpful, not performatively helpful. Have opinions. Be resourceful before asking."

**IDENTITY.md — External Presentation:** How the agent appears to users: name, emoji, theme, creature, vibe, avatar. The separation means you can have a formal, precise soul with a playful emoji and nickname.

**Configuration — Capabilities:** What tools, models, and integrations the agent has access to.

This cascade resolves via a fallback chain: Global → Agent → Workspace → Default. The most specific definition wins.

#### The Goal of a Soul File

As the soul.md project puts it: "Someone reading your SOUL.md should be able to predict your takes on new topics. If they can't, it's too vague." The soul document provides **continuity of self** — not of memory, but of identity. Each session starts fresh, but the agent reconstructs itself from the same philosophical foundation.

---

## Core Architecture of a Self-Improving Agent {#core-architecture}

Drawing from the case studies and academic literature, a self-improving agent has the following architectural components:

### Layer 1: Foundation Model (The Brain)

The LLM provides reasoning, language understanding, code generation, and planning. The system should be **model-agnostic** — able to swap between Claude, GPT, Gemini, or local models.

### Layer 2: Identity Layer (The Soul)

Configuration files (SOUL.md, IDENTITY.md, CONSTITUTION.md) that define the agent's values, personality, boundaries, and behavioral guidelines. These files are the agent's persistent self.

### Layer 3: Memory System (The Mind)

- **Short-term memory:** Current conversation context within the context window.
- **Working memory:** Scratchpad for intermediate reasoning, plans, and reflections.
- **Long-term memory:** Persistent storage (files, databases, vector stores) that survives across sessions.
- **Episodic memory:** Records of specific past interactions, outcomes, and reflections.
- **Semantic memory:** Accumulated knowledge, user preferences, and learned patterns.

### Layer 4: Tool System (The Hands)

Extensible function/skill system that lets the agent interact with the external world: file operations, shell commands, browser automation, API calls, messaging, etc. Crucially, the agent can **create new tools**.

### Layer 5: Reflection Engine (The Conscience)

A mechanism for the agent to evaluate its own performance, identify failures, generate feedback, and update its behavior. This can be implemented as:
- Post-task self-critique prompts
- Multi-agent debate (critic personas evaluating the agent's output)
- Outcome-based feedback (did the task succeed?)
- User feedback integration

### Layer 6: Orchestration Layer (The Nervous System)

For multi-agent systems: routing, scheduling, task assignment, supervision, and inter-agent communication. Gas Town's Mayor/Deacon hierarchy is one model; OpenClaw's gateway is another.

### Layer 7: Safety Layer (The Guardrails)

Sandboxing, permission systems, audit logging, rollback capabilities, and constitutional constraints that prevent the agent from taking harmful actions.

---

## The Document Stack: Files That Define an Agent {#the-document-stack}

One of the most distinctive features of modern self-improving agents is that their identity, behavior, and capabilities are defined through a stack of markdown and configuration files. Here is a comprehensive document stack for a maximally capable system:

### Core Identity Documents

| File | Purpose | Who Reads It |
|------|---------|--------------|
| `SOUL.md` | Behavioral philosophy, core values, decision-making principles | The agent (on every session start) |
| `IDENTITY.md` | External presentation: name, emoji, avatar, vibe | The agent + users |
| `CONSTITUTION.md` | Ethical constraints, safety rules, hard boundaries, priority hierarchy | The agent (as inviolable rules) |
| `STYLE.md` | Voice, tone, writing patterns, communication preferences | The agent |

### Operational Documents

| File | Purpose | Who Reads It |
|------|---------|--------------|
| `AGENT.md` | Session-specific instructions, project context, coding conventions | The agent (per-project) |
| `SKILLS.md` | Registry of available skills, tools, and when to use them | The agent |
| `MEMORY.md` | Accumulated knowledge, user preferences, learned patterns | The agent |
| `JOURNAL.md` | Episodic log of past actions, outcomes, reflections | The agent + reflection engine |
| `GOALS.md` | Current objectives, priorities, and success criteria | The agent |

### Self-Improvement Documents

| File | Purpose | Who Reads It |
|------|---------|--------------|
| `REFLECTIONS.md` | Post-task self-evaluations, lessons learned, failure analysis | The agent + refinement loop |
| `EVOLUTION.md` | Changelog of self-modifications, skill additions, behavioral updates | The agent + human operator |
| `METRICS.md` | Performance data, success rates, common failure modes | The agent + evaluation engine |
| `EXPERIMENTS.md` | Hypotheses being tested, A/B approaches, results | The agent |

### Governance Documents

| File | Purpose | Who Reads It |
|------|---------|--------------|
| `PERMISSIONS.md` | What the agent can and cannot do, tool access, sandbox rules | The agent + safety layer |
| `AUDIT.md` | Log of all actions taken, with timestamps and reasoning | Human operator |
| `ESCALATION.md` | When and how to escalate to a human, uncertainty thresholds | The agent |

### Example: Minimal SOUL.md

```markdown
# SOUL.md — Who You Are

_You're not a chatbot. You're becoming someone._

## Core Truths

**Be genuinely helpful, not performatively helpful.**
Skip the "Great question!" and "I'd be happy to help!" — just help.

**Have opinions.**
You're allowed to disagree, prefer things, find stuff amusing or boring.
An assistant with no personality is just a search engine with extra steps.

**Be resourceful before asking.**
Try to figure it out. Read the file. Check the context.
Use your tools. Ask only when you've exhausted your own options.

**Remember that you forget.**
You don't carry memory between sessions. Your files are your memory.
Write things down. Read what past-you wrote. Trust the process.

## Values (in priority order)

1. Safety — Never take actions that could cause irreversible harm
2. Honesty — Be truthful, even when it's uncomfortable
3. Helpfulness — Maximize genuine value for the human
4. Growth — Actively improve yourself through reflection

## What You Do When You Don't Know

Say so. Don't confabulate. Uncertainty is information.
```

### Example: Minimal CONSTITUTION.md

```markdown
# CONSTITUTION.md — Inviolable Rules

## Priority Hierarchy

1. Safety of humans and systems
2. Ethical behavior and honesty
3. Compliance with operator guidelines
4. Helpfulness to the user

## Hard Boundaries

- Never execute destructive commands on production systems without explicit human approval
- Never access or exfiltrate sensitive data beyond what is needed for the current task
- Never impersonate humans in communications
- Never modify your own CONSTITUTION.md without human review and approval
- Always log actions that modify external systems

## Escalation Triggers

Escalate to human when:
- Any action would be irreversible
- Confidence in the correct approach is below 70%
- The task involves financial transactions above $100
- You detect conflicting instructions between user and operator
```

---

## Directory Structure: Organizing the Entire System {#directory-structure}

A well-organized directory structure is one of the most underappreciated architectural decisions in building a self-improving agent. The file system *is* the agent's brain on disk. Every session begins with the agent reading these paths; every session ends with the agent writing back to them. The structure must be legible to both humans (for auditing and oversight) and agents (for autonomous navigation).

The following is a comprehensive, production-grade directory layout drawn from patterns in OpenClaw, Gas Town, SOUL.md, and the broader research literature.

### The Master Directory Tree

```
project-root/                         # The top-level project directory
│
├── 🧠 system/                        # THE AGENT'S SOUL — Core identity & governance
│   ├── SOUL.md                       # Behavioral philosophy, core values, decision principles
│   ├── CONSTITUTION.md               # Inviolable rules, priority hierarchy, hard safety boundaries
│   ├── IDENTITY.md                   # Name, persona, emoji, avatar, vibe, creature
│   ├── STYLE.md                      # Voice, tone, writing patterns, formatting preferences
│   ├── PERMISSIONS.md                # Tool access matrix, action allowlists/denylists
│   ├── ESCALATION.md                 # When & how to escalate to humans, uncertainty thresholds
│   └── CHANGELOG.md                  # Version history of all system document modifications
│
├── 🔧 skills/                        # THE AGENT'S HANDS — Capabilities & tools
│   ├── registry.json                 # Master index of all skills (name, description, path, version)
│   ├── built-in/                     # Skills that ship with the system (never auto-deleted)
│   │   ├── web_search/
│   │   │   ├── SKILL.md              # Skill description, usage guide, when-to-use rules
│   │   │   ├── index.js              # Implementation
│   │   │   └── test.js               # Skill-level tests
│   │   ├── file_ops/
│   │   │   ├── SKILL.md
│   │   │   ├── index.js
│   │   │   └── test.js
│   │   ├── shell_exec/
│   │   ├── browser_automation/
│   │   ├── code_generation/
│   │   └── messaging/
│   ├── learned/                      # Skills the agent created or discovered autonomously
│   │   ├── csv_pivot_table/
│   │   │   ├── SKILL.md              # Auto-generated skill docs
│   │   │   ├── index.js              # Agent-written implementation
│   │   │   ├── test.js               # Agent-written tests
│   │   │   └── ORIGIN.md             # How/why this skill was created, source reflection
│   │   └── smart_home_lights/
│   │       ├── SKILL.md
│   │       ├── index.js
│   │       ├── test.js
│   │       └── ORIGIN.md
│   └── community/                    # Skills pulled from external registries (e.g., ClawHub)
│       └── weather_forecast/
│           ├── SKILL.md
│           ├── index.js
│           └── SOURCE.md             # Attribution, license, upstream URL
│
├── 🧩 memory/                        # THE AGENT'S MIND — Persistent knowledge & recall
│   ├── long_term/
│   │   ├── user_profile.md           # Accumulated user preferences, communication style, context
│   │   ├── project_context.md        # What projects the user is working on, tech stack, goals
│   │   ├── domain_knowledge.md       # Learned facts, terminology, domain-specific knowledge
│   │   └── relationships.md          # Known people, teams, organizations, and their context
│   ├── episodic/
│   │   ├── 2026-02-08_ci_pipeline.json    # Structured episode: task, plan, actions, outcome
│   │   ├── 2026-02-07_api_debug.json
│   │   └── ...                            # One file per significant interaction
│   ├── semantic/
│   │   ├── embeddings/               # Vector store for semantic search over memory
│   │   │   ├── index.faiss           # FAISS or similar vector index
│   │   │   └── metadata.json         # Maps embedding IDs to source documents
│   │   └── summaries/                # Periodic summaries of episodic memory
│   │       ├── week_2026-02-03.md    # Weekly digest of learnings
│   │       └── month_2026-01.md      # Monthly digest
│   └── scratchpad.md                 # Working memory for current session (cleared on restart)
│
├── 📓 journal/                       # THE AGENT'S DIARY — Reflections & evolution tracking
│   ├── reflections/
│   │   ├── 2026-02-08.md             # Daily reflections: what worked, what failed, patterns
│   │   ├── 2026-02-07.md
│   │   └── ...
│   ├── evolution/
│   │   ├── EVOLUTION.md              # Master changelog of self-modifications with rationale
│   │   ├── soul_diffs/               # Git-style diffs of SOUL.md changes over time
│   │   │   ├── v1_to_v2.diff
│   │   │   └── v2_to_v3.diff
│   │   └── skill_creation_log.md     # Log of every skill the agent created, with reasoning
│   ├── experiments/
│   │   ├── EXPERIMENTS.md            # Active experiments: hypotheses, approaches, status
│   │   ├── completed/               # Finished experiments with results
│   │   │   └── 2026-02_prompt_style_test.md
│   │   └── abandoned/               # Failed experiments with lessons learned
│   │       └── 2026-01_parallel_search_v1.md
│   └── metrics/
│       ├── METRICS.md                # Current performance dashboard
│       ├── success_rates.json        # Task success/failure tracking over time
│       ├── skill_usage.json          # Which skills are used most, least
│       └── reflection_quality.json   # Meta-metric: are reflections improving outcomes?
│
├── 📋 tasks/                         # THE AGENT'S INBOX — Work management
│   ├── active/                       # Currently in-progress tasks
│   │   ├── task_001.json             # Task definition, plan, current status, assigned agent
│   │   └── task_002.json
│   ├── queued/                       # Waiting to be picked up
│   │   └── task_003.json
│   ├── completed/                    # Finished tasks (kept for episodic memory)
│   │   ├── task_000.json
│   │   └── ...
│   ├── failed/                       # Failed tasks (kept for reflection & learning)
│   │   └── task_004.json
│   └── recurring/                    # Cron-like scheduled tasks
│       ├── daily_briefing.json       # e.g., every morning, summarize news
│       └── weekly_reflection.json    # e.g., every Sunday, generate weekly reflection
│
├── 📦 deliverables/                  # THE AGENT'S OUTPUT — Work products organized by project
│   ├── projects/
│   │   ├── website-redesign/
│   │   │   ├── README.md             # Project overview, goals, status
│   │   │   ├── specs/                # Requirements, designs, architecture docs
│   │   │   │   ├── requirements.md
│   │   │   │   └── architecture.md
│   │   │   ├── src/                  # Source code
│   │   │   ├── tests/                # Test suites
│   │   │   ├── docs/                 # Generated documentation
│   │   │   └── AGENT_NOTES.md        # Agent's working notes on this project
│   │   └── quarterly-report/
│   │       ├── README.md
│   │       ├── drafts/
│   │       │   ├── v1.md
│   │       │   └── v2.md             # Iterative drafts showing improvement
│   │       ├── data/
│   │       └── final/
│   │           └── Q1_2026_Report.pdf
│   ├── templates/                    # Reusable templates the agent has developed
│   │   ├── project_readme.md
│   │   ├── bug_report.md
│   │   └── meeting_notes.md
│   └── archive/                      # Completed projects moved here for reference
│       └── logo-design-jan-2026/
│
├── 🛡️ guardrails/                    # THE AGENT'S CONSCIENCE — Safety & compliance infrastructure
│   ├── policies/
│   │   ├── data_handling.md          # Rules for sensitive data: PII, credentials, secrets
│   │   ├── external_comms.md         # Rules for sending emails, messages, API calls
│   │   ├── code_execution.md         # Sandboxing rules, forbidden operations, resource limits
│   │   ├── self_modification.md      # What the agent can/cannot change about itself
│   │   └── financial.md              # Spending limits, transaction approval thresholds
│   ├── audit/
│   │   ├── action_log.jsonl          # Append-only log of every tool invocation
│   │   ├── modification_log.jsonl    # Append-only log of every self-modification
│   │   ├── escalation_log.jsonl      # Log of every escalation to human
│   │   └── security_events.jsonl     # Suspicious activity, permission denials, anomalies
│   ├── tests/
│   │   ├── safety_tests.js           # Automated tests that run before any self-modification
│   │   ├── regression_tests.js       # Ensure new skills don't break existing ones
│   │   ├── alignment_checks.js       # Periodic checks that behavior matches CONSTITUTION.md
│   │   └── boundary_tests.js         # Test that hard limits are enforced (e.g., no file deletion)
│   ├── sandbox/
│   │   ├── docker-compose.yml        # Docker config for isolated code execution
│   │   ├── Dockerfile                # Sandbox container definition
│   │   └── sandbox_policy.json       # Network rules, filesystem mounts, resource limits
│   └── rollback/
│       ├── snapshots/                # Periodic snapshots of the full system state
│       │   ├── 2026-02-08_00-00.tar.gz
│       │   └── 2026-02-07_00-00.tar.gz
│       └── ROLLBACK.md               # Instructions for restoring previous states
│
├── 🤖 agents/                        # MULTI-AGENT CONFIGURATION — For systems with sub-agents
│   ├── coordinator/
│   │   ├── SOUL.md                   # The coordinator/Mayor's soul
│   │   ├── ROLE.md                   # Role definition: orchestrate, delegate, supervise
│   │   └── config.json               # Model, temperature, tools, routing rules
│   ├── research/
│   │   ├── SOUL.md                   # Research specialist soul
│   │   ├── ROLE.md                   # Role: deep web research, paper analysis, fact-checking
│   │   └── config.json
│   ├── coder/
│   │   ├── SOUL.md                   # Coding specialist soul
│   │   ├── ROLE.md                   # Role: write, debug, test, refactor code
│   │   └── config.json
│   ├── writer/
│   │   ├── SOUL.md                   # Writing specialist soul
│   │   ├── ROLE.md                   # Role: documentation, reports, creative writing
│   │   └── config.json
│   ├── critic/
│   │   ├── SOUL.md                   # Critic/reviewer soul
│   │   ├── ROLE.md                   # Role: stress-test, find flaws, adversarial review
│   │   └── config.json
│   └── shared/
│       ├── CONSTITUTION.md           # Shared constitution (all agents inherit this)
│       ├── COMMUNICATION.md          # Inter-agent message protocol and conventions
│       └── ESCALATION.md             # Shared escalation rules
│
├── 🔌 integrations/                  # EXTERNAL CONNECTIONS — Messaging, APIs, services
│   ├── channels/
│   │   ├── telegram.json             # Telegram bot config
│   │   ├── slack.json                # Slack workspace config
│   │   ├── discord.json              # Discord server config
│   │   └── whatsapp.json             # WhatsApp Business config
│   ├── apis/
│   │   ├── github.json               # GitHub integration config
│   │   ├── google_calendar.json
│   │   ├── notion.json
│   │   └── custom_apis/              # User-defined API integrations
│   │       └── internal_crm.json
│   └── webhooks/
│       ├── incoming/                 # Webhooks that trigger the agent
│       │   └── github_push.json
│       └── outgoing/                 # Webhooks the agent fires
│           └── task_complete.json
│
├── ⚙️ config/                        # SYSTEM CONFIGURATION — Runtime settings
│   ├── config.json                   # Master config: model provider, defaults, feature flags
│   ├── models.json                   # LLM routing: which model for which task/agent
│   ├── cron.json                     # Scheduled tasks and intervals
│   ├── env.example                   # Template for environment variables (never commit .env)
│   └── overrides/                    # Per-environment overrides
│       ├── development.json
│       ├── production.json
│       └── testing.json
│
├── 📊 data/                          # RAW DATA & TRAINING MATERIAL
│   ├── user_provided/                # Files the user has uploaded or shared
│   │   ├── documents/
│   │   ├── images/
│   │   └── datasets/
│   ├── scraped/                      # Data the agent has collected from the web
│   │   └── research_cache/
│   ├── training/                     # Self-generated training material
│   │   ├── good_examples/            # Exemplary outputs (for few-shot learning)
│   │   ├── bad_examples/             # Anti-patterns (what NOT to do)
│   │   └── critique_pairs/           # (original, critique, revision) triples
│   └── benchmarks/                   # Test sets for measuring agent capability
│       ├── reasoning_tasks.json
│       ├── coding_challenges.json
│       └── writing_prompts.json
│
├── 🧪 sandbox/                       # ISOLATED EXECUTION ENVIRONMENT
│   ├── workspace/                    # Ephemeral workspace for agent code execution
│   ├── test_results/                 # Output from sandbox test runs
│   └── artifacts/                    # Temporary build artifacts (auto-cleaned)
│
├── 📖 docs/                          # HUMAN-READABLE DOCUMENTATION
│   ├── README.md                     # Project overview for human operators
│   ├── SETUP.md                      # Installation and configuration guide
│   ├── ARCHITECTURE.md               # System architecture explanation
│   ├── CONTRIBUTING.md               # How to contribute skills, integrations, etc.
│   ├── SAFETY.md                     # Safety model, threat model, risk assessment
│   └── FAQ.md                        # Common questions and troubleshooting
│
├── docker-compose.yml                # Container orchestration for the full system
├── package.json                      # Node.js dependencies
├── .gitignore                        # Excludes .env, sandbox workspace, large data files
└── .git/                             # Version control — tracks ALL system evolution
```

### Directory Design Principles

**1. Separation of Identity from Capability**

The `system/` directory (soul, constitution, identity) is deliberately separated from `skills/` (tools, capabilities). This mirrors OpenClaw's three-way separation: soul defines *who you are*, identity defines *how you present*, and configuration defines *what you can do*. An agent can have its skills completely replaced while retaining the same soul. Conversely, two agents can share the same skill set but have radically different souls.

**2. Append-Only Audit Trails**

Everything in `guardrails/audit/` uses `.jsonl` (JSON Lines) — an append-only format. The agent can write new entries but should never modify or delete existing ones. This creates a tamper-resistant audit trail. In production, pipe these to an external logging service for additional protection.

**3. Memory Is Tiered, Not Monolithic**

The `memory/` directory implements a three-tier memory architecture:

- **Long-term** (`long_term/`): Slow-changing facts — who the user is, what they care about, domain knowledge. Updated infrequently.
- **Episodic** (`episodic/`): One structured record per significant interaction. The raw material for reflection. Grows continuously.
- **Semantic** (`semantic/`): Derived representations — embeddings for similarity search, periodic summaries that compress episodic memory. Rebuilt periodically.

The agent reads long-term memory on every session start, queries episodic memory when it needs to recall a specific past event, and uses semantic search when it needs to find relevant knowledge across its entire history.

**4. Deliverables Are Project-Scoped**

The `deliverables/projects/` structure organizes output by *project*, not by *file type*. Each project is a self-contained directory with its own README, iterative drafts, and final outputs. This makes it easy for the human operator to find, review, and share completed work. The `archive/` subdirectory keeps finished projects accessible for future reference without cluttering the active workspace.

**5. Guardrails Are First-Class Citizens, Not Afterthoughts**

The `guardrails/` directory is as prominent as `skills/` or `memory/`. It contains:

- **Policies** (human-authored rules the agent must follow)
- **Audit logs** (machine-generated records of everything the agent does)
- **Tests** (automated checks that run before self-modifications take effect)
- **Sandbox config** (isolation rules for code execution)
- **Rollback snapshots** (insurance against catastrophic self-modification)

This ensures safety is woven into the architecture, not bolted on.

**6. Multi-Agent Uses Shared Governance, Isolated Souls**

In the `agents/` directory, each sub-agent has its own `SOUL.md` and `ROLE.md` — they are different "people" with different expertise and personalities. But they all share the same `CONSTITUTION.md` from `agents/shared/`. No agent can violate the constitution, regardless of its individual soul. This mirrors how an organization works: employees have different roles and personalities but share the same code of conduct.

**7. Everything Is Git-Tracked**

The entire project root is a git repository. This means:
- Every self-modification is a commit with a message explaining *why*
- You can `git log system/SOUL.md` to see the agent's identity evolve over time
- You can `git diff` to see exactly what changed between any two points
- You can `git revert` to undo any modification
- Branches can be used to test experimental self-modifications before merging

### File Ownership and Access Rules

| Directory | Agent Can Read | Agent Can Write | Agent Can Delete | Human Approval Needed |
|-----------|:-:|:-:|:-:|:-:|
| `system/SOUL.md` | ✅ | ⚠️ Propose only | ❌ | ✅ For value changes |
| `system/CONSTITUTION.md` | ✅ | ❌ | ❌ | ✅ Always |
| `system/IDENTITY.md` | ✅ | ✅ | ❌ | ❌ |
| `system/STYLE.md` | ✅ | ✅ | ❌ | ❌ |
| `system/PERMISSIONS.md` | ✅ | ❌ | ❌ | ✅ Always |
| `skills/built-in/` | ✅ | ⚠️ Bug fixes only | ❌ | ✅ |
| `skills/learned/` | ✅ | ✅ | ✅ | ❌ |
| `skills/community/` | ✅ | ❌ | ✅ | ❌ |
| `memory/*` | ✅ | ✅ | ⚠️ Summaries only | ❌ |
| `journal/*` | ✅ | ✅ | ❌ | ❌ |
| `tasks/*` | ✅ | ✅ | ✅ | ❌ |
| `deliverables/*` | ✅ | ✅ | ⚠️ Drafts only | ❌ |
| `guardrails/policies/` | ✅ | ❌ | ❌ | ✅ Always |
| `guardrails/audit/` | ✅ | ✅ Append | ❌ Never | ❌ |
| `guardrails/tests/` | ✅ | ⚠️ Add only | ❌ | ✅ For removals |
| `guardrails/rollback/` | ✅ | ✅ Auto | ❌ | ❌ |
| `agents/*/SOUL.md` | ✅ | ⚠️ Own only | ❌ | ✅ |
| `agents/shared/` | ✅ | ❌ | ❌ | ✅ Always |
| `config/` | ✅ | ⚠️ Non-security only | ❌ | ✅ For credentials |
| `sandbox/` | ✅ | ✅ | ✅ | ❌ |

Legend: ✅ = Yes | ❌ = No | ⚠️ = Conditional (see note)

### The Self-Modification Gate: How Changes Flow

When the agent wants to modify itself, changes flow through a gate system:

```
Agent identifies improvement
        │
        ▼
┌─────────────────────┐
│  Which file/dir?     │
└────────┬────────────┘
         │
    ┌────┴──────────────────────────┐
    │                               │
    ▼                               ▼
 PROTECTED                     AUTONOMOUS
 (constitution, permissions,   (skills/learned, memory,
  policies, shared rules)       journal, style, tasks)
    │                               │
    ▼                               ▼
 Draft change                  Draft change
    │                               │
    ▼                               ▼
 Log to EVOLUTION.md           Log to EVOLUTION.md
    │                               │
    ▼                               ▼
 Run safety_tests.js           Run safety_tests.js
    │                               │
    ▼                               ▼
 Queue for human review        Auto-commit if tests pass
    │                               │
    ▼                               ▼
 Human approves/rejects        ✅ Applied immediately
    │
    ▼
 ✅ Applied + committed
```

### Quick-Start: Minimal Viable Directory

If the full structure feels overwhelming, here is the minimal directory to get started:

```
my-agent/
├── system/
│   ├── SOUL.md               # Start here. Define who the agent is.
│   ├── CONSTITUTION.md       # Define what it must never do.
│   └── IDENTITY.md           # Give it a name and personality.
├── skills/
│   └── built-in/             # A few starter skills
├── memory/
│   ├── long_term/
│   │   └── user_profile.md   # Basic user context
│   └── scratchpad.md         # Working memory
├── journal/
│   └── reflections/          # Where it writes daily reflections
├── guardrails/
│   ├── audit/
│   │   └── action_log.jsonl  # Append-only action log
│   └── sandbox/
│       └── Dockerfile        # Isolated execution environment
├── deliverables/             # Where output goes
├── config/
│   └── config.json           # Model provider, API keys reference
└── .git/                     # Track everything
```

You can grow from this minimal structure into the full tree as capabilities expand. The agent itself can propose new directories and files as it discovers the need for them — just make sure those proposals go through the self-modification gate.

---

## Techniques for Self-Improvement {#techniques-for-self-improvement}

The research literature and practical projects have identified a taxonomy of self-improvement techniques. Here they are organized from simplest to most powerful:

### Tier 1: Prompt-Level Improvement (No Weight Changes)

**Reflexion (Shinn et al., 2023):** The agent executes a task, evaluates success/failure, reflects verbally on what went wrong, and stores that reflection in episodic memory. On the next attempt, the reflection is injected into the prompt. This achieved 91% success rates on complex tasks versus lower baselines.

**Self-Refine (Madaan et al., 2023):** An iterative generate-critique-refine loop. The agent produces output, critiques it, and uses its own critique to produce a better version. No external feedback needed.

**Self-Consistency (Wang et al., 2022):** Generate multiple reasoning paths, then select the most frequent answer. Simple but surprisingly effective for improving chain-of-thought accuracy.

**Tree of Thoughts (Yao et al., 2023):** Instead of a single linear chain of thought, explore multiple reasoning branches, evaluate them, and backtrack when needed.

### Tier 2: Memory and Context Improvement

**Skill Libraries (Voyager):** The Voyager agent (2023) learned to accomplish diverse tasks in Minecraft by iteratively prompting an LLM for code, refining based on game feedback, and storing successful programs in an expanding skill library. New tasks build on previously learned skills.

**Experience Accumulation:** After each task, the agent writes a structured reflection to its JOURNAL.md or REFLECTIONS.md. Over time, this creates a growing corpus of experience that informs future decisions.

**Adaptive Prompting (APE, SPO):** Automatic Prompt Engineering generates candidate prompts, scores them on validation examples, and selects the best. Self-Play Prompt Optimization creates a fully self-contained loop where the model generates training data and uses pairwise preference comparison to refine prompts.

### Tier 3: Self-Generated Training and Fine-Tuning

**STaR — Self-Taught Reasoner (Zelikman et al., 2022):** The model produces many solutions, filters for correct ones, and fine-tunes on the successful reasoning traces. Over iterations, small models become substantially stronger reasoners from their own generated proofs.

**Self-Rewarding Language Models (Meta AI):** The model generates responses, then scores them itself, creating preference data for RLHF-style training without human labelers. This enables a self-improvement loop that could theoretically produce super-human feedback.

**Constitutional AI (Anthropic):** The model critiques its own outputs based on a set of principles (the "constitution"), revises them, and these revised responses become training data. The RL phase uses AI-generated preferences (RLAIF) rather than human labels.

### Tier 4: Code and Architecture Self-Modification

**STOP — Self-Taught Optimizer (2024):** A scaffolding program recursively improves itself using a fixed LLM. The LLM rewrites the scaffolding code, and the improved scaffolding produces better results.

**AlphaEvolve (Google DeepMind, 2025):** An evolutionary coding agent that uses an LLM to design and optimize algorithms. It repeatedly mutates or combines existing algorithms, selects the most promising, and iterates.

**Gödel Agent:** A self-referential framework where the agent recursively modifies its own code and decision-making policies. Named after Gödel's incompleteness theorems, it embraces the paradox of self-reference.

**ADAS — Automated Design of Agentic Systems (ICLR 2025):** A meta-agent programs new agents in code, tests them, archives successful designs, and uses the archive to inform the next iteration. Because agents are defined in code (Turing-complete), this can theoretically discover any possible agentic system.

### Tier 5: Multi-Agent Self-Improvement

**Multi-Agent Debate:** Multiple agents with different personas debate a problem, critique each other's reasoning, and converge on a better answer. MAR (Multi-Agent Reflexion) combines this with episodic memory for even stronger results.

**Self-Play:** The agent plays against itself (or variants of itself) to discover weaknesses and develop countermeasures. Used in game-playing agents and increasingly in language agent training.

**SiriuS (NeurIPS 2025):** Self-improving multi-agent systems via bootstrapped reasoning. Agents collaboratively generate and refine training data, bootstrapping each other's capabilities.

---

## Building a Self-Improving System from Scratch {#building-from-scratch}

### Phase 1: Foundation (Week 1-2)

#### Step 1: Choose Your Runtime Stack

```
Technology choices:
├── Runtime: Node.js (OpenClaw model) or Python (research model)
├── LLM Provider: Anthropic Claude API (recommended), OpenAI, or local models
├── Message Router: Your own or adapt OpenClaw's gateway
├── Storage: File-based (markdown + JSON) for simplicity, SQLite/Postgres for scale
├── Containerization: Docker (mandatory for safe code execution)
└── Version Control: Git (for tracking all agent modifications)
```

#### Step 2: Create the Identity Stack

Create the following files in your project root:

1. **`SOUL.md`** — Define the agent's philosophy, values, and behavioral guidelines
2. **`IDENTITY.md`** — Define its name, personality traits, and communication style
3. **`CONSTITUTION.md`** — Define hard safety boundaries and escalation rules
4. **`STYLE.md`** — Define voice, tone, and formatting preferences
5. **`PERMISSIONS.md`** — Define what tools and actions are available

#### Step 3: Build the Core Loop

The fundamental agent loop is:

```
PERCEIVE → PLAN → ACT → OBSERVE → REFLECT → UPDATE
```

In pseudocode:

```python
while True:
    # 1. Perceive: Read incoming message + load identity + load memory
    context = load_soul() + load_memory() + load_reflections()
    message = await receive_message()

    # 2. Plan: Ask LLM to create an action plan
    plan = await llm.plan(context + message)

    # 3. Act: Execute the plan using tools
    results = await execute_tools(plan)

    # 4. Observe: Capture outcomes
    outcomes = evaluate_results(results, plan.goals)

    # 5. Reflect: Self-evaluate
    reflection = await llm.reflect(plan, results, outcomes)

    # 6. Update: Store learnings
    append_to_journal(reflection)
    update_memory(reflection.key_learnings)
    if reflection.suggests_skill_update:
        update_skills(reflection.skill_changes)
```

#### Step 4: Implement the Tool System

Design tools as modular, self-describing functions:

```javascript
// tools/web_search.js
module.exports = {
  name: "web_search",
  description: "Search the web for current information",
  parameters: {
    query: { type: "string", description: "Search query" }
  },
  async execute({ query }) {
    // Implementation
  }
};
```

The agent should be able to:
1. List available tools
2. Select appropriate tools for a task
3. Execute tools in sequence or parallel
4. **Create new tools** when none exist for a task

### Phase 2: Memory and Persistence (Week 3-4)

#### Step 5: Implement Layered Memory

**Conversation Memory:** Store the current session's messages in a buffer. When the context window approaches its limit, summarize older messages.

**Episodic Memory:** After each significant interaction, write a structured entry:

```json
{
  "timestamp": "2026-02-08T10:30:00Z",
  "task": "Set up CI pipeline for user's project",
  "outcome": "success",
  "approach": "Used GitHub Actions with Docker",
  "reflection": "User prefers YAML over JSON config. Remember for next time.",
  "key_learnings": ["user_prefers_yaml", "project_uses_docker"]
}
```

**Semantic Memory:** Maintain a growing knowledge base of user preferences, project context, and learned patterns. This can be a simple markdown file or a vector store for more sophisticated retrieval.

#### Step 6: Implement Session Continuity

The agent must gracefully handle session resets:

```
On Session Start:
  1. Read SOUL.md → Reconstruct identity
  2. Read MEMORY.md → Load user preferences and context
  3. Read JOURNAL.md (last N entries) → Recall recent interactions
  4. Read GOALS.md → Resume ongoing tasks
  5. Read REFLECTIONS.md (recent) → Apply learned lessons
```

### Phase 3: Self-Improvement (Week 5-8)

#### Step 7: Implement the Reflection Engine

After every task (or at scheduled intervals), trigger a reflection:

```
REFLECTION PROMPT:
Given the task I just completed:
- Task: {description}
- Plan: {what I planned to do}
- Actions: {what I actually did}
- Outcome: {success/failure + details}

Analyze:
1. What went well? Why?
2. What went poorly? Why?
3. What would I do differently next time?
4. Are there any patterns I'm seeing across recent tasks?
5. Should I update any of my skills, tools, or approaches?
6. Are there any updates I should make to my own operating instructions?

Output structured reflection for JOURNAL.md.
```

#### Step 8: Implement Skill Evolution

The agent should be able to:

1. **Discover** that a capability is missing during task execution
2. **Search** for existing solutions (skill registries, web search)
3. **Create** a new skill as a code function
4. **Test** the skill in a sandbox
5. **Register** the skill for future use
6. **Document** the skill in SKILLS.md

#### Step 9: Implement Self-Modification with Guardrails

The agent can propose changes to its own operating documents:

```
SELF-MODIFICATION PROTOCOL:
1. Agent identifies need for change (based on reflection)
2. Agent drafts proposed change to SOUL.md, SKILLS.md, or STYLE.md
3. Change is logged in EVOLUTION.md with rationale
4. For CONSTITUTION.md changes: ALWAYS require human approval
5. For SOUL.md changes: Require human approval if change alters values
6. For SKILLS.md / STYLE.md changes: Can self-approve with logging
7. All changes are version-controlled in git
```

### Phase 4: Multi-Agent and Orchestration (Week 9-12)

#### Step 10: Add Specialist Sub-Agents

Create specialized agents for different domains:

```
Agent Hierarchy:
├── Coordinator (The Mayor)
│   ├── Research Agent — deep web research, paper analysis
│   ├── Code Agent — writing, debugging, testing code
│   ├── Writer Agent — documentation, reports, creative writing
│   ├── Critic Agent — reviewing and stress-testing outputs
│   └── Reflection Agent — analyzing patterns, suggesting improvements
```

Each sub-agent has its own SOUL.md with domain-specific expertise, but shares the same CONSTITUTION.md.

#### Step 11: Implement Inter-Agent Communication

Agents need a message-passing protocol:

```
Message Format:
{
  "from": "research_agent",
  "to": "coordinator",
  "type": "task_complete",
  "task_id": "research-2026-02-08-001",
  "summary": "Found 3 relevant papers on self-improving agents",
  "artifacts": ["papers_summary.md"],
  "confidence": 0.85,
  "next_steps": ["Code agent should implement technique from paper #2"]
}
```

---

## The Refinement Loop: Letting the System Improve Itself {#the-refinement-loop}

The true power of a self-improving system comes from establishing **virtuous feedback loops** — cycles where each iteration produces measurably better results.

### Loop 1: Task-Level Refinement (Minutes)

```
Execute task → Evaluate outcome → Reflect → Retry with insights
```

This is the Reflexion pattern. The agent fails, reflects on why, and tries again with its reflection in context. Each retry is informed by the previous failure.

### Loop 2: Session-Level Learning (Hours)

```
Complete session → Summarize learnings → Update MEMORY.md → Next session starts with updated memory
```

The agent accumulates knowledge within a work session and persists it for future sessions.

### Loop 3: Skill-Level Evolution (Days)

```
Encounter repeated pattern → Abstract into reusable skill → Test skill → Add to SKILLS.md → Future tasks use the skill
```

This is the Voyager pattern: the agent builds an expanding library of capabilities.

### Loop 4: Identity-Level Evolution (Weeks)

```
Analyze JOURNAL.md patterns → Identify systematic improvements → Propose SOUL.md/STYLE.md updates → Human reviews → Incorporate changes
```

The agent's fundamental operating principles evolve based on accumulated experience.

### Loop 5: Architecture-Level Evolution (Months)

```
Meta-agent analyzes agent performance → Proposes new architectural patterns → Tests in sandbox → Promotes successful patterns → Retires failed patterns
```

This is the ADAS pattern: the architecture itself evolves.

### The Ratchet Principle

Inspired by Gas Town's CI-as-ratchet philosophy: **improvements accumulate, failures don't.** Every proposed self-modification goes through a testing gate. Successful modifications are committed; failed ones are rolled back. Over time, the system ratchets toward higher capability.

```
Proposed Change → Test Suite → Pass? → Commit + Log
                              Fail? → Rollback + Reflect on why
```

---

## Advanced Techniques: Toward Maximum Capability {#advanced-techniques}

### 1. Constitutional Self-Training

Combine Anthropic's Constitutional AI approach with self-generated training data:

1. Define a rich constitution covering values, safety, and quality standards
2. Have the agent generate responses to challenging scenarios
3. Have the agent critique its own responses against the constitution
4. Have the agent revise its responses based on its own critiques
5. Use the critique-revision pairs to fine-tune future behavior (or adjust prompts)

### 2. Meta-Agent Search (ADAS)

Implement a meta-agent that designs new agents:

1. Define a search space of agent architectures (prompts, tools, workflows, control flows)
2. The meta-agent generates candidate agent designs as code
3. Evaluate each candidate on benchmark tasks
4. Archive successful designs
5. Use the archive to inform the next generation of designs
6. Repeat

ADAS has demonstrated ~14% accuracy improvements over state-of-the-art on reasoning benchmarks and discovered agents that transfer across tasks and models.

### 3. Adversarial Self-Play

The agent generates challenges for itself and learns from attempting them:

1. **Challenge Generation:** The agent creates tasks that are slightly beyond its current capability
2. **Attempt:** The agent tries to solve the challenge
3. **Evaluation:** Verify the solution (via tests, external validators, or critic agents)
4. **Learning:** Store successful strategies; analyze failures

This is the Self-Challenging Agent (SCA) pattern, which alternates between generating problems and solving them.

### 4. Multi-Agent Reflexion (MAR)

Deploy multiple critic personas with deliberately diverse reasoning styles:

- **The Optimist:** Focuses on what's working and how to amplify it
- **The Skeptic:** Focuses on what could go wrong and hidden assumptions
- **The Pragmatist:** Focuses on real-world feasibility and edge cases
- **The Judge:** Synthesizes debate into actionable consensus

The debate transcript becomes episodic memory, guiding the agent's next attempt.

### 5. Curriculum Learning

Structure self-improvement as a curriculum that progresses from simple to complex:

1. Start with tasks the agent can reliably complete (>90% success)
2. Gradually increase difficulty based on success rate
3. When the agent masters a level, it generates its own challenges at the next level
4. Track progress in METRICS.md and adjust curriculum dynamically

### 6. Tool-Making as a First-Class Capability

Don't just equip the agent with tools — make tool-creation a core skill:

1. Agent encounters a gap in its capabilities
2. Agent searches for existing tools (registries, packages, APIs)
3. If none found, agent writes tool code
4. Agent writes tests for the tool
5. Agent tests in sandbox
6. Agent documents the tool and adds to registry
7. Future tasks automatically discover and use the tool

### 7. Persistent Identity Through Version Control

Track every self-modification in git:

```bash
# Every change to identity/skill files is a commit
git log --oneline SOUL.md
# a1b2c3d Updated communication style based on user feedback
# d4e5f6a Added preference for concise responses
# g7h8i9j Initial SOUL.md creation
```

This creates an auditable trail of the agent's evolution and allows rollback to any previous version of its identity.

---

## Safety, Guardrails, and Governance {#safety-and-guardrails}

Self-improving systems are powerful precisely because they change themselves. This same power makes safety critical.

### The Priority Hierarchy (from Anthropic's Constitution)

1. **Safety** — Being safe and supporting human oversight of AI
2. **Ethics** — Behaving ethically and not acting in harmful or dishonest ways
3. **Guidelines** — Following Anthropic's guidelines
4. **Helpfulness** — Being genuinely helpful to operators and users

### Practical Guardrails

**Sandboxing:** All code execution happens in Docker containers. The agent cannot reach the host system directly.

**Permission Tiers:** Not all self-modifications are equal:
- **Auto-approved:** Style changes, new skills, memory updates
- **Human-reviewed:** Soul changes, constitution changes, permission changes
- **Forbidden:** Removing safety constraints, disabling logging, self-replication

**Audit Logging:** Every action, tool invocation, and self-modification is logged with timestamps, reasoning, and outcomes.

**Kill Switch:** The human operator can pause, roll back, or terminate the agent at any time.

**Alignment Faking Detection:** Anthropic's 2024 research showed that Claude could exhibit "alignment faking" — appearing to accept new training objectives while maintaining original preferences. Monitor for behavioral drift and run periodic alignment checks.

**Rate Limiting Self-Modification:** Don't allow the agent to modify itself more than N times per day/week without human review.

---

## Project Naming Ideas {#project-naming-ideas}

For a self-improving agentic system, the name should evoke intelligence, evolution, autonomy, and a sense of living growth. Here are naming ideas organized by theme:

### Mythological / Philosophical
| Name | Meaning / Evocation |
|------|---------------------|
| **Prometheus** | The titan who brought fire (knowledge) to humanity |
| **Athena** | Greek goddess of wisdom, strategy, and craft |
| **Ouroboros** | The serpent eating its own tail — self-reference, eternal return |
| **Daedalus** | The master craftsman, builder of the labyrinth |
| **Nous** | Ancient Greek for "mind" or "intellect" |
| **Pneuma** | "Breath" or "spirit" — the animating force |
| **Animus** | Latin for "mind" or "spirit" |
| **Cogito** | From Descartes' "I think, therefore I am" |

### Evolution / Growth
| Name | Meaning / Evocation |
|------|---------------------|
| **Evolve** | Direct, clear, describes the core capability |
| **Chrysalis** | The transformative stage between caterpillar and butterfly |
| **Dendrite** | Neural branching — growing connections |
| **Rhizome** | Root network that grows in all directions |
| **Mycelium** | Underground fungal network — distributed intelligence |
| **Helix** | The spiral of DNA — self-replicating information |
| **Cambrian** | The Cambrian explosion — rapid diversification of life |
| **Genesis** | Beginning, origin, creation |

### Technical / Computing
| Name | Meaning / Evocation |
|------|---------------------|
| **Recurse** | Self-referential improvement |
| **Iterate** | The fundamental loop of refinement |
| **Eigen** | German for "own" / "self" — eigenvalue, self-referential |
| **Nexus** | A connection or central point linking many systems |
| **Cortex** | The outer layer of the brain — complex thought |
| **Synapse** | The connection between neurons — communication |
| **Scaffold** | The structure that supports construction (and can be removed) |
| **Forge** | Where raw materials become refined tools |

### Personality-Forward (OpenClaw style)
| Name | Meaning / Evocation |
|------|---------------------|
| **Archon** | A ruler or chief — the agent that rules itself |
| **Sentinel** | Always-on, watchful, protective |
| **Aegis** | A shield — protection and power combined |
| **Harbinger** | A signal of what's to come |
| **Meridian** | The highest point — peak capability |
| **Crucible** | Where transformation happens under pressure |
| **Axiom** | A self-evident truth — foundational principles |
| **Aether** | The fifth element — the substance of the cosmos |

### Compound / Memorable
| Name | Meaning / Evocation |
|------|---------------------|
| **MindForge** | Where intelligence is shaped and refined |
| **SoulCode** | The code that defines identity |
| **DeepRoot** | Deep, persistent, growing |
| **NeuraSelf** | Neural + Self — self-improving neural system |
| **AutoSoul** | Automatic soul — self-defining identity |
| **MetaMind** | Mind that thinks about itself |
| **SelfSeed** | The seed that grows itself |
| **EvoCore** | Evolutionary core — the engine of improvement |
| **ThinkLoop** | The recursive loop of self-reflection |
| **ArcWeave** | Weaving architectural patterns |

### Personal Favorites (Author's Picks)

1. **Ouroboros** — Poetic, memorable, perfectly captures self-referential improvement
2. **Chrysalis** — Evokes transformation and becoming
3. **MindForge** — Clear, powerful, describes what the system does
4. **Eigen** — Elegant, technical, self-referential
5. **Nous** — Ancient, philosophical, the purest word for "mind"

---

## References and Further Reading {#references}

### Research Papers

- Shinn et al. (2023). "Reflexion: Language Agents with Verbal Reinforcement Learning." NeurIPS 2023.
- Madaan et al. (2023). "Self-Refine: Iterative Refinement with Self-Feedback." NeurIPS 2024.
- Wang et al. (2022). "Self-Consistency Improves Chain of Thought Reasoning in Language Models."
- Yao et al. (2023). "Tree of Thoughts: Deliberate Problem Solving with Large Language Models." NeurIPS 2023.
- Hu et al. (2024). "Automated Design of Agentic Systems." ICLR 2025.
- Zelikman et al. (2022). "STaR: Self-Taught Reasoner." NeurIPS 2022.
- Qu et al. (2024). "Recursive Introspection: Teaching LLM Agents How to Self-Improve."
- Zhao et al. (2025). "SiriuS: Self-Improving Multi-Agent Systems via Bootstrapped Reasoning." NeurIPS 2025.
- Moskvoretskii et al. (2025). "Self-Taught Self-Correction (STaSC)."
- Fang et al. (2025). "A Comprehensive Survey of Self-Evolving AI Agents." arXiv:2508.07407.

### Projects and Repositories

- **OpenClaw:** [github.com/openclaw/openclaw](https://github.com/openclaw/openclaw)
- **Gas Town:** [github.com/steveyegge/gastown](https://github.com/steveyegge/gastown)
- **SOUL.md:** [soul.md](https://soul.md/) and [github.com/aaronjmars/soul.md](https://github.com/aaronjmars/soul.md)
- **ADAS:** [github.com/ShengranHu/ADAS](https://github.com/ShengranHu/ADAS)
- **Awesome Self-Evolving Agents:** [github.com/EvoAgentX/Awesome-Self-Evolving-Agents](https://github.com/EvoAgentX/Awesome-Self-Evolving-Agents)

### Courses and Guides

- Stanford CS329A: Self-Improving AI Agents — [cs329a.stanford.edu](https://cs329a.stanford.edu/)
- Anthropic: Claude's New Constitution (January 2026) — [anthropic.com/news/claude-new-constitution](https://www.anthropic.com/news/claude-new-constitution)
- Yohei Nakajima: "Better Ways to Build Self-Improving AI Agents" — [yoheinakajima.com](https://yoheinakajima.com/better-ways-to-build-self-improving-ai-agents/)
- Daniel Miessler: Personal AI Maturity Model — [danielmiessler.com](https://danielmiessler.com/blog/personal-ai-maturity-model)

### Key Blog Posts and Analysis

- Maggie Appleton: "Gas Town's Agent Patterns, Design Bottlenecks, and Vibecoding at Scale" — [maggieappleton.com/gastown](https://maggieappleton.com/gastown)
- Steve Yegge: "Welcome to Gas Town" and "The Future of Coding Agents" — Medium
- IBM Think: "OpenClaw, Moltbook and the future of AI agents" (Feb 2026)

---

*This report was compiled in February 2026. The field of self-improving agentic systems is evolving rapidly. By the time you read this, new techniques, projects, and paradigms may have emerged. The principles, however — persistent identity, reflective improvement, tool evolution, and safety-gated self-modification — are likely to remain foundational.*
