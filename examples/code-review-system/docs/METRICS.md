# Metrics

Quantitative tracking for code review effectiveness.

---

## Quality Scale

| Rating | Meaning | Criteria |
|--------|---------|----------|
| 5/5 | Exceptional | Caught critical issue, highly educational, fully accepted |
| 4/5 | Strong | Useful feedback, mostly accepted, clear communication |
| 3/5 | Adequate | Some value provided, mixed acceptance |
| 2/5 | Weak | Low acceptance, unclear or unhelpful comments |
| 1/5 | Failed | Missed critical issue, or blocked valid PR incorrectly |

---

## Key Metrics

### Effectiveness Metrics
| Metric | Target | Current |
|--------|--------|---------|
| Suggestion acceptance rate | >70% | -- |
| Bug catch rate | >90% of preventable bugs | -- |
| False positive rate | <10% | -- |
| Review turnaround | <4 hours | -- |

### Volume Metrics
| Metric | This Week | This Month | All Time |
|--------|-----------|------------|----------|
| Reviews completed | | | |
| Comments made | | | |
| Blockers identified | | | |
| Bugs caught | | | |

---

## Review Log

| # | Date | PR | Size | Time | Comments | Accepted | Quality | Notes |
|---|------|-----|------|------|----------|----------|---------|-------|
| 1 | | | | | | | | |

### Size Categories
- **S**: <50 lines changed
- **M**: 50-200 lines changed
- **L**: 200-500 lines changed
- **XL**: >500 lines changed

---

## Acceptance Tracking

### By Category
| Category | Made | Accepted | Rate |
|----------|------|----------|------|
| Blocker | | | |
| Issue | | | |
| Suggestion | | | |
| Nitpick | | | |

### By Domain
| Area | Made | Accepted | Rate |
|------|------|----------|------|
| Security | | | |
| Performance | | | |
| Logic | | | |
| Style | | | |
| Testing | | | |

---

## Bug Escapes

Track bugs that made it to production that could have been caught in review.

| Date | Bug | Severity | Why Missed | Learning |
|------|-----|----------|------------|----------|
| | | | | |

---

## Trends

### Acceptance Rate Over Time
```
Week 1: --%
Week 2: --%
Week 3: --%
Week 4: --%
```

### Review Time Over Time
```
Week 1: -- min avg
Week 2: -- min avg
Week 3: -- min avg
Week 4: -- min avg
```

---

## Trigger Actions

| Condition | Action |
|-----------|--------|
| Acceptance rate <50% for 5 reviews | Review comment style and relevance |
| Bug escape | Add to LEARNING.md, update checklist |
| Review time >60min | Check if PR too large, suggest split |
| 3 consecutive low-quality reviews | Take a break, review SOUL.md |

---

## Monthly Summary Template

```markdown
## Month: [YYYY-MM]

### Volume
- Reviews: X
- Comments: X
- Avg review time: X min

### Quality
- Acceptance rate: X%
- Bugs caught: X
- Bugs escaped: X

### Learnings Added
- Principles: X
- Patterns: X
- Observations: X

### Process Changes
- [What changed and why]

### Focus for Next Month
- [Priority area]
```
