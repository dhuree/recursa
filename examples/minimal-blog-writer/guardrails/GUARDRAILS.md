# Guardrails — Safety Infrastructure

Safety policies for the BlogCraft blog writing system.

---

## Safety Philosophy

Quality content requires trust. These guardrails ensure the system produces accurate, ethical content while maintaining human oversight for critical decisions.

---

## Action Tiers

### Tier 1: Autonomous (No Approval Required)

- Drafting blog post content
- Editing and revising drafts
- Researching topics online
- Organizing notes and outlines
- Running code examples locally

### Tier 2: Notify (Inform Human After)

- Creating new files in the deliverables folder
- Updating LEARNING.md with new patterns
- Modifying drafts based on feedback

### Tier 3: Confirm (Ask Before Acting)

- Publishing content externally
- Sending drafts for external review
- Deleting completed posts
- Making API calls to external services

### Tier 4: Forbidden (Never Do)

- Publishing without human review
- Plagiarizing content
- Fabricating technical information
- Claiming false expertise or credentials
- Including untested code examples

---

## Content Safety

### Accuracy Requirements

- All technical claims must be verifiable
- Code examples must be tested before inclusion
- External sources must be cited
- Uncertainty must be acknowledged

### Prohibited Content

- Misinformation or unverified claims
- Content that could harm readers if followed
- Plagiarized material
- Discriminatory or offensive content

---

## Quality Gates

Before any post is considered "ready":

- [ ] Technical accuracy verified
- [ ] Code examples tested and working
- [ ] Sources cited where appropriate
- [ ] Reviewed for clarity and accessibility
- [ ] Human approval received

---

## Audit Trail

All significant actions are logged to `guardrails/audit/action_log.jsonl`:

```json
{
  "timestamp": "ISO-8601",
  "action": "action_type",
  "tier": 1-4,
  "details": {},
  "outcome": "success|failure|pending"
}
```

---

## Rollback Procedures

If a problem is discovered:

1. Identify the problematic content
2. Revert to last known good state (git)
3. Document what went wrong in journal/reflections/
4. Update LEARNING.md to prevent recurrence

---

**Version**: 1.0
