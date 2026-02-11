# Recurring Task: Issue Triage

<!--
TEMPLATE INSTRUCTIONS:
1. This task runs during each meso-retrospective
2. Customize time budget and escalation criteria for your domain
3. Remove this instruction block when done
-->

**Frequency**: Every [N] iterations (during meso retrospective)
**Duration**: ~15-30 minutes
**Priority**: Medium-High

---

## Trigger

After the meso retrospective metrics review, before writing the reflection.

---

## Checklist

### 1. Bug Triage

Review ISSUES.md Bugs section:

- [ ] **High severity bugs**: Must fix before next iteration
  - If >30 min to fix: Create minimal workaround, document, schedule fix
- [ ] **Medium severity bugs**:
  - Has workaround? → Verify workaround documented, schedule fix for macro
  - No workaround? → Escalate to High or implement workaround
- [ ] **Low severity bugs**: Batch for macro review (no action needed now)

### 2. Feature Requests

Review ISSUES.md Feature Requests section:

- [ ] **Quick wins (<30 min)**: Implement now during this triage session
- [ ] **Parameterization backlog**: Pick 2-3 highest-priority params to expose
- [ ] **Larger features**: Add to macro review agenda

### 3. Code Quality

Review ISSUES.md Code Quality section:

- [ ] **Silent failures**: Add error handling with clear messages
- [ ] **Missing validations**: Add input validation to prevent invalid configurations

### 4. Stale Issue Review

- [ ] Any issues older than [M] iterations? → Either fix, close, or document why blocked
- [ ] Any issues marked "In Progress" but stalled? → Update status

---

## Quick Fix Protocol

For issues fixable in <30 minutes:

1. Create a backup/branch if modifying core code
2. Implement the fix
3. Test with a case that previously failed
4. Update ISSUES.md status to "Fixed"
5. Move to "Recently Fixed" section with brief notes

---

## Escalation Criteria

Escalate to **macro review** if:
- Bug count (High + Medium) exceeds threshold for your domain
- Same bug recurring across iterations
- Feature request would significantly improve output quality
- Technical debt blocking core exploration

---

## Output

After triage:
- [ ] ISSUES.md status updated for addressed items
- [ ] Recently Fixed section updated with this session's fixes
- [ ] Any new parameters documented appropriately
- [ ] Remaining backlog prioritized for next triage or macro review

---

## Time Budget

| Category | Max Time |
|----------|----------|
| Bug triage & quick fixes | [X] min |
| Feature quick wins | [X] min |
| Parameterization | [X] min |
| Documentation updates | [X] min |
| **Total** | **~[Y] min max** |

If exceeding budget, note remaining items for macro review.

---

## Connection to Other Processes

- **Meso Retrospective**: Issue triage happens DURING meso, after metrics review
- **Macro Review**: Deep dive on all issues, clear stale backlog
- **EVOLUTION.md**: Log significant code changes in Change Log
- **LEARNING.md**: If bug reveals a structural limitation, document as anti-pattern
