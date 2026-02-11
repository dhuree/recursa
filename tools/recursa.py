#!/usr/bin/env python3
"""
Recursa CLI

Command-line interface for managing Recursa self-improving projects.
"""

import os
import sys
import json
import shutil
from datetime import datetime
from pathlib import Path
from typing import Optional

# Add tools directory to path for imports
sys.path.insert(0, str(Path(__file__).parent))

from validate import validate_project, print_result

# Current framework version
FRAMEWORK_VERSION = "1.0.0"

# Minimal directory structure
MINIMAL_STRUCTURE = [
    "system",
    "docs",
    "memory",
    "user-inputs",
    "journal",
    "journal/reflections",
    "journal/metrics",
    "guardrails",
    "guardrails/audit",
    "guardrails/policies",
]

# Minimal files to create
MINIMAL_FILES = {
    "system/ORIGIN.md": """# Origin

Bootstrap context and foundational purpose.

## Bootstrap Date
**Created**: [DATE]
**Framework Version**: 1.0.0

## Core Purpose
[What is this system for? What problem does it solve?]

## Domain
[What domain/field does this operate in?]

## Iteration Unit
[What is one cycle of work?]

## Quality Criteria
[What makes output excellent?]

## Original Prompt
> [The bootstrap request that started this project]

## Interview Summary
[Key answers from the bootstrap interview]
""",
    "system/SOUL.md": """# Soul

## Identity
[Your system's name and purpose]

## Core Values
1. [Value 1]
2. [Value 2]
3. [Value 3]

## Personality
- [Trait 1]
- [Trait 2]
""",
    "docs/LOOP.md": """# Iteration Loop

## Phases

### 1. PREPARE
- Review goals and context
- Gather inputs

### 2. EXECUTE
- [Your domain-specific actions]

### 3. EVALUATE
- Assess output quality
- Rate 1-5

### 4. CAPTURE
- Record learnings
- Update metrics
""",
    "docs/LEARNING.md": """# Learning

## Knowledge Levels
- `[P]` Principle - Causal understanding
- `[*]` Pattern - Confirmed 3+ times
- `[-]` Observation - Single data point
- `[?]` Hypothesis - Untested

## Discoveries

### [Category 1]
- [?] [Your first hypothesis]

### [Category 2]
- [?] [Your first hypothesis]
""",
    "docs/METRICS.md": """# Metrics

## Quality Scale
| Rating | Meaning |
|--------|---------|
| 5/5 | Exceptional |
| 4/5 | Strong |
| 3/5 | Adequate |
| 2/5 | Weak |
| 1/5 | Failed |

## Tracking

### Iteration Log
| # | Date | Quality | Notes |
|---|------|---------|-------|
| 1 | | | |
""",
    "memory/scratchpad.md": """# Scratchpad

Working notes for current session.

---

""",
    "guardrails/audit/action_log.jsonl": "",
    ".recursa-version": FRAMEWORK_VERSION,
}


def get_iteration_count(project_path: Path) -> int:
    """Get the current iteration count from metrics or journal."""
    # Try to read from a state file first
    state_file = project_path / ".recursa-state.json"
    if state_file.exists():
        try:
            state = json.loads(state_file.read_text())
            return state.get("iteration_count", 0)
        except Exception:
            pass

    # Fall back to counting journal entries
    reflections_dir = project_path / "journal" / "reflections"
    if reflections_dir.exists():
        return len(list(reflections_dir.glob("*.md")))

    return 0


def get_last_activity(project_path: Path) -> Optional[str]:
    """Get the timestamp of the last activity."""
    state_file = project_path / ".recursa-state.json"
    if state_file.exists():
        try:
            state = json.loads(state_file.read_text())
            return state.get("last_activity")
        except Exception:
            pass

    # Fall back to most recent file modification
    latest_time = None
    for pattern in ["docs/*.md", "journal/**/*.md", "memory/*.md"]:
        for f in project_path.glob(pattern):
            mtime = f.stat().st_mtime
            if latest_time is None or mtime > latest_time:
                latest_time = mtime

    if latest_time:
        return datetime.fromtimestamp(latest_time).isoformat()
    return None


def cmd_init(args):
    """Initialize a new Recursa project."""
    project_path = Path(args.path).resolve()

    if project_path.exists() and any(project_path.iterdir()):
        if not args.force:
            print(f"Error: Directory is not empty: {project_path}")
            print("Use --force to initialize anyway (may overwrite files)")
            return 1

    print(f"Initializing Recursa project at: {project_path}")

    # Create directories
    for dir_path in MINIMAL_STRUCTURE:
        (project_path / dir_path).mkdir(parents=True, exist_ok=True)
        print(f"  Created: {dir_path}/")

    # Create files
    for file_path, content in MINIMAL_FILES.items():
        full_path = project_path / file_path
        if not full_path.exists() or args.force:
            full_path.write_text(content)
            print(f"  Created: {file_path}")

    # Create .gitkeep files for empty directories
    for dir_path in ["journal/reflections", "journal/metrics", "guardrails/policies"]:
        gitkeep = project_path / dir_path / ".gitkeep"
        if not gitkeep.exists():
            gitkeep.touch()

    print(f"\nProject initialized successfully!")
    print(f"\nNext steps:")
    print(f"  1. Edit system/SOUL.md to define your system's identity")
    print(f"  2. Edit docs/LOOP.md to define your iteration process")
    print(f"  3. Start your first iteration!")
    return 0


def cmd_validate(args):
    """Validate a Recursa project."""
    result = validate_project(args.path, strict=args.strict)
    print_result(result, verbose=args.verbose)
    return 0 if result.is_valid else 1


def cmd_status(args):
    """Show project status."""
    project_path = Path(args.path).resolve()

    if not project_path.exists():
        print(f"Error: Project not found: {project_path}")
        return 1

    print(f"\n{'='*50}")
    print(f"RECURSA PROJECT STATUS")
    print(f"{'='*50}")
    print(f"Project: {project_path.name}")
    print(f"Path: {project_path}")

    # Version
    version_file = project_path / ".recursa-version"
    if version_file.exists():
        version = version_file.read_text().strip()
        print(f"Version: {version}")
        if version != FRAMEWORK_VERSION:
            print(f"  (Latest: {FRAMEWORK_VERSION} - run 'recursa migrate' to update)")
    else:
        print(f"Version: Unknown (no .recursa-version file)")

    # Iteration count
    iteration_count = get_iteration_count(project_path)
    print(f"Iterations: {iteration_count}")

    # Last activity
    last_activity = get_last_activity(project_path)
    if last_activity:
        print(f"Last Activity: {last_activity}")

    # Quick validation
    result = validate_project(str(project_path))
    print(f"Completeness: {result.completeness:.1f}%")
    print(f"Status: {'Valid' if result.is_valid else 'Invalid'}")
    if result.errors:
        print(f"  ({len(result.errors)} error(s), {len(result.warnings)} warning(s))")

    # Learning stats
    learning_file = project_path / "docs" / "LEARNING.md"
    if learning_file.exists():
        content = learning_file.read_text()
        principles = content.count("[P]")
        patterns = content.count("[*]")
        observations = content.count("[-]")
        hypotheses = content.count("[?]")
        print(f"\nKnowledge:")
        print(f"  Principles: {principles}")
        print(f"  Patterns: {patterns}")
        print(f"  Observations: {observations}")
        print(f"  Hypotheses: {hypotheses}")

    print(f"{'='*50}\n")
    return 0


def cmd_log(args):
    """Log an action to the audit trail."""
    project_path = Path(args.path).resolve()
    audit_file = project_path / "guardrails" / "audit" / "action_log.jsonl"

    if not audit_file.parent.exists():
        print(f"Error: Audit directory not found. Is this a Recursa project?")
        return 1

    entry = {
        "timestamp": datetime.now().isoformat(),
        "action": args.action,
        "message": args.message,
        "tier": args.tier or "info",
    }

    with open(audit_file, "a") as f:
        f.write(json.dumps(entry) + "\n")

    print(f"Logged: [{entry['tier']}] {entry['action']}: {entry['message']}")
    return 0


def cmd_migrate(args):
    """Check for and apply migrations."""
    project_path = Path(args.path).resolve()

    if not project_path.exists():
        print(f"Error: Project not found: {project_path}")
        return 1

    version_file = project_path / ".recursa-version"
    current_version = "0.0.0"
    if version_file.exists():
        current_version = version_file.read_text().strip()

    print(f"Current version: {current_version}")
    print(f"Latest version: {FRAMEWORK_VERSION}")

    if current_version == FRAMEWORK_VERSION:
        print("Project is up to date!")
        return 0

    print(f"\nMigration needed: {current_version} -> {FRAMEWORK_VERSION}")

    # Check for missing files/directories
    missing_dirs = []
    for dir_path in MINIMAL_STRUCTURE:
        if not (project_path / dir_path).exists():
            missing_dirs.append(dir_path)

    missing_files = []
    for file_path in MINIMAL_FILES:
        if not (project_path / file_path).exists():
            missing_files.append(file_path)

    if missing_dirs:
        print(f"\nMissing directories:")
        for d in missing_dirs:
            print(f"  - {d}/")

    if missing_files:
        print(f"\nMissing files:")
        for f in missing_files:
            print(f"  - {f}")

    if not args.apply:
        print(f"\nRun with --apply to apply migrations")
        return 0

    # Apply migrations
    print(f"\nApplying migrations...")

    for dir_path in missing_dirs:
        (project_path / dir_path).mkdir(parents=True, exist_ok=True)
        print(f"  Created: {dir_path}/")

    for file_path in missing_files:
        full_path = project_path / file_path
        if file_path in MINIMAL_FILES:
            full_path.write_text(MINIMAL_FILES[file_path])
            print(f"  Created: {file_path}")

    # Update version file
    version_file.write_text(FRAMEWORK_VERSION)
    print(f"  Updated: .recursa-version")

    print(f"\nMigration complete!")
    return 0


def cmd_health(args):
    """Check knowledge base health."""
    import subprocess

    project_path = Path(args.path).resolve()

    if not project_path.exists():
        print(f"Error: Path not found: {project_path}")
        return 1

    # Run the knowledge-health tool
    health_script = Path(__file__).parent / "knowledge-health.py"

    if not health_script.exists():
        print(f"Error: knowledge-health.py not found")
        return 1

    cmd = [sys.executable, str(health_script), str(project_path)]
    if args.json:
        cmd.append("--json")

    result = subprocess.run(cmd)
    return result.returncode


def main():
    """CLI entry point."""
    import argparse

    parser = argparse.ArgumentParser(
        description="Recursa CLI - Manage self-improving projects",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  recursa init ~/my-project          Initialize a new project
  recursa validate ~/my-project      Check project structure
  recursa status ~/my-project        Show project status
  recursa health ~/my-project        Check knowledge base health
  recursa log ~/my-project -a "edit" -m "Updated SOUL.md"
  recursa migrate ~/my-project       Check for updates
        """
    )

    subparsers = parser.add_subparsers(dest="command", help="Command to run")

    # init command
    init_parser = subparsers.add_parser("init", help="Initialize a new Recursa project")
    init_parser.add_argument("path", help="Path for the new project")
    init_parser.add_argument("--force", "-f", action="store_true",
                            help="Overwrite existing files")

    # validate command
    validate_parser = subparsers.add_parser("validate", help="Validate project structure")
    validate_parser.add_argument("path", help="Path to the project")
    validate_parser.add_argument("--strict", action="store_true",
                                help="Treat warnings as errors")
    validate_parser.add_argument("--verbose", "-v", action="store_true",
                                help="Show detailed output")

    # status command
    status_parser = subparsers.add_parser("status", help="Show project status")
    status_parser.add_argument("path", help="Path to the project")

    # log command
    log_parser = subparsers.add_parser("log", help="Log an action to audit trail")
    log_parser.add_argument("path", help="Path to the project")
    log_parser.add_argument("-a", "--action", required=True, help="Action type")
    log_parser.add_argument("-m", "--message", required=True, help="Action message")
    log_parser.add_argument("-t", "--tier", help="Action tier (info, warning, error)")

    # migrate command
    migrate_parser = subparsers.add_parser("migrate", help="Check/apply migrations")
    migrate_parser.add_argument("path", help="Path to the project")
    migrate_parser.add_argument("--apply", action="store_true",
                               help="Apply migrations (otherwise just check)")

    # health command
    health_parser = subparsers.add_parser("health", help="Check knowledge base health")
    health_parser.add_argument("path", help="Path to the project")
    health_parser.add_argument("--json", action="store_true",
                              help="Output as JSON")

    args = parser.parse_args()

    if not args.command:
        parser.print_help()
        return 1

    commands = {
        "init": cmd_init,
        "validate": cmd_validate,
        "status": cmd_status,
        "log": cmd_log,
        "migrate": cmd_migrate,
        "health": cmd_health,
    }

    return commands[args.command](args)


if __name__ == "__main__":
    sys.exit(main())
