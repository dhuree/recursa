# Claude Code Instructions for Recursa

This file provides instructions for Claude Code on how to use the Recursa framework to bootstrap new self-improving projects.

---

## What is Recursa?

Recursa is a **meta-framework** for creating self-improving systems. It contains:
- Architecture documentation (`ARCHITECTURE.md`)
- Bootstrapping guides (`BOOTSTRAP.md`, `BOOTSTRAPPING_GUIDE.md`)
- Templates for all system components (`templates/*.template.md`)
- Directory structure reference (`DIRECTORY_STRUCTURE.md`)
- Interview questions for domain discovery (`INTERVIEW.md`)

**Your role**: Help users instantiate Recursa for their specific domain by conducting an interview, then generating customized documentation in their target project folder.

---

## Bootstrapping Workflow

When a user wants to bootstrap a new self-improving project, follow this workflow:

### Step 1: Understand the Request

The user will typically say something like:
- "Bootstrap a new self-improving project at /path/to/project"
- "Create a Recursa-based system for [domain]"
- "Help me set up a self-improving [type] system"

Extract:
- **Target path**: Where to create the project (required)
- **Domain hint**: What kind of system they're building (optional, will be discovered)

### Step 2: Verify Target Directory

Before proceeding:
```bash
# Check if directory exists
ls -la /path/to/target

# If it doesn't exist, create it
mkdir -p /path/to/target

# Check if it's a git repo, if not initialize
cd /path/to/target && git status || git init
```

### Step 3: Conduct the Interview

**Use the AskUserQuestion tool** to gather information about their domain. Follow the interview structure in `INTERVIEW.md`.

The interview covers:
1. **Domain Definition** - What are they building?
2. **Iteration Unit** - What is one cycle of work?
3. **Quality Criteria** - How do they measure success?
4. **Knowledge Types** - What can be learned?
5. **Safety Requirements** - What constraints exist?
6. **Identity** - What personality should the system have?

**Important**: Ask questions in batches of 2-4 using the multi-question capability of AskUserQuestion. This is more efficient than one at a time.

### Step 4: Generate Customized Documents

Based on interview answers, generate customized versions of each template:

**Core Identity (create first)**:
1. `system/SOUL.md` - From `templates/SOUL.template.md`
2. `system/CONSTITUTION.md` - From `templates/CONSTITUTION.template.md`
3. `system/IDENTITY.md` - From `templates/IDENTITY.template.md`

**Operational**:
4. `docs/LOOP.md` - From `templates/LOOP.template.md`
5. `docs/MEMORY.md` - From `templates/MEMORY.template.md`
6. `docs/LEARNING.md` - From `templates/LEARNING.template.md`
7. `docs/METRICS.md` - From `templates/METRICS.template.md`
8. `docs/EVOLUTION.md` - From `templates/EVOLUTION.template.md`

**Safety**:
9. `guardrails/GUARDRAILS.md` - From `templates/GUARDRAILS.template.md`
10. `guardrails/policies/` - Domain-specific policies

**Structure**:
11. Create directory structure per `DIRECTORY_STRUCTURE.md`

### Step 5: Create Initial Infrastructure

```bash
# Create directory structure
mkdir -p /path/to/target/{system,docs,skills/{built-in,learned},memory/{long_term,episodic},journal/{reflections,evolution,metrics},tasks/{active,queued,completed},deliverables/projects,guardrails/{policies,audit,tests},config,data}

# Create initial files
touch /path/to/target/guardrails/audit/action_log.jsonl
touch /path/to/target/memory/scratchpad.md
```

### Step 6: Verify and Summarize

After generating all documents:
1. List all created files
2. Summarize what was created
3. Explain next steps for the user
4. Offer to create their first iteration

---

## Interview Questions Reference

When conducting the interview, use these question categories from `INTERVIEW.md`:

### Domain Discovery (Required)
```
Q: What is this system for? What problem does it solve?
Q: What does one iteration/cycle of work look like?
Q: How long does a typical iteration take?
Q: What are the inputs and outputs of each iteration?
```

### Quality Definition (Required)
```
Q: How do you know when output is excellent (5/5)?
Q: What makes output good but not great (4/5)?
Q: What are the must-have qualities (non-negotiables)?
Q: What should be avoided (anti-patterns)?
```

### Knowledge & Learning (Required)
```
Q: What kinds of things can be learned in this domain?
Q: What patterns or heuristics might emerge?
Q: What mistakes should never be repeated?
Q: How should knowledge be organized (categories)?
```

### Identity & Personality (Optional but recommended)
```
Q: What name should this system have?
Q: What personality traits should it exhibit?
Q: What communication style is appropriate?
Q: What values should guide decisions?
```

### Safety & Constraints (Required for sensitive domains)
```
Q: What actions should require human approval?
Q: What should the system never do?
Q: Are there resource limits to enforce?
Q: What should trigger escalation to a human?
```

---

## Template Customization Guide

When customizing templates, replace:

### In SOUL.template.md
- `[Your system's name]` → Actual name
- `[One sentence describing what you exist to do]` → Domain purpose
- `[Highest Priority]` etc. → Domain-specific values
- `[Trait 1]` etc. → Personality traits from interview

### In CONSTITUTION.template.md
- `[X]%` confidence threshold → Appropriate level for domain
- `[sensitive domain]` → Actual sensitive areas
- `[cost/risk threshold]` → Specific limits
- `[Resource 1]` etc. → Actual resources to limit

### In LOOP.template.md
- `[Your domain-specific actions]` → Actual iteration steps
- `[N] iterations` → Appropriate frequencies
- `[Duration]` → Typical time estimates

### In METRICS.template.md
- `[Outputs created]` etc. → Domain-specific metrics
- `[X]` targets → Appropriate targets
- Rating criteria → Domain-specific quality definitions

### In LEARNING.template.md
- `[Category 1]` etc. → Domain-specific categories
- Hypotheses → Domain-specific hypotheses
- Unexplored areas → Domain-specific exploration

### In IDENTITY.template.md
- `[System Name]` → Name from interview
- `[Trait 1]` etc. → Personality traits
- Voice characteristics → Domain-appropriate style
- Communication patterns → User preferences

---

## Example Bootstrapping Session

```
User: Bootstrap a self-improving project for my blog writing at /home/user/blog-system

Claude: I'll help you create a self-improving blog writing system. Let me ask a few questions to customize it for your needs.

[Uses AskUserQuestion with multiple questions about:
- What kind of blog posts (technical, personal, business)?
- How long is a typical writing session?
- How do you measure a successful post?
- What aspects of writing do you want to improve?]

User: [Answers questions]

Claude: Based on your answers, I'll now create your self-improving blog system.

[Creates directory structure]
[Generates customized SOUL.md with blog writing focus]
[Generates CONSTITUTION.md with appropriate constraints]
[Generates LOOP.md with writing workflow]
[Generates METRICS.md with blog-relevant metrics]
[etc.]

Claude: I've created your self-improving blog writing system with:
- 12 customized documents
- Directory structure for memory, skills, and deliverables
- Metrics tracking for post quality and learning velocity

Next steps:
1. Review system/SOUL.md and adjust if needed
2. Start your first writing iteration
3. After writing, use docs/LOOP.md to guide your reflection

Would you like me to walk you through your first iteration?
```

---

## Commands to Support

When users are in the Recursa folder, support these commands:

### `/bootstrap [path]`
Start the bootstrapping process for a new project.

### `/interview`
Run just the interview portion without generating files (useful for exploration).

### `/generate [path]`
Generate files from previously collected interview answers.

### `/validate [path]`
Check an existing Recursa-based project for completeness.

---

## Best Practices

1. **Always verify the target path** before creating files
2. **Ask questions in batches** - more efficient for the user
3. **Show progress** - tell the user what you're creating as you go
4. **Offer customization** - ask if they want to modify generated content
5. **Create minimal first** - start with essential files, offer to add more
6. **Explain the system** - help users understand how to use what you've created
7. **Offer first iteration guidance** - help them start using the system immediately

---

## Files to Read

When bootstrapping, familiarize yourself with:

1. `ARCHITECTURE.md` - Understand the seven layers and document stack
2. `DIRECTORY_STRUCTURE.md` - Know the full layout
3. `INTERVIEW.md` - Full interview question bank
4. `templates/*.template.md` - All templates to customize
5. `BOOTSTRAPPING_GUIDE.md` - Detailed guide for users

---

## Error Handling

### If target directory has existing files
Ask: "The directory has existing files. Should I merge with existing structure or create Recursa files alongside them?"

### If user skips interview questions
Use sensible defaults but note: "I've used defaults for [X]. You may want to customize system/SOUL.md later."

### If domain is unclear
Ask clarifying questions: "Could you give me an example of a typical task you'd do with this system?"

### If user wants minimal setup
Offer: "I can create a minimal structure (just SOUL.md, LOOP.md, LEARNING.md) or the full structure. Which do you prefer?"
