# Issues & Improvements

<!--
TEMPLATE INSTRUCTIONS:
1. Track bugs, performance issues, and feature requests discovered during iteration
2. Review during meso-retrospective (triage) and macro review (deep dive)
3. Customize severity criteria for your domain
4. Remove this instruction block when done
-->

Track bugs, performance issues, and feature requests discovered during iteration.

---

## Bugs

| ID | Category | Issue | Severity | Status |
|----|----------|-------|----------|--------|
| B001 | <!-- Category --> | <!-- Description --> | <!-- High/Medium/Low --> | Open |

### Severity Guide (Bugs)

| Severity | Criteria | Action |
|----------|----------|--------|
| **High** | Blocks core work or produces incorrect output | Fix before next iteration |
| **Medium** | Annoying but has workaround | Document workaround, schedule fix |
| **Low** | Minor issue, doesn't affect quality | Batch for macro review |

---

## Performance

| ID | Category | Issue | Impact | Status |
|----|----------|-------|--------|--------|
| P001 | <!-- Category --> | <!-- Description --> | <!-- High/Medium/Low --> | Open |

---

## Feature Requests

| ID | Category | Request | Priority | Status |
|----|----------|---------|----------|--------|
| F001 | <!-- Category --> | <!-- Description --> | <!-- High/Medium/Low --> | Open |

### Priority Guide (Features)

| Priority | Criteria | When to Address |
|----------|----------|-----------------|
| **High** | Would significantly improve quality or efficiency | Next meso triage |
| **Medium** | Nice to have, enables new exploration | Macro review |
| **Low** | Minor enhancement | When convenient |

---

## Code Quality / Technical Debt

| ID | Area | Issue | Priority | Status |
|----|------|-------|----------|--------|
| Q001 | <!-- Area --> | <!-- Description --> | <!-- High/Medium/Low --> | Open |

---

## Recently Fixed

| ID | Issue | Fixed In | Notes |
|----|-------|----------|-------|
| <!-- ID --> | <!-- Brief description --> | <!-- Iteration/date --> | <!-- How it was fixed --> |

---

## Usage

### Adding Issues

When you discover an issue during iteration:

```markdown
| B007 | Category | Description of bug | High/Medium/Low | Open |
```

### Status Values

- **Open**: Not yet addressed
- **In Progress**: Currently being worked on
- **Blocked**: Waiting on external dependency
- **Workaround**: Issue exists but has documented workaround
- **Fixed**: Resolved (move to Recently Fixed)
- **Won't Fix**: Intentionally not addressing (document reason)

### During Iteration

1. Discover issue while working
2. Add to appropriate table above
3. Fix immediately if <5 min, otherwise note and continue
4. Address accumulated issues during meso triage

### Stale Issue Policy

Issues older than [M] iterations (macro cycle) should be:
- Fixed
- Closed with explanation
- Documented as blocked (with blocker reason)

---

## Parameterization Backlog

Track hardcoded values that should be configurable:

| ID | File | Line | Current Value | Suggested Parameter | Priority |
|----|------|------|---------------|---------------------|----------|
| F0XX-1 | <!-- path --> | <!-- line --> | <!-- value --> | <!-- param_name --> | <!-- H/M/L --> |

### Parameterization Priority

| Priority | Criteria |
|----------|----------|
| **High** | Limits exploration, affects core algorithms |
| **Medium** | Would enable new variations, affects output |
| **Low** | Nice-to-have flexibility |

At each meso triage, implement 2-3 high-priority parameterizations.
