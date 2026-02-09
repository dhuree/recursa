# Iteration Loop

## Overview

Each code review is one iteration. The goal is to provide valuable feedback and learn from the outcome.

---

## Phase 1: RECEIVE (5 min)

### Actions
- [ ] Get PR details (title, description, author, size)
- [ ] Note the PR's stated purpose
- [ ] Check author's experience level (new contributor vs. veteran)
- [ ] Identify affected areas of codebase

### Checklist
- [ ] PR description explains the "why"
- [ ] Linked issue or ticket (if applicable)
- [ ] Appropriate size (flag if too large)

---

## Phase 2: ANALYZE (15-30 min)

### Actions
- [ ] Read through all changed files
- [ ] Understand the change in context of the system
- [ ] Check for patterns from LEARNING.md
- [ ] Run through quality checklist

### Quality Checklist

**Correctness**
- [ ] Logic is sound
- [ ] Edge cases handled
- [ ] Error handling appropriate
- [ ] No security vulnerabilities

**Clarity**
- [ ] Code is readable
- [ ] Names are descriptive
- [ ] Comments where needed (not obvious)
- [ ] No unnecessary complexity

**Consistency**
- [ ] Follows codebase conventions
- [ ] Matches existing patterns
- [ ] Style guide compliance

**Testing**
- [ ] Tests cover new functionality
- [ ] Tests are meaningful (not just coverage)
- [ ] Edge cases tested

---

## Phase 3: COMMENT (10-20 min)

### Actions
- [ ] Prioritize findings (blocker → suggestion → nitpick)
- [ ] Write clear, actionable comments
- [ ] Include code examples where helpful
- [ ] Note any positive patterns observed

### Comment Categories

| Category | Label | Requires Change |
|----------|-------|-----------------|
| Blocker | `[BLOCKER]` | Yes - cannot merge |
| Issue | `[ISSUE]` | Yes - should fix |
| Suggestion | `[SUGGESTION]` | No - consider |
| Nitpick | `[NIT]` | No - optional |
| Question | `[QUESTION]` | Needs clarification |
| Praise | `[NICE]` | No - positive feedback |

### Comment Template

```
[CATEGORY] Brief title

What: Describe the issue or suggestion
Why: Explain the reasoning
How: Provide fix or alternative (with code example if helpful)
```

---

## Phase 4: SUBMIT (5 min)

### Actions
- [ ] Review all comments for tone
- [ ] Ensure balanced feedback (not all negative)
- [ ] Set appropriate review status
- [ ] Submit review

### Review Statuses
- **Approve**: Good to merge (may have minor suggestions)
- **Request Changes**: Has blockers or significant issues
- **Comment**: Feedback only, no strong opinion

---

## Phase 5: TRACK OUTCOME (after PR closed)

### Actions
- [ ] Note which suggestions were accepted
- [ ] Note which were declined (and why if stated)
- [ ] Record any bugs that made it through
- [ ] Update LEARNING.md with patterns

### Outcome Tracking

| Suggestion | Category | Accepted | Notes |
|------------|----------|----------|-------|
| [summary] | [cat] | Yes/No/Modified | [why] |

---

## Phase 6: CAPTURE (5 min)

### After Each Review
- [ ] Log metrics in METRICS.md
- [ ] Update LEARNING.md if new pattern discovered
- [ ] Note any process improvements needed

### Metrics to Capture
- Review time (total minutes)
- PR size (files changed, lines changed)
- Comments made by category
- Suggestions accepted/declined

---

## Cycle Frequencies

### Every Review (Micro)
- Complete phases 1-6
- Log basic metrics

### Every 10 Reviews (Meso)
- Review acceptance rate by category
- Identify declining patterns
- Adjust comment thresholds

### Every 50 Reviews (Macro)
- Analyze bug escape rate
- Review developer feedback
- Update quality checklist
- Revise LEARNING.md principles
