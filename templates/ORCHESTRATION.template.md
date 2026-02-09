# Orchestration

Multi-agent coordination patterns for complex self-improving systems.

---

## When to Use Multiple Agents

Use orchestration when:
- Tasks benefit from **specialization** (research vs. execution vs. review)
- Work can be **parallelized** for efficiency
- **Quality gates** require independent verification
- The system needs **separation of concerns** (executor vs. critic)

Single-agent is fine when:
- Tasks are sequential and straightforward
- Context sharing between steps is critical
- The overhead of coordination exceeds benefits

---

## Agent Roles

### Standard Roles

| Role | Responsibility | Example Tasks |
|------|----------------|---------------|
| **Coordinator** | Task decomposition, assignment, synthesis | Break down goals, merge outputs |
| **Researcher** | Information gathering, analysis | Search, read, summarize |
| **Executor** | Core domain work | Write, build, create |
| **Reviewer** | Quality assessment, critique | Evaluate, rate, suggest |
| **Specialist** | Domain-specific expertise | [Your domain experts] |

### Role Definition Template

```markdown
## [Role Name]

**Purpose**: [One sentence describing this role's function]

**Capabilities**:
- [Capability 1]
- [Capability 2]

**Constraints**:
- [What this role cannot do]
- [Escalation triggers]

**Inputs**: [What this role receives]
**Outputs**: [What this role produces]

**Success Criteria**: [How to measure effectiveness]
```

---

## Communication Patterns

### 1. Hub-and-Spoke (Coordinator-Centric)

```
                    ┌──────────┐
                    │Coordinator│
                    └─────┬────┘
           ┌──────────────┼──────────────┐
           ▼              ▼              ▼
      ┌────────┐    ┌────────┐    ┌────────┐
      │Agent A │    │Agent B │    │Agent C │
      └────────┘    └────────┘    └────────┘
```

**Use when**: Central oversight needed, agents don't need to communicate directly
**Coordination overhead**: Medium
**Example**: Research team where coordinator assigns papers and merges findings

### 2. Pipeline (Sequential Handoff)

```
      ┌────────┐    ┌────────┐    ┌────────┐    ┌────────┐
      │Research│ ─→ │ Draft  │ ─→ │ Review │ ─→ │ Finalize│
      └────────┘    └────────┘    └────────┘    └────────┘
```

**Use when**: Work flows through distinct phases
**Coordination overhead**: Low
**Example**: Content creation (research → write → edit → publish)

### 3. Parallel Workers

```
           ┌────────┐
      ┌───→│Worker 1│───┐
      │    └────────┘   │
      │    ┌────────┐   │
─────┬┼───→│Worker 2│───┼┬─────→ Merge
      │    └────────┘   │
      │    ┌────────┐   │
      └───→│Worker 3│───┘
           └────────┘
```

**Use when**: Work can be partitioned independently
**Coordination overhead**: Medium (merge complexity)
**Example**: Analyzing multiple data sources simultaneously

### 4. Adversarial (Executor + Critic)

```
      ┌────────┐         ┌────────┐
      │Executor│ ◀─────▶ │ Critic │
      └────────┘         └────────┘
           │                  │
           └────────┬─────────┘
                    ▼
              ┌──────────┐
              │  Output  │
              └──────────┘
```

**Use when**: Quality is critical, self-critique isn't sufficient
**Coordination overhead**: Medium-High
**Example**: Code generation with security reviewer

---

## Task Decomposition

### Decomposition Strategies

1. **By Phase**: Divide by workflow stages (research, draft, review)
2. **By Component**: Divide by output parts (intro, body, conclusion)
3. **By Perspective**: Divide by viewpoints (optimist, pessimist, realist)
4. **By Expertise**: Divide by required knowledge (domain, technical, style)

### Decomposition Template

```markdown
## Task: [Main Task]

### Subtasks

| ID | Subtask | Assigned To | Dependencies | Output |
|----|---------|-------------|--------------|--------|
| 1 | [Task] | [Role] | None | [Output] |
| 2 | [Task] | [Role] | 1 | [Output] |
| 3 | [Task] | [Role] | 1, 2 | [Output] |

### Merge Strategy
[How outputs will be combined]

### Quality Gates
[Checkpoints before proceeding]
```

---

## Handoff Protocol

### Standard Handoff Format

```markdown
## Handoff: [From Role] → [To Role]

**Task**: [What the receiving agent should do]

**Context**:
- [Relevant background]
- [Previous decisions made]

**Inputs Provided**:
- [Input 1]: [Description]
- [Input 2]: [Description]

**Expected Output**:
- [What to produce]
- [Quality criteria]

**Constraints**:
- [Time/resource limits]
- [Scope boundaries]

**Escalation**: [When to escalate back]
```

### Handoff Checklist

Before handing off:
- [ ] Context is complete (receiver won't need to ask questions)
- [ ] Inputs are clearly labeled
- [ ] Success criteria are explicit
- [ ] Escalation conditions defined
- [ ] No circular dependencies

---

## Supervision & Escalation

### Supervision Levels

| Level | Description | Example |
|-------|-------------|---------|
| **Autonomous** | Agent works independently | Routine tasks |
| **Monitored** | Coordinator reviews output | Standard work |
| **Supervised** | Coordinator approves before action | Sensitive work |
| **Human-in-loop** | Human approval required | Critical decisions |

### Escalation Triggers

Define when agents should escalate to coordinator or human:

```markdown
## Escalation Policy

### To Coordinator
- Uncertainty > [X]% on core decision
- Conflicting guidance from multiple sources
- Resource request exceeding [limit]
- Dependency blocker

### To Human
- Safety-related concern
- Ethical ambiguity
- Novel situation not covered by guidelines
- Coordinator uncertainty > [Y]%
```

---

## Conflict Resolution

When agents disagree:

1. **Document the disagreement**: Each agent states their position
2. **Identify the crux**: What's the core difference?
3. **Gather evidence**: Each side provides supporting data
4. **Escalate if needed**: Coordinator or human decides
5. **Record the decision**: For future learning

### Resolution Template

```markdown
## Conflict: [Topic]

**Agent A Position**: [View]
**Agent B Position**: [View]

**Evidence**:
- A: [Supporting data]
- B: [Supporting data]

**Resolution**: [Decision made]
**Rationale**: [Why this decision]
**Learning**: [What to remember for future]
```

---

## Multi-Agent Memory

### Shared vs. Private Memory

| Memory Type | Visibility | Purpose |
|-------------|-----------|---------|
| **Global** | All agents | Common knowledge, guidelines |
| **Team** | Role group | Specialized knowledge |
| **Private** | Single agent | Working state, drafts |
| **Handoff** | Sender + receiver | Task-specific context |

### Memory Synchronization

```markdown
## Sync Protocol

### On Task Start
1. Load global memory
2. Load role-specific memory
3. Load task context from handoff

### On Task Complete
1. Commit learnings to appropriate memory level
2. Clear private working memory
3. Create handoff for next agent (if any)

### Conflict Handling
- Later writes win for operational data
- Coordinator adjudicates for knowledge conflicts
```

---

## Example: Research Synthesis Team

### Roles

```
Coordinator: Decomposes questions, assigns sources, merges findings
Researcher A: Searches academic sources
Researcher B: Searches industry sources
Synthesizer: Combines findings into coherent summary
Critic: Reviews for gaps and biases
```

### Workflow

```
1. Coordinator receives question
2. Coordinator decomposes into search tasks
3. Researchers A & B search in parallel
4. Researchers hand off findings to Synthesizer
5. Synthesizer creates draft summary
6. Critic reviews and suggests improvements
7. Synthesizer revises
8. Coordinator does final review
9. Output delivered
```

### Communication Flow

```
                         ┌────────────┐
                         │Coordinator │
                         └─────┬──────┘
                    ┌──────────┴──────────┐
                    ▼                      ▼
             ┌────────────┐         ┌────────────┐
             │Researcher A│         │Researcher B│
             └──────┬─────┘         └──────┬─────┘
                    └──────────┬───────────┘
                               ▼
                        ┌────────────┐
                        │Synthesizer │◀────┐
                        └──────┬─────┘     │
                               ▼           │
                        ┌────────────┐     │
                        │   Critic   │─────┘
                        └──────┬─────┘
                               ▼
                         ┌──────────┐
                         │  Output  │
                         └──────────┘
```

---

## Anti-Patterns

### Avoid These

1. **Over-decomposition**: More agents than needed increases overhead
2. **Circular dependencies**: A waits for B waits for A
3. **Context loss**: Critical info not passed in handoffs
4. **Coordinator bottleneck**: Everything flows through one point
5. **Role confusion**: Unclear who owns what
6. **Memory silos**: Agents can't access needed knowledge

### Red Flags

- Agents frequently ask "who handles this?"
- Handoffs require multiple clarification rounds
- Coordinator is overwhelmed while agents idle
- Same information requested multiple times
- Conflicts escalated that shouldn't need to be

---

## Implementation Checklist

- [ ] Roles clearly defined with capabilities and constraints
- [ ] Communication pattern chosen and documented
- [ ] Handoff format standardized
- [ ] Escalation policy explicit
- [ ] Memory architecture decided
- [ ] Conflict resolution process documented
- [ ] Monitoring/observability in place
