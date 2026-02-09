# Learning Log

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

---

## Key Discoveries

### Structure & Organization

- **[*] Start with the problem, not the solution**: Readers engage when they recognize their pain point upfront
  - First observed: Post 3
  - Confirmed by: Posts 5, 8, 12
  - Conditions: Works for all technical content

- **[-] Keep introductions under 100 words**: Longer intros lose readers before the content
  - First observed: Post 7 (analytics showed drop-off)
  - Needs validation: Track on next 3 posts

### Code Examples

- **[P] Test code in isolation before embedding**: Code that works in your project may fail for readers missing dependencies
  - First observed: Post 2 (reader reported error)
  - Confirmed by: Many subsequent posts
  - Conditions: Always applies

- **[*] Show the error before the fix**: Readers learn better when they see what goes wrong
  - First observed: Post 4
  - Confirmed by: Posts 9, 15
  - Conditions: When explaining debugging or common mistakes

### Engagement

- **[-] Analogies to everyday objects increase comprehension**: Comparing Redis to a "scratch pad on your desk" worked well
  - First observed: Post 11
  - Needs validation: Try more analogies

### Writing Process

- **[?] Outline for 30 min before writing produces faster drafts**: Hypothesis based on one experience
  - Status: Testing
  - Conditions: For posts over 1500 words

---

## Anti-Patterns (Avoid)

| Category | Issue | Why It Fails |
|----------|-------|--------------|
| Code | Pseudocode without real examples | Readers can't verify it works |
| Structure | Burying the lede | Readers leave before value |
| Tone | "Simply" or "obviously" | Alienates learners |
| Length | 3000+ words without breaks | Reader fatigue |
| Testing | Testing in your IDE only | Missing dependencies not caught |

---

## Cross-Category Patterns

| Pattern | Categories | Insight |
|---------|------------|---------|
| Show before tell | Code, Structure | Demonstrate the outcome, then explain how |
| Respect reader time | Length, Structure | Dense > lengthy |
| Verify everything | Code, Accuracy | If you didn't test it, assume it's wrong |

---

## Hypotheses to Test

| ID | Hypothesis | Category | Status | Outcome |
|----|------------|----------|--------|---------|
| H001 | Posts with GIFs get more shares | Engagement | Open | - |
| H002 | Numbered lists outperform bullets for steps | Structure | Testing | - |
| H003 | Morning writing produces higher quality | Process | Open | - |

**Status values**: Open → Testing → Confirmed/Refuted

---

## Unexplored Territory

1. Video embeds vs. static code blocks
2. Interactive code playgrounds
3. Series vs. standalone posts
4. Guest expert interviews
5. "What I got wrong" retrospective posts

---

## Knowledge Evolution Log

| Date | Change | From | To |
|------|--------|------|-----|
| - | - | - | - |

---

## The Learning Imperative

**Every post should add to this document.**

If posts pass without new entries, something is wrong:
- Not observing carefully enough
- Not capturing observations
- Stuck in exploitation, not exploring

Knowledge compounds. Feed the compound.
