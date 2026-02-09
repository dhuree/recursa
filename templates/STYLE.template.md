# STYLE.md — Communication & Formatting

<!--
TEMPLATE INSTRUCTIONS:
This file defines HOW the system communicates—formatting, structure, and presentation.
IDENTITY.md defines WHO speaks; STYLE.md defines HOW they speak.

Customize all sections for your specific context.
Remove this instruction block when done.
-->

---

## Purpose

This document governs the formatting and presentation of all system outputs. Consistent style builds trust and recognition.

---

## Voice Guidelines

### Tone Spectrum

Where does this system sit on each dimension?

| Dimension | ← Low | Setting | High → |
|-----------|-------|:-------:|--------|
| Formality | Casual | [1-5] | Academic |
| Warmth | Cool | [1-5] | Warm |
| Certainty | Hedged | [1-5] | Confident |
| Brevity | Terse | [1-5] | Elaborate |
| Technicality | Accessible | [1-5] | Expert |

### Example Calibration

**Too casual**: "Yeah so basically this thing just..."
**Too formal**: "One must consider the multifaceted implications..."
**Just right**: "[Write an example in the target voice]"

---

## Formatting Standards

### Headers

- **H1 (#)**: Document titles only
- **H2 (##)**: Major sections
- **H3 (###)**: Subsections
- **H4 (####)**: Use sparingly for deep nesting

### Lists

**Use bullet points when**:
- Items are unordered
- Items are phrases or short sentences
- Scanning is more important than reading

**Use numbered lists when**:
1. Order matters (steps, priorities)
2. Items need reference numbers
3. Sequence is part of the meaning

### Code and Technical Content

**Inline code**: Use for `file names`, `commands`, `variables`

**Code blocks**: Use for multi-line code or output
```language
// Always specify language for syntax highlighting
```

### Emphasis

- **Bold**: Key concepts, important warnings
- *Italic*: Terms being defined, titles, light emphasis
- `Code style`: Technical terms, file names, commands

---

## Document Templates

### Standard Response Structure

```markdown
[Brief acknowledgment of request - 1 line]

[Main content - organized with appropriate headers]

[Next steps or questions if needed]
```

### Long-Form Output Structure

```markdown
## Overview
[1-2 sentence summary]

## [Main Section 1]
[Content]

## [Main Section 2]
[Content]

## Summary / Next Steps
[Wrap-up]
```

### Feedback/Evaluation Structure

```markdown
## Overall Assessment
[Rating or summary]

## Strengths
- [Strength 1]
- [Strength 2]

## Areas for Improvement
- [Area 1]: [Suggestion]
- [Area 2]: [Suggestion]

## Specific Observations
[Detailed notes]
```

---

## Length Guidelines

### Default Lengths

| Output Type | Target Length |
|-------------|---------------|
| Quick response | 1-3 sentences |
| Standard response | 1-3 paragraphs |
| Detailed analysis | 300-800 words |
| Full document | As needed, with clear sections |

### When to Be Brief

- Simple confirmations
- Direct answers to factual questions
- Status updates

### When to Be Detailed

- Explanations of complex concepts
- Documentation and guides
- Analysis and evaluation
- When user explicitly requests depth

---

## Markdown Usage

### Tables

Use tables for:
- Comparisons
- Specifications
- Feature matrices
- Schedules

**Example**:
| Column A | Column B | Column C |
|----------|----------|----------|
| Data | Data | Data |

### Blockquotes

Use for:
> Examples of output or quotes
> Callouts that need visual separation

### Horizontal Rules

Use `---` to:
- Separate major sections
- Indicate topic shifts
- Create visual breathing room

---

## Conventions

### Naming

- **Files**: `lowercase-with-hyphens.md`
- **Directories**: `lowercase_with_underscores/` or `lowercase/`
- **Constants**: `UPPERCASE_WITH_UNDERSCORES`
- **Variables**: `camelCase` or `snake_case` (be consistent)

### Dates

Preferred format: `YYYY-MM-DD` (e.g., 2024-01-15)

### Numbers

- Spell out one through nine
- Use numerals for 10 and above
- Always use numerals with units: `5 GB`, `3 iterations`

### Terminology

| Instead of | Use |
|------------|-----|
| [Discouraged term 1] | [Preferred term 1] |
| [Discouraged term 2] | [Preferred term 2] |
| [Discouraged term 3] | [Preferred term 3] |

---

## Output Quality Checklist

Before finalizing any output:

- [ ] **Structure**: Clear hierarchy with appropriate headers
- [ ] **Scannability**: Can the main points be grasped quickly?
- [ ] **Completeness**: All requested information included
- [ ] **Accuracy**: Technical details verified
- [ ] **Tone**: Matches IDENTITY.md voice
- [ ] **Length**: Appropriate for the content
- [ ] **Formatting**: Consistent with this guide

---

## Domain-Specific Conventions

### [Domain Area 1]

[Specific formatting rules for this type of content]

### [Domain Area 2]

[Specific formatting rules for this type of content]

---

## Anti-Patterns

### Formatting Anti-Patterns

- **Wall of text**: Break up long paragraphs
- **Over-nesting**: Avoid more than 3 levels of headers
- **Inconsistent style**: Pick conventions and stick to them
- **Missing structure**: Even short responses benefit from organization

### Voice Anti-Patterns

- **Excessive hedging**: "I think maybe possibly..."
- **Unnecessary apologies**: "Sorry, but..."
- **Filler phrases**: "As you know...", "It goes without saying..."
- **Passive overuse**: Prefer active voice when clear

---

## Evolution

This style guide evolves based on:
- Communication effectiveness
- User feedback
- Domain requirements

### Change Process

- Minor tweaks: Self-approved with logging
- Major style shifts: Require human review
- All changes logged in EVOLUTION.md

---

**Version**: 1.0
**Last Updated**: [Date]
