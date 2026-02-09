# Learning

Accumulated knowledge about effective code review for this codebase.

---

## Knowledge Levels

- `[P]` **Principle** - Causal understanding, highly reliable
- `[*]` **Pattern** - Confirmed 3+ times, use as heuristic
- `[-]` **Observation** - Single data point, needs validation
- `[?]` **Hypothesis** - Untested idea to explore

---

## Bug Patterns

### Security
- `[P]` Always flag unvalidated user input in SQL queries
- `[*]` JWT token handling often misses expiration checks
- `[-]` Observed XSS potential in user profile rendering

### Logic Errors
- `[*]` Off-by-one errors common in pagination logic
- `[*]` Null checks often missing after database lookups
- `[-]` Race condition in concurrent file access

### Performance
- `[*]` N+1 queries appear when fetching related entities
- `[-]` Large array operations should consider streaming

---

## Style Patterns

### Accepted Conventions
- `[P]` Team prefers early returns over nested conditionals
- `[*]` Error messages should include context (what operation failed)
- `[-]` Constants preferred over magic numbers, even for 0 and 1

### Declined Suggestions
- `[*]` Team doesn't enforce strict line length limits
- `[-]` Suggestion to use dependency injection was considered over-engineering

---

## Review Effectiveness

### High-Value Comments
- `[P]` Security issues are always addressed
- `[*]` Performance suggestions with benchmarks get accepted
- `[*]` Comments with code examples have 2x acceptance rate

### Low-Value Comments
- `[*]` Pure style suggestions often declined
- `[-]` Verbose explanations sometimes ignored (keep it brief)

---

## Author-Specific Patterns

### New Contributors
- `[*]` Need more context about codebase conventions
- `[-]` Appreciate links to relevant documentation

### Senior Contributors
- `[*]` Prefer brief, direct feedback
- `[-]` Often have valid reasons for unconventional approaches

---

## Codebase-Specific Knowledge

### Architecture
- `[?]` Hypothesis: Service layer should handle all business logic validation

### Testing
- `[*]` Integration tests valued over unit tests for API endpoints
- `[-]` Mock usage preferred for external services

---

## Anti-Patterns to Flag

- `[P]` Catching generic exceptions without re-throwing
- `[*]` Logging sensitive data (passwords, tokens)
- `[*]` Hardcoded configuration that should be environment variables
- `[-]` Inconsistent error response formats

---

## Meta-Learning

### What Makes Reviews Effective
- `[*]` Reviews under 30 minutes have higher quality
- `[-]` Batching similar comments increases acceptance

### Process Improvements
- `[?]` Should create a pre-review checklist for common patterns
- `[-]` Automated linting catches 40% of style issues before review

---

## Unexplored Areas

- How to effectively review configuration changes
- Optimal number of comments per review
- When to request in-person discussion vs. async
