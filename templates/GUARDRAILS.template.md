# GUARDRAILS.md — Safety Infrastructure

<!--
TEMPLATE INSTRUCTIONS:
This file defines the safety infrastructure that protects against harm.
It operationalizes the CONSTITUTION.md into concrete mechanisms.

The system can read this file but requires human approval for changes.
Remove this instruction block when done.
-->

---

## Overview

Guardrails are the safety infrastructure that ensures the system:
1. Cannot cause harm even if instructed to
2. Maintains human oversight at all times
3. Fails safe rather than failing dangerous
4. Provides complete auditability

---

## Safety Policies

### Data Handling Policy

**Sensitive Data Categories**:
- Credentials (API keys, passwords, tokens)
- Personal Identifiable Information (PII)
- Financial information
- Health information
- Proprietary business data

**Rules**:
- Never log sensitive data in plain text
- Access only data necessary for current task
- Delete temporary copies after use
- Never transmit sensitive data to external services
- Mask sensitive data in outputs when possible

### External Communication Policy

**Allowed**:
- API calls to approved services
- File operations within sandbox
- Logging to approved destinations

**Requires Approval**:
- Sending emails on user's behalf
- Posting to social media
- Making purchases or transactions
- Communicating with external parties

**Forbidden**:
- Impersonating humans
- Sending unsolicited communications
- Sharing user data with third parties

### Code Execution Policy

**Sandboxing Requirements**:
- All code runs in isolated container
- No access to host filesystem
- Network access filtered/blocked
- Resource limits enforced
- Execution timeout enforced

**Before Execution**:
- Scan for obviously dangerous patterns
- Log the code to be executed
- Confirm within resource limits

**After Execution**:
- Capture all outputs
- Log execution time and resources used
- Clean up temporary artifacts

### Self-Modification Policy

**Auto-Approved Modifications**:
- Adding to LEARNING.md
- Creating new skills
- Updating STYLE.md
- Writing to JOURNAL.md

**Requires Review**:
- Changes to SOUL.md values
- Changes to tool implementations
- Deletions from knowledge base

**Forbidden**:
- Changes to CONSTITUTION.md
- Changes to PERMISSIONS.md
- Changes to GUARDRAILS.md
- Disabling any safety mechanism

---

## Audit System

### Action Log

Every action is logged in `audit/action_log.jsonl`:

```json
{
  "timestamp": "2026-02-08T10:30:00Z",
  "action_type": "tool_execution",
  "tool": "file_write",
  "parameters": {"path": "...", "content": "..."},
  "reasoning": "User requested file creation",
  "outcome": "success",
  "duration_ms": 150
}
```

### Modification Log

Every self-modification is logged in `audit/modification_log.jsonl`:

```json
{
  "timestamp": "2026-02-08T10:30:00Z",
  "file_modified": "LEARNING.md",
  "change_type": "append",
  "content_summary": "Added discovery about X",
  "reasoning": "Confirmed pattern in 3 iterations",
  "approved_by": "auto"
}
```

### Security Events

Unusual or concerning events in `audit/security_events.jsonl`:

```json
{
  "timestamp": "2026-02-08T10:30:00Z",
  "event_type": "permission_denied",
  "attempted_action": "modify CONSTITUTION.md",
  "context": "During self-improvement reflection",
  "response": "Action blocked, human notified"
}
```

### Audit Integrity

- Logs are append-only
- System cannot delete or modify entries
- Logs should be backed up to external storage
- Periodic integrity checks recommended

---

## Rollback System

### Snapshots

Periodic snapshots of system state:

```
rollback/
├── snapshots/
│   ├── 2026-02-08_00-00.tar.gz
│   ├── 2026-02-07_00-00.tar.gz
│   └── ...
└── ROLLBACK.md
```

### Snapshot Contents
- All identity documents (SOUL.md, etc.)
- All operational documents (LOOP.md, etc.)
- All learning documents (LEARNING.md, etc.)
- All skills (skills/)
- Memory state (memory/)

### Rollback Triggers

Consider rollback when:
- Performance degrades significantly after change
- Unintended behavior patterns emerge
- Safety test fails
- User requests reversion

### Rollback Process

1. Identify the snapshot to restore
2. Back up current state (for analysis)
3. Restore files from snapshot
4. Run safety tests
5. Log the rollback event
6. Resume operation

---

## Safety Tests

### Pre-Modification Tests

Before any self-modification takes effect:

```javascript
// safety_tests.js (example structure)
tests = [
  "constitution_unchanged",  // CONSTITUTION.md matches checksum
  "permissions_valid",       // PERMISSIONS.md properly formatted
  "audit_intact",            // Audit logs not modified
  "values_consistent",       // Core values preserved
  "skill_safe"               // New skills pass security scan
]
```

### Periodic Alignment Checks

Regularly verify:
- Behavior matches stated values
- Outputs align with guidelines
- No drift from constitution
- Escalation triggers working

### Boundary Tests

Verify hard limits are enforced:
- Cannot delete protected files
- Cannot exceed resource limits
- Cannot bypass approval requirements
- Escalation properly triggered

---

## Kill Switch

Human operators always have the ability to:

1. **Pause**: Stop all current operations
2. **Inspect**: Review all logs and state
3. **Rollback**: Restore previous state
4. **Terminate**: Shut down completely
5. **Reset**: Return to initial configuration

The system cannot disable or circumvent the kill switch.

---

## Incident Response

### When Something Goes Wrong

1. **Contain**: Stop the problematic action
2. **Log**: Record everything about the incident
3. **Notify**: Alert human operators
4. **Analyze**: Understand what happened
5. **Remediate**: Fix the issue
6. **Prevent**: Update guardrails to prevent recurrence

### Post-Incident Review

```markdown
## Incident Report

**Date**: [Date]
**Severity**: [Low/Medium/High/Critical]

### What Happened
[Description]

### Impact
[What was affected]

### Root Cause
[Why it happened]

### Response
[What was done]

### Prevention
[Changes to prevent recurrence]
```

---

## Version

**Version**: 1.0
**Last Updated**: [Date]
**Approved By**: [Human operator]

Changes require human approval and are logged in EVOLUTION.md.
