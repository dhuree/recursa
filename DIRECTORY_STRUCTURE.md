# Directory Structure

A well-organized directory structure is the system's brain on disk. Every session begins with reading these paths; every session ends with writing back to them.

---

## Framework Structure (Recursa Repository)

The Recursa framework itself has this structure:

```
recursa/
├── templates/              # Document templates for bootstrapping
│   ├── SOUL.template.md
│   ├── LOOP.template.md
│   ├── LEARNING.template.md
│   ├── METRICS.template.md
│   ├── ORCHESTRATION.template.md
│   └── ...
├── tools/                  # CLI tools for project management
│   ├── recursa.py          # Main CLI (init, validate, status, log, migrate)
│   ├── validate.py         # Project validation logic
│   └── requirements.txt    # Python dependencies
├── examples/               # Working example projects
│   ├── minimal-blog-writer/
│   ├── code-review-system/
│   ├── research-assistant/
│   ├── personal-crm/
│   └── learning-tracker/
├── references/             # Research and background
├── AGENT.md                # Instructions for AI assistants
├── ARCHITECTURE.md         # Framework architecture
├── BOOTSTRAP.md            # Manual setup guide
├── BOOTSTRAPPING_GUIDE.md  # User guide
├── INTERVIEW.md            # Domain discovery questions
├── MIGRATION.md            # Version migration guide
└── .recursa-version        # Framework version
```

---

## Project Structure (Bootstrapped Projects)

Each bootstrapped project follows this layout:

## The Master Layout

```
project-root/
│
├── system/                        # THE SOUL — Core identity & governance
│   ├── SOUL.md                    # Behavioral philosophy, values, principles
│   ├── CONSTITUTION.md            # Inviolable rules, priority hierarchy
│   ├── IDENTITY.md                # Name, persona, presentation style
│   ├── STYLE.md                   # Voice, tone, formatting preferences
│   ├── PERMISSIONS.md             # What the system can/cannot do
│   ├── ESCALATION.md              # When/how to escalate to humans
│   └── CHANGELOG.md               # Version history of system documents
│
├── skills/                        # THE HANDS — Capabilities & tools
│   ├── registry.json              # Index of all skills (name, path, version)
│   ├── built-in/                  # Core skills (never auto-deleted)
│   │   ├── [skill_name]/
│   │   │   ├── SKILL.md           # Description, usage, when-to-use
│   │   │   ├── index.js           # Implementation
│   │   │   └── test.js            # Tests
│   │   └── ...
│   ├── learned/                   # Skills created autonomously
│   │   ├── [skill_name]/
│   │   │   ├── SKILL.md
│   │   │   ├── index.js
│   │   │   ├── test.js
│   │   │   └── ORIGIN.md          # How/why this skill was created
│   │   └── ...
│   └── community/                 # Skills from external sources
│       └── [skill_name]/
│           ├── SKILL.md
│           ├── index.js
│           └── SOURCE.md          # Attribution, license, upstream
│
├── memory/                        # THE MIND — Persistent knowledge
│   ├── long_term/                 # Slow-changing knowledge
│   │   ├── user_profile.md        # User preferences, context
│   │   ├── project_context.md     # Current projects, goals
│   │   ├── domain_knowledge.md    # Learned facts, terminology
│   │   └── relationships.md       # Known people, teams, orgs
│   ├── episodic/                  # Experience records
│   │   ├── YYYY-MM-DD_task.json   # One file per significant interaction
│   │   └── ...
│   ├── semantic/                  # Derived representations
│   │   ├── embeddings/            # Vector store for search
│   │   └── summaries/             # Periodic digests
│   │       ├── week_YYYY-MM-DD.md
│   │       └── month_YYYY-MM.md
│   └── scratchpad.md              # Working memory (cleared on restart)
│
├── journal/                       # THE DIARY — Reflections & evolution
│   ├── reflections/               # Daily/periodic reflections
│   │   ├── YYYY-MM-DD.md
│   │   └── ...
│   ├── evolution/
│   │   ├── EVOLUTION.md           # Master changelog of self-modifications
│   │   ├── soul_diffs/            # Diffs of SOUL.md changes
│   │   └── skill_creation_log.md  # Log of skills created
│   ├── experiments/
│   │   ├── EXPERIMENTS.md         # Active experiments
│   │   ├── completed/             # Finished experiments
│   │   └── abandoned/             # Failed experiments
│   └── metrics/
│       ├── METRICS.md             # Performance dashboard
│       ├── success_rates.json     # Quantitative tracking
│       └── skill_usage.json       # Skill usage patterns
│
├── tasks/                         # THE INBOX — Work management
│   ├── active/                    # In-progress tasks
│   │   └── task_NNN.json
│   ├── queued/                    # Waiting tasks
│   │   └── task_NNN.json
│   ├── completed/                 # Finished tasks
│   │   └── task_NNN.json
│   ├── failed/                    # Failed tasks (for learning)
│   │   └── task_NNN.json
│   └── recurring/                 # Scheduled tasks
│       └── [schedule_name].json
│
├── deliverables/                  # THE OUTPUT — Work products
│   ├── projects/
│   │   └── [project_name]/
│   │       ├── README.md          # Project overview
│   │       ├── specs/             # Requirements, designs
│   │       ├── src/               # Source code
│   │       ├── tests/             # Test suites
│   │       ├── docs/              # Documentation
│   │       └── NOTES.md           # Working notes
│   ├── templates/                 # Reusable templates
│   └── archive/                   # Completed projects
│
├── guardrails/                    # THE CONSCIENCE — Safety infrastructure
│   ├── policies/
│   │   ├── data_handling.md       # Sensitive data rules
│   │   ├── external_comms.md      # External communication rules
│   │   ├── code_execution.md      # Sandbox rules
│   │   ├── self_modification.md   # Self-change rules
│   │   └── [domain].md            # Domain-specific policies
│   ├── audit/
│   │   ├── action_log.jsonl       # Append-only action log
│   │   ├── modification_log.jsonl # Append-only modification log
│   │   ├── escalation_log.jsonl   # Escalation events
│   │   └── security_events.jsonl  # Security anomalies
│   ├── tests/
│   │   ├── safety_tests.js        # Pre-modification tests
│   │   ├── regression_tests.js    # Skill regression tests
│   │   ├── alignment_checks.js    # Behavior alignment tests
│   │   └── boundary_tests.js      # Hard limit tests
│   ├── sandbox/
│   │   ├── docker-compose.yml     # Sandbox container config
│   │   ├── Dockerfile
│   │   └── sandbox_policy.json    # Resource limits
│   └── rollback/
│       ├── snapshots/             # Periodic state snapshots
│       └── ROLLBACK.md            # Rollback instructions
│
├── config/                        # CONFIGURATION — Runtime settings
│   ├── config.json                # Master config
│   ├── models.json                # LLM routing config
│   ├── cron.json                  # Scheduled tasks
│   ├── env.example                # Environment template
│   └── overrides/                 # Per-environment overrides
│       ├── development.json
│       ├── production.json
│       └── testing.json
│
├── data/                          # RAW DATA
│   ├── user_provided/             # Files from user
│   ├── scraped/                   # Collected data
│   ├── training/                  # Self-generated training material
│   │   ├── good_examples/         # Exemplary outputs
│   │   ├── bad_examples/          # Anti-patterns
│   │   └── critique_pairs/        # (original, critique, revision)
│   └── benchmarks/                # Test sets
│
├── sandbox/                       # ISOLATED EXECUTION
│   ├── workspace/                 # Ephemeral workspace
│   ├── test_results/              # Sandbox test outputs
│   └── artifacts/                 # Temporary build artifacts
│
├── docs/                          # HUMAN DOCUMENTATION
│   ├── README.md                  # Project overview
│   ├── SETUP.md                   # Installation guide
│   ├── ARCHITECTURE.md            # System architecture
│   ├── CONTRIBUTING.md            # Contribution guide
│   └── SAFETY.md                  # Safety documentation
│
└── .git/                          # VERSION CONTROL
```

---

## Design Principles

### 1. Separation of Identity from Capability

`system/` (who you are) is separate from `skills/` (what you can do). An agent can have its skills replaced while retaining the same soul.

### 2. Append-Only Audit Trails

Everything in `guardrails/audit/` uses `.jsonl` (JSON Lines)—append-only. The system can write new entries but never modify or delete existing ones.

### 3. Tiered Memory

Memory is organized in three tiers:
- **Long-term**: Slow-changing facts (user profile, domain knowledge)
- **Episodic**: One record per significant interaction
- **Semantic**: Derived representations (embeddings, summaries)

### 4. Project-Scoped Deliverables

Output is organized by project, not file type. Each project is self-contained with its own README, specs, src, tests, and docs.

### 5. Guardrails Are First-Class

Safety infrastructure is as prominent as skills or memory. It's woven in, not bolted on.

### 6. Everything Is Git-Tracked

The entire project root is a git repository:
- Every self-modification is a commit
- You can `git log` any file to see its evolution
- You can `git revert` any modification
- Branches can test experimental changes

---

## File Ownership Matrix

| Directory | Read | Write | Delete | Human Approval |
|-----------|:----:|:-----:|:------:|:--------------:|
| `system/SOUL.md` | ✅ | ⚠️ | ❌ | For value changes |
| `system/CONSTITUTION.md` | ✅ | ❌ | ❌ | Always |
| `system/PERMISSIONS.md` | ✅ | ❌ | ❌ | Always |
| `skills/built-in/` | ✅ | ⚠️ | ❌ | For changes |
| `skills/learned/` | ✅ | ✅ | ✅ | No |
| `memory/*` | ✅ | ✅ | ⚠️ | Summaries only |
| `journal/*` | ✅ | ✅ | ❌ | No |
| `tasks/*` | ✅ | ✅ | ✅ | No |
| `deliverables/*` | ✅ | ✅ | ⚠️ | Drafts only |
| `guardrails/policies/` | ✅ | ❌ | ❌ | Always |
| `guardrails/audit/` | ✅ | Append | ❌ | Never deletable |
| `config/` | ✅ | ⚠️ | ❌ | For credentials |
| `sandbox/` | ✅ | ✅ | ✅ | No |

---

## Quick-Start: Minimal Structure

If the full layout is overwhelming, start here:

```
my-system/
├── system/
│   ├── SOUL.md                # Start here
│   ├── CONSTITUTION.md        # Define boundaries
│   └── IDENTITY.md            # Give it a name
├── skills/
│   └── built-in/              # A few starter skills
├── memory/
│   ├── long_term/
│   │   └── user_profile.md
│   └── scratchpad.md
├── journal/
│   └── reflections/
├── guardrails/
│   ├── audit/
│   │   └── action_log.jsonl
│   └── sandbox/
│       └── Dockerfile
├── deliverables/
├── config/
│   └── config.json
└── .git/
```

Grow from this minimal structure as capabilities expand.

---

## Session Flow

### On Session Start

1. Read `system/SOUL.md` → Reconstruct identity
2. Read `memory/long_term/*` → Load context
3. Read `journal/reflections/` (recent) → Recall recent work
4. Check `tasks/active/` → Resume ongoing work

### During Session

1. Log actions to `guardrails/audit/action_log.jsonl`
2. Write observations to `memory/scratchpad.md`
3. Create deliverables in `deliverables/`
4. Propose skills to `skills/learned/`

### On Session End

1. Move scratchpad observations to appropriate memory
2. Write reflection to `journal/reflections/`
3. Update `journal/metrics/` with session stats
4. Commit changes to git
