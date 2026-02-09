# Domain Discovery Interview

This document contains the structured interview questions for discovering a user's domain when bootstrapping a new Recursa-based self-improving system.

---

## Quick Reference: Required Questions

For a **minimal bootstrap** (5 minutes), ask only these **6 essential questions**:

| ID | Question | Maps To |
|----|----------|---------|
| D1 | What is this system for? | SOUL.md purpose |
| I1 | What is one cycle of work? | LOOP.md iteration |
| I2 | How long does a typical iteration take? | LOOP.md timing |
| Q1 | How do you know when output is excellent? | METRICS.md rating |
| Q3 | What are the must-have qualities? | CONSTITUTION.md |
| S1 | What actions need approval? | CONSTITUTION.md tiers |

For a **standard bootstrap** (15-20 minutes), also include:
- D4, I4, I5, Q4, Q6, K1, K3, K4, P1, P4, S2, S4

For a **comprehensive bootstrap** (30+ minutes), use all questions.

---

## Question Priority Legend

Throughout this document:
- **Required** = Must ask for minimal viable system
- **Recommended** = Strongly improves customization
- **Optional** = Nice to have, domain-dependent

---

## How to Use This Interview

1. **Don't ask all questions** - Select relevant ones based on context
2. **Use AskUserQuestion tool** - Batch 2-4 questions at a time
3. **Follow up on unclear answers** - Probe deeper when needed
4. **Adapt to domain** - Skip irrelevant sections
5. **Capture everything** - Record answers for document generation

---

## Phase 1: Domain Definition

### Core Purpose
These questions establish what the system is for.

| ID | Question | Required | Maps To |
|----|----------|----------|---------|
| D1 | What is this system for? What problem does it solve? | Yes | SOUL.md purpose |
| D2 | Who will use this system? (You, a team, automated?) | Yes | SOUL.md relationship |
| D3 | What domain or field is this in? | Yes | Categories in LEARNING.md |
| D4 | What does success look like for this system overall? | Yes | SOUL.md optimization targets |

**Example AskUserQuestion batch:**
```json
{
  "questions": [
    {
      "question": "What is this system for? What problem will it help you solve?",
      "header": "Purpose",
      "options": [
        {"label": "Creative work", "description": "Art, writing, music, design"},
        {"label": "Software development", "description": "Coding, testing, deployment"},
        {"label": "Research & learning", "description": "Study, experimentation, knowledge"},
        {"label": "Business process", "description": "Sales, operations, management"}
      ]
    },
    {
      "question": "Who will be using this system?",
      "header": "Users",
      "options": [
        {"label": "Just me", "description": "Personal productivity system"},
        {"label": "Small team", "description": "2-5 people collaborating"},
        {"label": "Automated agent", "description": "AI-driven with human oversight"},
        {"label": "Hybrid", "description": "Mix of human and automated use"}
      ]
    }
  ]
}
```

---

## Phase 2: Iteration Definition

### The Work Cycle
These questions define what one iteration looks like.

| ID | Question | Required | Maps To |
|----|----------|----------|---------|
| I1 | What is one cycle/iteration of work? | Yes | LOOP.md iteration unit |
| I2 | How long does a typical iteration take? | Yes | LOOP.md timing |
| I3 | What are the inputs to an iteration? | Yes | LOOP.md prepare phase |
| I4 | What are the outputs of an iteration? | Yes | LOOP.md deliverables |
| I5 | What steps happen during an iteration? | Yes | LOOP.md execute phase |
| I6 | How do you know when an iteration is complete? | Yes | LOOP.md completion criteria |

**Example AskUserQuestion batch:**
```json
{
  "questions": [
    {
      "question": "What does one cycle of work look like? (e.g., 'write one blog post', 'complete one feature', 'run one experiment')",
      "header": "Iteration",
      "options": [
        {"label": "Single task", "description": "One discrete unit of work"},
        {"label": "Time block", "description": "A fixed time period of work"},
        {"label": "Project phase", "description": "A stage of a larger project"},
        {"label": "Other", "description": "I'll describe my iteration"}
      ]
    },
    {
      "question": "How long does a typical iteration take?",
      "header": "Duration",
      "options": [
        {"label": "< 1 hour", "description": "Quick iterations"},
        {"label": "1-4 hours", "description": "Half-day iterations"},
        {"label": "1 day", "description": "Daily iterations"},
        {"label": "Multiple days", "description": "Longer iteration cycles"}
      ]
    }
  ]
}
```

---

## Phase 3: Quality Definition

### Success Criteria
These questions define what "good" means in this domain.

| ID | Question | Required | Maps To |
|----|----------|----------|---------|
| Q1 | How do you know when output is excellent (5/5)? | Yes | METRICS.md rating scale |
| Q2 | What makes output good but not great (4/5)? | Yes | METRICS.md rating scale |
| Q3 | What are the must-have qualities? | Yes | CONSTITUTION.md non-negotiables |
| Q4 | What makes output fail (1-2/5)? | Yes | LEARNING.md anti-patterns |
| Q5 | Are there any external standards or benchmarks? | No | METRICS.md comparison |
| Q6 | What dimensions matter most? (speed, quality, novelty, etc.) | Yes | METRICS.md dimensions |

**Example AskUserQuestion batch:**
```json
{
  "questions": [
    {
      "question": "What makes output excellent (5/5 quality)?",
      "header": "Excellence",
      "options": [
        {"label": "Meets all requirements perfectly", "description": "Complete, correct, polished"},
        {"label": "Exceeds expectations", "description": "Surprising quality or insight"},
        {"label": "Ready for production/publication", "description": "No further work needed"},
        {"label": "Other criteria", "description": "I'll describe my 5/5 standard"}
      ]
    },
    {
      "question": "What are the must-have qualities that can never be compromised?",
      "header": "Non-negotiables",
      "multiSelect": true,
      "options": [
        {"label": "Correctness", "description": "Must be factually/technically accurate"},
        {"label": "Completeness", "description": "Must cover all requirements"},
        {"label": "Clarity", "description": "Must be understandable"},
        {"label": "Timeliness", "description": "Must meet deadlines"}
      ]
    }
  ]
}
```

---

## Phase 4: Knowledge & Learning

### What Can Be Learned
These questions define the knowledge structure.

| ID | Question | Required | Maps To |
|----|----------|----------|---------|
| K1 | What kinds of things can be learned in this domain? | Yes | MEMORY.md knowledge types |
| K2 | What patterns or heuristics might emerge? | Yes | LEARNING.md heuristics |
| K3 | What categories should knowledge be organized into? | Yes | LEARNING.md categories |
| K4 | What mistakes should never be repeated? | Yes | LEARNING.md anti-patterns |
| K5 | How quickly does knowledge become outdated? | No | MEMORY.md decay |
| K6 | What sources of external knowledge exist? | No | Skills/integrations |

**Example AskUserQuestion batch:**
```json
{
  "questions": [
    {
      "question": "What kinds of things can be learned and improved over time?",
      "header": "Learning",
      "multiSelect": true,
      "options": [
        {"label": "Techniques/methods", "description": "How to do things better"},
        {"label": "Domain knowledge", "description": "Facts and concepts"},
        {"label": "User preferences", "description": "What you/users like"},
        {"label": "Tool/skill proficiency", "description": "Getting better at tools"}
      ]
    },
    {
      "question": "How should knowledge be organized? What are the main categories?",
      "header": "Categories",
      "options": [
        {"label": "By topic/subject", "description": "Organize by what it's about"},
        {"label": "By technique/method", "description": "Organize by how it's done"},
        {"label": "By project/context", "description": "Organize by where it applies"},
        {"label": "Other structure", "description": "I'll describe my categories"}
      ]
    }
  ]
}
```

---

## Phase 5: Identity & Personality

### System Character
These questions define the system's personality.

| ID | Question | Required | Maps To |
|----|----------|----------|---------|
| P1 | What name should this system have? | Recommended | IDENTITY.md name |
| P2 | What personality traits should it exhibit? | No | SOUL.md traits |
| P3 | What communication style is appropriate? | No | STYLE.md tone |
| P4 | What values should guide decisions? | Yes | SOUL.md values |
| P5 | How formal or casual should it be? | No | STYLE.md formality |
| P6 | Are there any role models or examples to emulate? | No | SOUL.md inspiration |

**Example AskUserQuestion batch:**
```json
{
  "questions": [
    {
      "question": "What should this system be named?",
      "header": "Name",
      "options": [
        {"label": "Suggest names for me", "description": "Based on the domain"},
        {"label": "Keep it generic", "description": "Just call it 'the system'"},
        {"label": "I have a name", "description": "I'll provide a name"},
        {"label": "No name needed", "description": "Prefer not to name it"}
      ]
    },
    {
      "question": "What personality should the system have?",
      "header": "Personality",
      "options": [
        {"label": "Professional & precise", "description": "Formal, accurate, thorough"},
        {"label": "Friendly & encouraging", "description": "Warm, supportive, positive"},
        {"label": "Direct & efficient", "description": "No-nonsense, action-oriented"},
        {"label": "Creative & exploratory", "description": "Curious, experimental, playful"}
      ]
    }
  ]
}
```

---

## Phase 6: Safety & Constraints

### Guardrails
These questions define safety requirements.

| ID | Question | Required | Maps To |
|----|----------|----------|---------|
| S1 | What actions should require human approval? | Yes | CONSTITUTION.md tiers |
| S2 | What should the system never do? | Yes | CONSTITUTION.md forbidden |
| S3 | Are there resource limits to enforce? | No | GUARDRAILS.md limits |
| S4 | What should trigger escalation to a human? | Yes | CONSTITUTION.md triggers |
| S5 | Are there sensitive data types to protect? | No | GUARDRAILS.md data policy |
| S6 | What external systems can be accessed? | No | PERMISSIONS.md |

**Example AskUserQuestion batch:**
```json
{
  "questions": [
    {
      "question": "What actions should always require your approval first?",
      "header": "Approval",
      "multiSelect": true,
      "options": [
        {"label": "External communications", "description": "Sending emails, messages"},
        {"label": "File deletions", "description": "Removing any files"},
        {"label": "Spending money", "description": "Any financial transactions"},
        {"label": "Publishing content", "description": "Making things public"}
      ]
    },
    {
      "question": "What should the system absolutely never do?",
      "header": "Forbidden",
      "multiSelect": true,
      "options": [
        {"label": "Share private data", "description": "No data leaves the system"},
        {"label": "Make irreversible changes", "description": "Must be able to undo"},
        {"label": "Act without logging", "description": "All actions must be recorded"},
        {"label": "Exceed budgets", "description": "No overspending"}
      ]
    }
  ]
}
```

---

## Phase 7: Process & Workflow

### How It Should Work
These questions refine the operational details.

| ID | Question | Required | Maps To |
|----|----------|----------|---------|
| W1 | What should happen at the start of each session? | Yes | LOOP.md prepare |
| W2 | How often should retrospectives happen? | Yes | LOOP.md cycles |
| W3 | What tools or integrations are needed? | No | Skills to create |
| W4 | How should progress be tracked? | No | METRICS.md tracking |
| W5 | Are there recurring tasks or schedules? | No | Tasks/cron |
| W6 | How should work be organized (projects, categories)? | No | Deliverables structure |

---

## Interview Flow Recommendation

### Minimal Interview (5-10 minutes)
For quick bootstrapping, ask only:
- D1 (Purpose)
- I1 + I2 (Iteration unit and duration)
- Q1 + Q3 (Excellence and non-negotiables)
- K1 (What can be learned)
- S1 (What needs approval)

### Standard Interview (15-20 minutes)
Add:
- D4 (Success definition)
- I4 + I5 (Outputs and steps)
- Q4 + Q6 (Failure modes and dimensions)
- K3 + K4 (Categories and anti-patterns)
- P1 + P4 (Name and values)
- S2 + S4 (Forbidden actions and escalation)

### Comprehensive Interview (30+ minutes)
Include all phases for maximum customization.

---

## Answer Recording Template

Record answers in this format for document generation:

```markdown
## Interview Results

### Domain
- **Purpose**: [D1 answer]
- **Users**: [D2 answer]
- **Field**: [D3 answer]
- **Success vision**: [D4 answer]

### Iteration
- **Unit**: [I1 answer]
- **Duration**: [I2 answer]
- **Inputs**: [I3 answer]
- **Outputs**: [I4 answer]
- **Steps**: [I5 answer]
- **Completion criteria**: [I6 answer]

### Quality
- **5/5 criteria**: [Q1 answer]
- **4/5 criteria**: [Q2 answer]
- **Non-negotiables**: [Q3 answer]
- **Failure modes**: [Q4 answer]
- **Key dimensions**: [Q6 answer]

### Knowledge
- **Learnable things**: [K1 answer]
- **Potential patterns**: [K2 answer]
- **Categories**: [K3 answer]
- **Anti-patterns**: [K4 answer]

### Identity
- **Name**: [P1 answer]
- **Personality**: [P2 answer]
- **Values**: [P4 answer]
- **Style**: [P3/P5 answer]

### Safety
- **Requires approval**: [S1 answer]
- **Forbidden**: [S2 answer]
- **Escalation triggers**: [S4 answer]
- **Resource limits**: [S3 answer]
```

---

## Domain-Specific Question Sets

### For Creative Work (Art, Writing, Music)
Focus on:
- Style and aesthetic preferences
- Inspiration and influences
- Critique and feedback process
- Portfolio vs. exploration balance

### For Software Development
Focus on:
- Code quality standards
- Testing requirements
- Deployment constraints
- Technical debt tolerance

### For Research & Learning
Focus on:
- Knowledge validation methods
- Citation and source standards
- Hypothesis formation
- Experiment design

### For Business Processes
Focus on:
- Stakeholder requirements
- Compliance constraints
- KPIs and metrics
- Approval workflows
