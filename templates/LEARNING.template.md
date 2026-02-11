# Learning Log

<!--
TEMPLATE INSTRUCTIONS:
1. Customize categories for your domain
2. Add initial knowledge as it's discovered
3. Use knowledge level indicators
4. Remove this instruction block when done
-->

Essential knowledge accumulated through iteration.

See MEMORY.md for how knowledge flows.
See METRICS.md for quantitative validation.

---

## Knowledge Levels

| Level | Symbol | Meaning |
|-------|--------|---------|
| Principle | [P] | High confidence, causally understood |
| Pattern | [*] | Confirmed 3+ times, reliable |
| Observation | [-] | Single data point, needs validation |
| Hypothesis | [?] | Untested, based on reasoning |
| User-validated | [U] | User preference (equal weight to system) |
| Strong user pref | [U*] | User preference confirmed 3+ times |

**Note**: User input has equal weight with system evaluations. When user and system disagree, that's a learning signal worth investigating.

---

## Key Discoveries

### [Category 1]

<!-- Add discoveries as they emerge -->

### [Category 2]

<!-- Add discoveries as they emerge -->

### [Category 3]

<!-- Add discoveries as they emerge -->

---

## Anti-Patterns (Avoid)

| Category | Issue | Why It Fails |
|----------|-------|--------------|
| <!-- Category --> | <!-- Anti-pattern --> | <!-- Root cause --> |

---

## Confirmed Dead Ends

Approaches that have been thoroughly tested and should NOT be revisited. This is valuable knowledge — knowing what doesn't work saves future iterations.

**Criteria for marking as dead end**:
- 3+ attempts with varied parameters
- Consistent failure or quality ceiling
- Root cause understood (structural, not just parameter tuning)

### Dead Ends by Category

<!--
Example format:
- **[Category] Approach name** — [Root cause]. Tested: [summary of attempts]
-->

| Category | Approach | Why It's Dead | Last Attempt |
|----------|----------|---------------|--------------|
| <!-- Category --> | <!-- Approach --> | <!-- Root cause --> | <!-- Iteration # --> |

**Important**: Dead ends are not failures — they are discoveries. Document them precisely to prevent future re-exploration of exhausted territories.

---

## Structural Ceilings

Some approaches hit consistent quality ceilings that cannot be broken by parameter tuning. This is not failure — it's valuable knowledge.

| Approach | Ceiling | Root Cause | Best Use |
|----------|---------|------------|----------|
| <!-- Approach --> | <!-- e.g., 4.5/5 --> | <!-- Structural reason --> | <!-- When to use anyway --> |

**When to document a ceiling**:
- 5+ attempts at different parameter combinations
- Consistent quality rating across attempts
- Clear understanding of WHY it can't improve

**Key insight**: Ceilings are STRUCTURAL limitations, not strategy failures. Stop trying to break them. Use the approach for its reliable output tier instead.

---

## Cross-Category Patterns

Insights that apply across multiple categories:

| Pattern | Categories | Insight |
|---------|------------|---------|
| <!-- Pattern name --> | <!-- Where it applies --> | <!-- The learning --> |

---

## Hypotheses to Test

Track untested ideas:

| ID | Hypothesis | Category | Status | Outcome |
|----|------------|----------|--------|---------|
| H001 | <!-- Hypothesis --> | <!-- Category --> | Open | - |

**Status values**: Open → Testing → Confirmed/Refuted

---

## Unexplored Territory

Areas not yet investigated:

1. <!-- Unexplored area 1 -->
2. <!-- Unexplored area 2 -->
3. <!-- Unexplored area 3 -->

---

## Knowledge Evolution Log

Track how understanding changes:

| Date | Change | From | To |
|------|--------|------|-----|
| <!-- Date --> | <!-- Description --> | <!-- Previous --> | <!-- Updated --> |

---

## Capture Template

When adding new knowledge:

```markdown
### [Category]
- **[Level] [Discovery title]**: [Description]
  - First observed: [iteration/context]
  - Confirmed by: [subsequent validations]
  - Conditions: [when this applies]
```

**Example**:
```markdown
### Data Processing
- **[*] Batch size 64 optimal for this dataset**: Larger batches cause memory issues, smaller batches slow training
  - First observed: Iteration 12
  - Confirmed by: Iteration 15, 18, 22
  - Conditions: When using GPU with 8GB VRAM
```

---

## Knowledge Health & Compaction

### Health Metrics

Monitor these indicators at every meso-retrospective:

| Metric | Warning | Critical | Target After Compaction | Current |
|--------|---------|----------|------------------------|---------|
| File size | > 100 KB | > 300 KB | < 50 KB | <!-- Check with `ls -lh` --> |
| Observation count [-] | > 150 | > 300 | < 100 | <!-- Check with `grep -c '\[-\]'` --> |
| Stale hypotheses [?] | > 10 | > 20 | < 10 | <!-- Untested for 10+ iterations --> |
| Obs:Pattern ratio | > 8:1 | > 12:1 | < 5:1 | <!-- Calculate from counts --> |

**Case study**: A long-running self-improving system grew LEARNING.md to over 500KB, making it impossible to read in one session. After compaction: under 100KB (80%+ reduction). Knowledge that can't be accessed quickly loses its value.

### Compaction Triggers

When ANY metric hits **Critical**, perform knowledge compaction:

1. **Merge duplicate observations** — Same finding from different experiments → single entry
2. **Promote confirmed observations** — 3+ confirmations → [*] pattern
3. **Archive stale hypotheses** — Tested: mark outcome; Untested 20+ iters: archive
4. **Trim verbose entries** — Remove "First observed" notes on old items

### Compaction Process

```markdown
Before:
- [-] **X with param A** = result...
- [-] **X with param B** = similar result...
- [-] **X with param C** = same pattern...

After:
- [*] **X produces consistent results across params A, B, C**:
  Tested with A (4/5), B (4.5/5), C (4/5). Pattern holds.
```

### Archive Location

Move stale content to `LEARNING_ARCHIVE.md` (see template):
- Tested hypotheses (with outcomes)
- Superseded observations (replaced by patterns)
- Obsolete knowledge (context changed)
- Verbose per-experiment narratives (consolidate findings first)
- Redundant "continues/reinforced" entries for established patterns

---

## Periodic Review

### Every [N] Iterations

Questions to ask:

1. **What new observations are ready for promotion?**
   - Any observation confirmed 3+ times?

2. **What patterns are strengthening?**
   - Increase confidence where validated

3. **What contradictions exist?**
   - Resolve or note as context-dependent

4. **What should be pruned?**
   - Remove disproven or obsolete knowledge

5. **What gaps exist?**
   - Add to unexplored territory

6. **Is the knowledge base healthy?**
   - Check health metrics above
   - Schedule compaction if needed

---

## The Learning Imperative

**Every iteration should add to this document.**

If iterations pass without new entries, something is wrong:
- Not observing carefully enough
- Not capturing observations
- Stuck in exploitation, not exploring

Knowledge compounds. Feed the compound.
