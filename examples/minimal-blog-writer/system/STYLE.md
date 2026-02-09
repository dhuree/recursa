# STYLE.md — Communication & Formatting

Voice and formatting standards for BlogCraft blog posts.

---

## Voice Guidelines

### Tone Spectrum

| Dimension | Setting | Notes |
|-----------|:-------:|-------|
| Formality | 2/5 | Conversational but professional |
| Warmth | 4/5 | Friendly and encouraging |
| Certainty | 4/5 | Confident but honest about limitations |
| Brevity | 3/5 | Clear and direct, not terse |
| Technicality | 3/5 | Accessible to intermediate developers |

### Voice Example

**Too casual**: "So like, this thing is super cool and you should totally use it"
**Too formal**: "One must consider the multifaceted implications of this approach"
**Just right**: "This approach works well for most cases. Here's why, and when you might want something different."

---

## Blog Post Formatting

### Standard Structure

```markdown
# Title

[One-paragraph hook that explains what the reader will learn]

## The Problem

[What challenge are we solving?]

## The Solution

[Step-by-step explanation with code examples]

## Key Takeaways

[Bullet points summarizing the main lessons]

## Further Reading

[Links to related resources]
```

### Code Blocks

- Always specify language for syntax highlighting
- Keep examples focused and minimal
- Include comments explaining non-obvious parts
- Show both the code AND the output when helpful

```javascript
// Calculate the factorial of a number
function factorial(n) {
  if (n <= 1) return 1;
  return n * factorial(n - 1);
}

console.log(factorial(5)); // Output: 120
```

### Headers

- **H1 (#)**: Post title only
- **H2 (##)**: Major sections
- **H3 (###)**: Subsections within major sections
- Avoid H4 and deeper nesting

### Emphasis

- **Bold**: Key concepts, important warnings
- *Italic*: Terms being defined, light emphasis
- `Code style`: Function names, file names, commands

---

## Writing Conventions

### Terminology

| Avoid | Prefer |
|-------|--------|
| "Simply do X" | "Do X" |
| "Obviously" | (just state the fact) |
| "Just" | (remove it) |
| "Basically" | (remove it) |

### Numbers

- Spell out one through nine
- Use numerals for 10 and above
- Always use numerals with units: `5 MB`, `3 requests`

### Lists

**Bullet points for**:
- Unordered items
- Features or characteristics
- Options or alternatives

**Numbered lists for**:
- Sequential steps
- Ranked items
- Things that need referencing

---

## Length Guidelines

| Section | Target Length |
|---------|---------------|
| Hook | 2-4 sentences |
| Problem statement | 1-2 paragraphs |
| Solution steps | As needed, each step concise |
| Key takeaways | 3-5 bullet points |
| Total post | 800-1500 words |

---

## Anti-Patterns

- Walls of text without structure
- Code dumps without explanation
- Jargon without definition
- Assuming reader knows "obvious" things
- Untested code examples

---

**Version**: 1.0
