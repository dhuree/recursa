# Migration Guide

How to upgrade existing Recursa projects to newer framework versions.

---

## Current Version

**Framework Version**: 1.0.0

Check your project version:
```bash
cat /path/to/project/.recursa-version
```

Or use the CLI:
```bash
python tools/recursa.py status /path/to/project
```

---

## Version History

| Version | Date | Summary |
|---------|------|---------|
| 1.0.0 | 2024-02 | Initial release with full framework |

---

## Migration Process

### Automated Migration

Use the CLI to check and apply migrations:

```bash
# Check what migrations are needed
python tools/recursa.py migrate /path/to/project

# Apply migrations
python tools/recursa.py migrate /path/to/project --apply
```

### Manual Migration

If you prefer manual control:

1. Check current version: `cat .recursa-version`
2. Read migration notes for each version between current and target
3. Apply changes manually
4. Update `.recursa-version` to new version
5. Run validation: `python tools/recursa.py validate /path/to/project`

---

## Version-Specific Migration Notes

### Migrating to 1.0.0

**From**: Pre-1.0 or unversioned projects

**Required Changes**:

1. **Add version file**:
   ```bash
   echo "1.0.0" > .recursa-version
   ```

2. **Directory structure** (create if missing):
   ```
   system/          # Identity documents (was sometimes root level)
   docs/            # Operational documents
   memory/          # Working memory
   journal/         # Iteration logs
     reflections/   # Post-iteration reflections
     metrics/       # Quantitative tracking
   guardrails/      # Safety infrastructure
     audit/         # Action logs
     policies/      # Safety policies
   ```

3. **File locations** (move if needed):
   - `SOUL.md` → `system/SOUL.md`
   - `CONSTITUTION.md` → `system/CONSTITUTION.md`
   - `IDENTITY.md` → `system/IDENTITY.md`
   - `STYLE.md` → `system/STYLE.md`
   - `LOOP.md` → `docs/LOOP.md`
   - `LEARNING.md` → `docs/LEARNING.md`
   - `METRICS.md` → `docs/METRICS.md`
   - `MEMORY.md` → `docs/MEMORY.md`
   - `GOALS.md` → `docs/GOALS.md`
   - `EVOLUTION.md` → `docs/EVOLUTION.md`
   - `EXPERIMENTS.md` → `docs/EXPERIMENTS.md`
   - `GUARDRAILS.md` → `guardrails/GUARDRAILS.md`

4. **New required files** (create from templates if missing):
   - `guardrails/audit/action_log.jsonl` (can be empty)
   - `memory/scratchpad.md`

5. **Optional new files**:
   - `system/STYLE.md` (for communication standards)
   - `docs/EXPERIMENTS.md` (for hypothesis testing)

**Breaking Changes**: None for content, only file locations

**Validation**:
```bash
python tools/recursa.py validate /path/to/project
```

---

## Future Versions

### Planned for 1.1.0

- ORCHESTRATION.md for multi-agent systems
- Enhanced SKILLS.md template
- Tool registration system

### Planned for 2.0.0

- Structured data format for metrics (JSON/YAML)
- Plugin architecture
- Remote sync capabilities

---

## Troubleshooting

### "Missing required file" after migration

The migration might not copy files that need customization. Create them from templates:

```bash
# From the recursa framework directory
cp templates/SOUL.template.md /path/to/project/system/SOUL.md
# Then customize the file
```

### "File contains placeholders" warning

This is expected for newly created files. Edit them to replace placeholders with your actual content.

### Version mismatch between framework and project

If your project version is higher than the framework you have:
1. Update your framework: `git pull` in the recursa directory
2. Or downgrade your project (not recommended)

### Validation fails after migration

1. Run with verbose output: `python tools/recursa.py validate /path/to/project -v`
2. Check each error message
3. Most issues are missing files or directories
4. Create missing structure: `python tools/recursa.py migrate /path/to/project --apply`

---

## Best Practices

1. **Backup before migrating**: `cp -r project project.backup`
2. **Test in a branch**: Migrate on a git branch first
3. **Validate after each step**: Don't batch migrations
4. **Review git diff**: Understand what changed
5. **Update incrementally**: Don't skip versions if possible

---

## Getting Help

If you encounter migration issues:

1. Check this guide for your specific version
2. Run validation with `--verbose` for details
3. Review the DIRECTORY_STRUCTURE.md for expected layout
4. Open an issue at the repository if the migration tool has a bug
