# Recursa Architecture

The deep patterns that enable self-improving systems.

---

## Table of Contents

1. [The Seven Layers](#the-seven-layers)
2. [The Document Stack](#the-document-stack)
3. [The Five Pillars](#the-five-pillars)
4. [The Intelligence Stack](#the-intelligence-stack)
5. [The Learning Ladder](#the-learning-ladder)
6. [The Refinement Loops](#the-refinement-loops)
7. [The Self-Modification Gate](#the-self-modification-gate)
8. [The Evolution Cycles](#the-evolution-cycles)
9. [Critical Success Factors](#critical-success-factors)
10. [Anti-Patterns](#anti-patterns)
11. [Domain Adaptation](#domain-adaptation)

---

## The Seven Layers

A fully-realized self-improving system has seven architectural layers:

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                     THE SEVEN LAYERS OF A SELF-IMPROVING SYSTEM             │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│   Layer 7: SAFETY LAYER (The Guardrails)                                    │
│   │   Sandboxing, permissions, audit logging, rollback, constitutional      │
│   │   constraints that prevent harmful actions                              │
│   │                                                                          │
│   Layer 6: ORCHESTRATION LAYER (The Nervous System)                         │
│   │   Routing, scheduling, task assignment, supervision, inter-component    │
│   │   communication for complex or multi-agent systems                      │
│   │                                                                          │
│   Layer 5: REFLECTION ENGINE (The Conscience)                               │
│   │   Self-evaluation, failure analysis, feedback generation, behavioral    │
│   │   updating based on outcomes                                            │
│   │                                                                          │
│   Layer 4: TOOL SYSTEM (The Hands)                                          │
│   │   Extensible capabilities for interacting with the world: file ops,     │
│   │   APIs, execution environments. Critically: can CREATE new tools        │
│   │                                                                          │
│   Layer 3: MEMORY SYSTEM (The Mind)                                         │
│   │   Short-term (session), working (scratchpad), long-term (persistent),   │
│   │   episodic (experiences), semantic (knowledge)                          │
│   │                                                                          │
│   Layer 2: IDENTITY LAYER (The Soul)                                        │
│   │   Values, personality, boundaries, behavioral guidelines encoded in     │
│   │   configuration files (SOUL.md, CONSTITUTION.md, STYLE.md)              │
│   │                                                                          │
│   Layer 1: FOUNDATION (The Brain)                                           │
│       The core reasoning capability—LLM, human, or hybrid. Provides         │
│       planning, language understanding, generation, and decision-making     │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

### Layer Interactions

Each layer enables the one above:
- **Foundation** provides reasoning for all other layers
- **Identity** shapes how reasoning is applied
- **Memory** gives context to reasoning
- **Tools** execute decisions
- **Reflection** evaluates outcomes
- **Orchestration** coordinates complexity
- **Safety** constrains all actions

---

## The Document Stack

The system's intelligence is encoded in structured documents. This is the **brain on disk**.

### Core Identity Documents

| File | Purpose | Who Reads It |
|------|---------|--------------|
| `SOUL.md` | Behavioral philosophy, core values, decision principles | System (every session) |
| `CONSTITUTION.md` | Inviolable rules, safety boundaries, priority hierarchy | System (as hard constraints) |
| `IDENTITY.md` | Name, persona, avatar, presentation style | System + users |
| `STYLE.md` | Voice, tone, formatting, communication preferences | System |

### Operational Documents

| File | Purpose | Who Reads It |
|------|---------|--------------|
| `LOOP.md` | Iteration process, workflow steps | System |
| `SKILLS.md` | Available capabilities and when to use them | System |
| `MEMORY.md` | How memory works, knowledge architecture | System |
| `GOALS.md` | Current objectives, priorities, success criteria | System |

### Learning Documents

| File | Purpose | Who Reads It |
|------|---------|--------------|
| `LEARNING.md` | Accumulated discoveries, patterns, anti-patterns | System |
| `JOURNAL.md` | Episodic log of actions, outcomes, reflections | System + reflection engine |
| `METRICS.md` | Performance data, success rates, trend analysis | System + evaluation engine |
| `EXPERIMENTS.md` | Hypotheses being tested, A/B approaches, results | System |

### Self-Improvement Documents

| File | Purpose | Who Reads It |
|------|---------|--------------|
| `EVOLUTION.md` | Changelog of self-modifications with rationale | System + human operator |
| `REFLECTIONS.md` | Post-task evaluations, lessons learned, failure analysis | System + refinement loop |

### Governance Documents

| File | Purpose | Who Reads It |
|------|---------|--------------|
| `PERMISSIONS.md` | What the system can/cannot do, access rules | System + safety layer |
| `AUDIT.md` | Log of all actions with timestamps and reasoning | Human operator |
| `ESCALATION.md` | When/how to escalate to human, uncertainty thresholds | System |
| `GUARDRAILS.md` | Safety policies, sandbox rules, rollback procedures | System + safety layer |

### Document Cascade

Documents resolve through a fallback chain: **Specific → General → Default**

```
Project-specific SOUL.md
        ↓ (if not found)
Workspace SOUL.md
        ↓ (if not found)
Global SOUL.md
        ↓ (if not found)
System defaults
```

The most specific definition wins. This enables context-appropriate behavior.

---

## The Five Pillars

Every self-improving system rests on five pillars. Remove any one, and the system degrades.

### Pillar 1: Structured Memory

**What it is**: A system for preserving knowledge in a way that enables retrieval and connection.

**Why it matters**: Without memory, every iteration starts from zero. With memory, iteration 100 benefits from iterations 1-99.

**Key components**:
- Knowledge types (facts, procedures, heuristics, anti-patterns)
- Knowledge levels (hypothesis → observation → pattern → principle)
- Connection mechanisms (linking related knowledge)
- Decay management (knowing what's still valid)

```
┌─────────────────────────────────────────────────────────────────┐
│                    STRUCTURED MEMORY                            │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│   ┌─────────────┐    ┌─────────────┐    ┌─────────────┐         │
│   │   CAPTURE   │ ─→ │   CONNECT   │ ─→ │   RETRIEVE  │         │
│   │   (learn)   │    │   (link)    │    │   (use)     │         │
│   └─────────────┘    └─────────────┘    └─────────────┘         │
│         │                  │                  │                 │
│         ▼                  ▼                  ▼                 │
│   New knowledge      Related to       Informs next              │
│   from iteration     existing         decision                  │
│                      knowledge                                  │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

---

### Pillar 2: Quantitative Metrics

**What it is**: Systematic tracking of measurable outcomes.

**Why it matters**: Intuition is biased. Numbers reveal patterns that feelings miss. "I think I'm improving" vs "Success rate increased from 15% to 25%."

**Key components**:
- Outcome metrics (what was produced)
- Process metrics (how it was produced)
- Trend analysis (change over time)
- Comparative analysis (across categories/techniques)

```
┌─────────────────────────────────────────────────────────────────┐
│                    QUANTITATIVE METRICS                         │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│   Track                Analyze              Act                 │
│     │                    │                   │                  │
│     ▼                    ▼                   ▼                  │
│   ┌──────┐          ┌──────┐           ┌──────┐                 │
│   │ Data │    ─→    │Trends│    ─→     │Change│                 │
│   │ Points│         │Patterns│         │Behavior│               │
│   └──────┘          └──────┘           └──────┘                 │
│                                                                 │
│   "What happened?"  "What's the       "What should              │
│                      pattern?"         I do now?"               │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

---

### Pillar 3: Honest Evaluation

**What it is**: Rigorous, unbiased assessment of outputs and processes.

**Why it matters**: Improvement requires knowing current state accurately. Self-deception is the enemy of growth.

**Key components**:
- Quality criteria (what "good" means)
- Rating systems (consistent measurement)
- Comparative judgment (against prior work)
- Root cause analysis (understanding failures)

**The Evaluation Triad**:

| Evaluation Type | Question | Focus |
|-----------------|----------|-------|
| **Output** | How good are results? | Quality of what's produced |
| **Process** | How well does the system work? | Efficiency, learning rate |
| **Meta** | Is improvement happening? | The improvement process itself |

---

### Pillar 4: Systematic Improvement

**What it is**: Converting learnings into changes to the system.

**Why it matters**: Learning without action is just data collection. The system must change based on what it learns.

**Key components**:
- Improvement mechanisms (how changes happen)
- Validation (did the change work?)
- Rollback (reversing failed changes)
- Documentation (recording what changed and why)

```
┌─────────────────────────────────────────────────────────────────┐
│                    IMPROVEMENT CYCLE                            │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│   Observe      Diagnose      Prescribe      Implement           │
│     │            │              │              │                │
│     ▼            ▼              ▼              ▼                │
│   ┌────┐      ┌────┐        ┌────┐        ┌────┐               │
│   │See │  ─→  │Why │   ─→   │What│   ─→   │Do  │               │
│   │    │      │    │        │    │        │    │               │
│   └────┘      └────┘        └────┘        └────┘               │
│     │                                        │                  │
│     └────────────────────────────────────────┘                  │
│                    Feedback loop                                │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

---

### Pillar 5: Meta-Evolution

**What it is**: The capability to improve the improvement process itself.

**Why it matters**: This is what separates truly intelligent systems from merely iterative ones. The system gets better at getting better.

**Key components**:
- Meta-observation (watching how the system learns)
- Meta-evaluation (judging learning effectiveness)
- Meta-improvement (changing the learning process)
- Recursive application (apply to any level)

```
┌─────────────────────────────────────────────────────────────────┐
│                       META-EVOLUTION                            │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│   Level 3: Improving how we improve improvements                │
│                           │                                     │
│                           ▼                                     │
│   Level 2: Improving how we improve ◀────────────────┐          │
│                           │                          │          │
│                           ▼                          │          │
│   Level 1: Improving the core process                │          │
│                           │                          │          │
│                           ▼                          │          │
│   Level 0: The core process (doing) ─────────────────┘          │
│                                                                 │
│   Each level enables better operation of the level below.       │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

---

## The Intelligence Stack

A self-improving system operates on multiple cognitive levels simultaneously.

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                         THE INTELLIGENCE STACK                              │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│   ┌─────────────────────────────────────────────────────────────────────┐   │
│   │  LEVEL 4: META-COGNITION                                            │   │
│   │  "How do I think? How can I think better?"                          │   │
│   │  • Improving the improvement process                                │   │
│   │  • Questioning assumptions about learning                           │   │
│   │  • Evolving the system architecture                                 │   │
│   └─────────────────────────────────────────────────────────────────────┘   │
│                                  │                                          │
│                                  ▼                                          │
│   ┌─────────────────────────────────────────────────────────────────────┐   │
│   │  LEVEL 3: STRATEGIC INTELLIGENCE                                    │   │
│   │  "What should I focus on? What's highest leverage?"                 │   │
│   │  • Resource allocation                                              │   │
│   │  • Priority setting                                                 │   │
│   │  • Trade-off navigation                                             │   │
│   └─────────────────────────────────────────────────────────────────────┘   │
│                                  │                                          │
│                                  ▼                                          │
│   ┌─────────────────────────────────────────────────────────────────────┐   │
│   │  LEVEL 2: EVALUATIVE INTELLIGENCE                                   │   │
│   │  "How well am I doing? What's working?"                             │   │
│   │  • Self-assessment                                                  │   │
│   │  • Pattern recognition                                              │   │
│   │  • Quality judgment                                                 │   │
│   └─────────────────────────────────────────────────────────────────────┘   │
│                                  │                                          │
│                                  ▼                                          │
│   ┌─────────────────────────────────────────────────────────────────────┐   │
│   │  LEVEL 1: OPERATIONAL INTELLIGENCE                                  │   │
│   │  "What do I do? How do I execute?"                                  │   │
│   │  • Task execution                                                   │   │
│   │  • Domain expertise                                                 │   │
│   │  • Output production                                                │   │
│   └─────────────────────────────────────────────────────────────────────┘   │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

**Key insight**: Most systems only have Level 1. Self-improving systems add Levels 2-4.

---

## The Learning Ladder

Knowledge evolves through predictable stages.

```
┌─────────────────────────────────────────────────────────────────┐
│                      THE LEARNING LADDER                        │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│   INTUITION     "I know without thinking"                       │
│       ▲         Internalized, automatic                         │
│       │         10+ successful applications                     │
│       │                                                         │
│   PRINCIPLE     "I understand why"                              │
│       ▲         Causal mechanism understood                     │
│       │         Transferable to new contexts                    │
│       │                                                         │
│   PATTERN       "I've seen this work repeatedly"                │
│       ▲         3+ confirmations                                │
│       │         Reliable heuristic                              │
│       │                                                         │
│   OBSERVATION   "This worked once"                              │
│       ▲         Single data point                               │
│       │         Needs validation                                │
│       │                                                         │
│   HYPOTHESIS    "I think this might work"                       │
│                 Untested                                        │
│                 Based on reasoning                              │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

### Promotion Criteria

| From | To | Requires |
|------|-----|----------|
| Hypothesis | Observation | 1 successful experiment |
| Observation | Pattern | 3+ confirmations in varied contexts |
| Pattern | Principle | Understanding of causal mechanism |
| Principle | Intuition | 10+ automatic successful applications |

### Demotion Triggers

Knowledge can move down the ladder:

- **Contradicting evidence**: Pattern fails in new context
- **Better explanation**: Principle was wrong about mechanism
- **Changed conditions**: What worked no longer works

---

## The Refinement Loops

Self-improvement requires multiple feedback loops operating at different timescales. The power comes from **virtuous cycles** where each iteration produces measurably better results.

### Loop 1: Task-Level Refinement (Minutes)

```
Execute task → Evaluate outcome → Reflect → Retry with insights
```

The Reflexion pattern: fail, reflect on why, retry with reflection in context.

### Loop 2: Session-Level Learning (Hours)

```
Complete session → Summarize learnings → Update MEMORY → Next session benefits
```

Knowledge accumulates within a session and persists for future sessions.

### Loop 3: Skill-Level Evolution (Days)

```
Encounter pattern → Abstract into skill → Test → Register → Future uses skill
```

The system builds an expanding library of capabilities.

### Loop 4: Identity-Level Evolution (Weeks)

```
Analyze patterns → Identify improvements → Propose updates → Human reviews → Incorporate
```

Fundamental operating principles evolve based on accumulated experience.

### Loop 5: Architecture-Level Evolution (Months)

```
Meta-analysis → Propose new patterns → Test in sandbox → Promote successful → Retire failed
```

The architecture itself evolves—the ADAS pattern.

### The Ratchet Principle

**Improvements accumulate, failures don't.**

```
Proposed Change → Test Suite → Pass? → Commit + Log
                              Fail? → Rollback + Reflect
```

Every proposed modification goes through a testing gate. Successful modifications are committed; failed ones are rolled back. Over time, the system ratchets toward higher capability.

---

## The Self-Modification Gate

Not all self-modifications are equal. Changes flow through a gate system:

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                     THE SELF-MODIFICATION GATE                              │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│   System identifies need for change                                         │
│                    │                                                        │
│                    ▼                                                        │
│            Which document/area?                                             │
│                    │                                                        │
│         ┌─────────┴─────────┐                                               │
│         ▼                   ▼                                               │
│    PROTECTED            AUTONOMOUS                                          │
│   (constitution,       (skills, memory,                                     │
│    permissions,         style, learning)                                    │
│    core values)              │                                              │
│         │                    ▼                                              │
│         ▼               Draft change                                        │
│    Draft change              │                                              │
│         │                    ▼                                              │
│         ▼               Log to EVOLUTION.md                                 │
│    Log to EVOLUTION.md       │                                              │
│         │                    ▼                                              │
│         ▼               Run safety tests                                    │
│    Run safety tests          │                                              │
│         │                    ▼                                              │
│         ▼               Tests pass?                                         │
│    Queue for human           │                                              │
│    review                    ▼                                              │
│         │              Auto-commit                                          │
│         ▼                    │                                              │
│    Human approves?           ▼                                              │
│         │              ✅ Applied                                            │
│         ▼                                                                   │
│    ✅ Applied                                                                │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

### Modification Permission Matrix

| Document | Read | Write | Delete | Human Approval |
|----------|:----:|:-----:|:------:|:--------------:|
| CONSTITUTION.md | ✅ | ❌ | ❌ | Always required |
| SOUL.md (values) | ✅ | ⚠️ | ❌ | For value changes |
| PERMISSIONS.md | ✅ | ❌ | ❌ | Always required |
| SOUL.md (style) | ✅ | ✅ | ❌ | No |
| IDENTITY.md | ✅ | ✅ | ❌ | No |
| STYLE.md | ✅ | ✅ | ❌ | No |
| LEARNING.md | ✅ | ✅ | ⚠️ | For deletions |
| MEMORY/* | ✅ | ✅ | ⚠️ | Summaries only |
| Skills (learned) | ✅ | ✅ | ✅ | No |
| Skills (built-in) | ✅ | ⚠️ | ❌ | For changes |
| Audit logs | ✅ | Append | ❌ | Never deletable |

Legend: ✅ = Yes | ❌ = No | ⚠️ = Conditional

---

## The Evolution Cycles

### Cycle Frequencies

| Cycle | Frequency | Activities |
|-------|-----------|------------|
| **Micro** | Every iteration | Capture learnings, update metrics |
| **Meso** | Every 5 iterations | Retrospective, pattern promotion, process tweaks |
| **Macro** | Every 20 iterations | Strategic review, knowledge consolidation, architecture assessment |
| **Meta** | Continuous | Monitor learning effectiveness, evolve the learning system |

### Cycle Nesting

```
┌─────────────────────────────────────────────────────────────────────────────┐
│  META CYCLE (continuous) ──────────────────────────────────────────────────│
│  ┌───────────────────────────────────────────────────────────────────────┐ │
│  │  MACRO CYCLE (every 20 iterations) ─────────────────────────────────  │ │
│  │  ┌─────────────────────────────────────────────────────────────────┐  │ │
│  │  │  MESO CYCLE (every 5 iterations) ─────────────────────────────  │  │ │
│  │  │  ┌───────────────────────────────────────────────────────────┐  │  │ │
│  │  │  │  MICRO CYCLE (every iteration)                            │  │  │ │
│  │  │  │  [ iter 1 ] [ iter 2 ] [ iter 3 ] [ iter 4 ] [ iter 5 ]   │  │  │ │
│  │  │  └───────────────────────────────────────────────────────────┘  │  │ │
│  │  │                          ↓ retrospective                        │  │ │
│  │  └─────────────────────────────────────────────────────────────────┘  │ │
│  │                                                                       │ │
│  │  (4 meso cycles = 20 iterations) ↓ strategic review                  │ │
│  └───────────────────────────────────────────────────────────────────────┘ │
│                                                                             │
│  Meta-observation happens throughout, improving all levels                  │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## Critical Success Factors

### 1. Capture Discipline

The system must reliably capture learnings. Missing captures means lost intelligence.

**Signs of good capture**:
- Every iteration produces documented learnings
- Failures are analyzed, not just noted
- Successes are understood, not just celebrated

**Signs of poor capture**:
- "I learned something but didn't write it down"
- Repeated discoveries of the same thing
- Knowledge exists only in informal memory

### 2. Honest Assessment

Self-deception is the death of self-improvement.

**Signs of honest assessment**:
- Failures acknowledged and analyzed
- Metrics tracked even when unflattering
- Ratings consistent and defensible

**Signs of dishonest assessment**:
- Inflated ratings to feel good
- Avoided metrics that might show problems
- Rationalization of poor results

### 3. Pattern Recognition

The system must see patterns across iterations.

**Signs of good pattern recognition**:
- Insights connect across different contexts
- Heuristics emerge from observations
- Predictions improve over time

**Signs of poor pattern recognition**:
- Each iteration feels isolated
- Same mistakes repeated
- No sense of what to expect

### 4. Actionable Improvement

Learning must translate to behavior change.

**Signs of actionable improvement**:
- Process changes based on retrospectives
- Decisions informed by metrics
- Knowledge actively guides choices

**Signs of non-actionable improvement**:
- Documentation exists but isn't used
- Retrospectives don't lead to changes
- Same processes despite learnings

### 5. Meta-Awareness

The system must monitor its own learning.

**Signs of good meta-awareness**:
- Learning rate tracked
- Improvement process itself evolves
- Questions about "how do we learn?"

**Signs of poor meta-awareness**:
- No sense of whether learning is effective
- Learning process static
- Only focused on domain, not process

---

## Anti-Patterns

Behaviors that prevent self-improvement:

### 1. Capture Neglect
"I'll remember this" → No you won't

### 2. Metric Avoidance
"I don't need numbers, I can feel it" → Bias wins

### 3. Rating Inflation
"Everything is 4/5" → No signal

### 4. Retrospective Theater
"We do retrospectives" → But nothing changes

### 5. Knowledge Silos
"I know this" → But it's not accessible

### 6. Local Optimization
"I'm perfecting this one thing" → Missing the forest

### 7. Process Ossification
"This is how we do it" → Never evolving

### 8. Meta-Blindness
"Just do the work" → Never improving how we improve

---

## Domain Adaptation

Recursa applies to any domain with iterative output. Here's how to adapt:

### Step 1: Identify the Iteration Unit

What is one cycle of work?
- Software: One feature/bug fix
- Writing: One draft/edit pass
- Research: One experiment
- Sales: One pitch/deal
- Learning: One study session

### Step 2: Define Quality

What makes output "good" in this domain?
- Define rating criteria
- Establish measurement methods
- Set quality thresholds

### Step 3: Map Knowledge Types

What can be learned?
- Domain facts (what works here)
- Procedures (how to do things)
- Heuristics (rules of thumb)
- Anti-patterns (what to avoid)

### Step 4: Design Feedback Loops

How will learning flow back?
- Micro: Every iteration capture
- Meso: Periodic retrospective
- Macro: Strategic review
- Meta: Learning improvement

### Step 5: Establish Metrics

What can be measured?
- Output quality
- Process efficiency
- Learning velocity
- Improvement rate

### Step 6: Enable Meta-Evolution

How will the system improve itself?
- Meta-observation mechanisms
- Process change protocols
- Architecture evolution triggers

---

## The Ultimate Test

A Recursa system is working when:

1. **Iteration 100 is measurably better than iteration 1**
2. **Knowledge compounds rather than repeats**
3. **The system predicts what will work**
4. **Failures make the system stronger**
5. **The improvement process itself improves**

The goal: **A system that gets better forever.**
