# Bootstrapping a Recursa System

A step-by-step guide to instantiate a self-improving system in any domain.

---

## Table of Contents

1. [Prerequisites](#prerequisites)
2. [Phase 1: Domain Definition](#phase-1-domain-definition)
3. [Phase 2: Documentation Setup](#phase-2-documentation-setup)
4. [Phase 3: Process Definition](#phase-3-process-definition)
5. [Phase 4: First Iteration](#phase-4-first-iteration)
6. [Phase 5: Establish Rhythms](#phase-5-establish-rhythms)
7. [Phase 6: Verify & Calibrate](#phase-6-verify--calibrate)
8. [Checklist](#checklist)

---

## Prerequisites

Before starting, confirm:

- [ ] **Iterative domain**: Your work involves repeated cycles of output
- [ ] **Measurable outcomes**: You can assess quality of outputs
- [ ] **Ability to change**: You can modify your process based on learnings
- [ ] **Commitment**: You'll maintain the system even when inconvenient

---

## Phase 1: Domain Definition

### Step 1.1: Define the Iteration Unit

What constitutes one cycle of work?

```markdown
## My Iteration Unit

**Name**: [e.g., "feature sprint", "writing session", "experiment", "deal cycle"]

**Duration**: [typical time to complete one iteration]

**Inputs**: [what goes into an iteration]

**Outputs**: [what comes out of an iteration]

**Success criteria**: [when is an iteration successful]
```

**Examples**:

| Domain | Iteration Unit | Duration | Output |
|--------|----------------|----------|--------|
| Software | Feature/bug fix | 1-5 days | Working code |
| Writing | Draft/edit pass | 2-4 hours | Revised text |
| Research | Experiment | 1 day - 2 weeks | Results + analysis |
| Sales | Deal cycle | 1-8 weeks | Closed/lost deal |
| Learning | Study session | 1-2 hours | Mastered concepts |
| Art | Piece creation | 1-8 hours | Finished artwork |

### Step 1.2: Define Quality Criteria

How do you know if an output is good?

```markdown
## Quality Criteria

### Rating Scale
| Rating | Name | Meaning |
|--------|------|---------|
| 5/5 | [Excellent] | [Definition] |
| 4/5 | [Strong] | [Definition] |
| 3/5 | [Adequate] | [Definition] |
| 2/5 | [Weak] | [Definition] |
| 1/5 | [Failed] | [Definition] |

### Key Dimensions
1. **[Dimension 1]**: [What it measures]
2. **[Dimension 2]**: [What it measures]
3. **[Dimension 3]**: [What it measures]

### Non-Negotiables
- [Must-have quality 1]
- [Must-have quality 2]
```

### Step 1.3: Identify Knowledge Types

What kinds of things can you learn in this domain?

```markdown
## Knowledge Types

### Factual
[What objective truths exist in this domain?]
- Example: "X technology performs Y under Z conditions"

### Procedural
[What processes and methods work?]
- Example: "The best way to do A is B then C"

### Heuristic
[What rules of thumb emerge?]
- Example: "When you see P, usually do Q"

### Anti-Pattern
[What should be avoided?]
- Example: "Never do R because S happens"
```

### Step 1.4: Define Success Metrics

What numbers will you track?

```markdown
## Core Metrics

### Output Metrics
- [Metric 1]: [What it measures] [Target]
- [Metric 2]: [What it measures] [Target]

### Process Metrics
- [Metric 3]: [What it measures] [Target]
- [Metric 4]: [What it measures] [Target]

### Learning Metrics
- [Metric 5]: [What it measures] [Target]
- [Metric 6]: [What it measures] [Target]
```

---

## Phase 2: Documentation Setup

### Step 2.1: Create Directory Structure

```bash
mkdir -p your-project/docs
```

### Step 2.2: Instantiate Templates

Copy and customize templates from `templates/`:

| Template | Your File | Purpose |
|----------|-----------|---------|
| `MEMORY.template.md` | `docs/MEMORY.md` | How memory works |
| `LOOP.template.md` | `docs/LOOP.md` | Iteration process |
| `LEARNING.template.md` | `docs/LEARNING.md` | Accumulated knowledge |
| `METRICS.template.md` | `docs/METRICS.md` | Tracking framework |
| `EVOLUTION.template.md` | `docs/EVOLUTION.md` | Self-improvement |

### Step 2.3: Create Domain-Specific Docs

Based on your domain, add:

```markdown
docs/
├── MEMORY.md          # Memory system (from template)
├── LOOP.md            # Iteration process (from template)
├── LEARNING.md        # Knowledge log (from template)
├── METRICS.md         # Tracking (from template)
├── EVOLUTION.md       # Self-improvement (from template)
├── REFERENCE.md       # Domain encyclopedia (custom)
├── ISSUES.md          # Problems & fixes (custom)
└── OUTPUTS.md         # Quality-rated results (custom)
```

### Step 2.4: Initial Content

Each file should start with minimal content:

**LEARNING.md**:
```markdown
# Learning Log

Knowledge accumulated through iteration.

---

## Key Discoveries

(To be filled as learnings emerge)

---

## Anti-Patterns

(To be filled as failures teach)
```

**OUTPUTS.md**:
```markdown
# Quality Outputs

Rated results from iterations.

---

## Top Tier (5/5)

(None yet)

---

## Strong (4/5)

(None yet)
```

---

## Phase 3: Process Definition

### Step 3.1: Define the Core Loop

Customize `LOOP.md` with your iteration steps:

```markdown
# Iteration Loop

## Steps

### 1. Prepare
- Read LEARNING.md for relevant knowledge
- Check METRICS.md for patterns
- Review recent OUTPUTS.md for context

### 2. Execute
- [Your domain-specific actions]
- Capture observations as you go
- Note surprises, difficulties, successes

### 3. Evaluate
- Rate output using quality criteria
- Log metrics
- Compare to prior work

### 4. Capture
- Add discoveries to LEARNING.md
- Rate output in OUTPUTS.md
- Log issues in ISSUES.md

### 5. Improve
- Update process if needed
- Add to unexplored backlog
- Prepare for next iteration
```

### Step 3.2: Define Review Cycles

Set up retrospective rhythms:

```markdown
## Review Cycles

### After Every Iteration (Micro)
- Log metrics
- Capture learnings
- Rate outputs

### Every [N] Iterations (Meso)
- Pattern analysis
- Process improvement
- Knowledge promotion

### Every [M] Iterations (Macro)
- Strategic review
- Knowledge consolidation
- Architecture assessment
```

### Step 3.3: Define Improvement Triggers

What triggers process changes?

```markdown
## Improvement Triggers

### Automatic
- Success rate drops below [X]%: investigate
- Same mistake repeated 3x: create anti-pattern
- Process step always skipped: remove or enforce

### Review-Based
- Pattern confirmed 3x: promote to principle
- Technique unused 5+ iterations: explore or remove
- Metric plateau for 10 iterations: try something new
```

---

## Phase 4: First Iteration

### Step 4.1: Execute First Iteration

Do one complete cycle:

1. Prepare (read docs, even though sparse)
2. Execute (do the work)
3. Evaluate (rate honestly)
4. Capture (document everything)
5. Improve (note what could be better)

### Step 4.2: First Capture

After first iteration, document:

```markdown
## Iteration 1 Capture

### What Happened
- [Brief summary of the iteration]

### What Worked
- [Aspects that went well]

### What Didn't Work
- [Aspects that were difficult]

### Discoveries
- [New knowledge gained]

### Questions Raised
- [What do I want to explore next?]

### Metrics
- [Output rating: X/5]
- [Time spent: X]
- [Other relevant metrics]
```

### Step 4.3: Validate the System

Check that documentation is usable:

- [ ] Can you find what you captured?
- [ ] Is the rating system clear?
- [ ] Do metrics make sense?
- [ ] Is the loop practical?

---

## Phase 5: Establish Rhythms

### Step 5.1: Iteration Rhythm

Make the loop automatic:

```
Before each iteration:
  □ Consult LEARNING.md
  □ Review recent OUTPUTS.md
  □ Check METRICS.md trends

During each iteration:
  □ Capture observations in real-time
  □ Note surprises

After each iteration:
  □ Rate output
  □ Log metrics
  □ Update LEARNING.md
```

### Step 5.2: Retrospective Rhythm

Schedule regular reviews:

| Review | Frequency | Duration | Focus |
|--------|-----------|----------|-------|
| Micro | Every iteration | 5-10 min | Capture |
| Meso | Every 5 iterations | 30-60 min | Patterns & process |
| Macro | Every 20 iterations | 2-4 hours | Strategy & architecture |

### Step 5.3: Documentation Rhythm

Keep docs current:

- LEARNING.md: Update every iteration
- METRICS.md: Update tracking every iteration, analysis every meso cycle
- OUTPUTS.md: Update every rated output
- LOOP.md: Update during meso/macro cycles
- EVOLUTION.md: Update during macro cycles

---

## Phase 6: Verify & Calibrate

### Step 6.1: After 5 Iterations

First meso review:

```markdown
## 5-Iteration Verification

### Is capture working?
- [ ] LEARNING.md has [N] new entries
- [ ] OUTPUTS.md has [N] rated items
- [ ] METRICS.md is being tracked

### Are patterns emerging?
- [ ] Can identify at least 1 pattern
- [ ] Some observations ready for promotion

### Is the process practical?
- [ ] Loop is followed consistently
- [ ] Documentation overhead acceptable
- [ ] System adds value, not just overhead

### Calibration needed?
- [ ] Rating scale appropriate?
- [ ] Metrics meaningful?
- [ ] Cycle frequencies right?
```

### Step 6.2: After 20 Iterations

First macro review:

```markdown
## 20-Iteration Verification

### Is knowledge accumulating?
- [ ] LEARNING.md has promoted patterns
- [ ] Anti-patterns are preventing mistakes
- [ ] Predictions improving

### Is quality improving?
- [ ] Compare iteration 20 to iteration 1
- [ ] Trend in ratings
- [ ] Reduction in failures

### Is the system improving itself?
- [ ] Process has been refined
- [ ] Documentation is evolving
- [ ] Meta-observations being made
```

### Step 6.3: Adjust & Continue

Based on reviews:

1. **What's working**: Keep and reinforce
2. **What's not working**: Modify or remove
3. **What's missing**: Add
4. **What's overhead**: Simplify

---

## Checklist

### Pre-Launch
- [ ] Iteration unit defined
- [ ] Quality criteria established
- [ ] Knowledge types identified
- [ ] Metrics specified
- [ ] Directory structure created
- [ ] Templates customized
- [ ] Core loop documented
- [ ] Review cycles scheduled

### First 5 Iterations
- [ ] 5 iterations completed
- [ ] Learnings captured each time
- [ ] Outputs rated
- [ ] Metrics tracked
- [ ] First meso review done
- [ ] System calibrated

### First 20 Iterations
- [ ] 20 iterations completed
- [ ] Patterns emerging
- [ ] Anti-patterns documented
- [ ] Quality trend visible
- [ ] First macro review done
- [ ] System demonstrably improving

### Ongoing
- [ ] Iteration rhythm automatic
- [ ] Retrospectives happening
- [ ] Knowledge compounding
- [ ] Process evolving
- [ ] Meta-observation active

---

## Common Pitfalls

### 1. Over-Engineering at Start
Don't try to perfect the system before using it. Start simple, evolve.

### 2. Capture Fatigue
If capture feels burdensome, simplify. Better to capture less consistently than more inconsistently.

### 3. Metric Obsession
Metrics inform, they don't decide. Use them as input, not gospel.

### 4. Review Skipping
Retrospectives feel optional until they're not. Missing them degrades the system.

### 5. Documentation Decay
If docs aren't current, they're not useful. Currency > comprehensiveness.

---

## Success Indicators

You know the system is working when:

1. **You consult docs naturally**: LEARNING.md informs decisions without forcing
2. **Patterns emerge**: You see what works across iterations
3. **Quality rises**: Later iterations outperform earlier ones
4. **Failures teach**: Mistakes don't repeat
5. **The system evolves**: Process improves over time
6. **Meta-awareness exists**: You notice how you're learning

---

## Next Steps

After bootstrapping:

1. Complete 5 iterations
2. Run first meso review
3. Calibrate and continue
4. Complete 20 iterations
5. Run first macro review
6. Celebrate the learning system you've built

The system will take care of the rest—getting better forever.
