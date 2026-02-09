#!/usr/bin/env python3
"""
Recursa Project Validator

Validates that a Recursa-based project has the required structure and content.
"""

import os
import sys
import re
import json
from pathlib import Path
from typing import Dict, List, Tuple, Optional

# Required files for a minimal Recursa project
MINIMAL_FILES = [
    "system/ORIGIN.md",
    "system/SOUL.md",
    "docs/LOOP.md",
    "docs/LEARNING.md",
    "docs/METRICS.md",
]

# Additional files for a standard project
STANDARD_FILES = [
    "system/CONSTITUTION.md",
    "system/IDENTITY.md",
    "system/STYLE.md",
    "docs/MEMORY.md",
    "docs/GOALS.md",
    "docs/EVOLUTION.md",
    "docs/EXPERIMENTS.md",
    "guardrails/GUARDRAILS.md",
]

# Required directories
REQUIRED_DIRS = [
    "system",
    "docs",
]

STANDARD_DIRS = [
    "memory",
    "journal",
    "guardrails",
    "guardrails/audit",
]

# Placeholder patterns that indicate uncustomized content
PLACEHOLDER_PATTERNS = [
    r'\[Your .*?\]',
    r'\[System .*?\]',
    r'\[PLACEHOLDER\]',
    r'\[TODO\]',
    r'\[INSERT .*?\]',
    r'\[Describe .*?\]',
    r'\[List .*?\]',
    r'\[Define .*?\]',
    r'\[X\]%',  # Percentage placeholders
    r'\[N\] iterations',
    r'\[Duration\]',
    r'\[Category \d+\]',
    r'\[Trait \d+\]',
    r'\[Goal \d+\]',
]


class ValidationResult:
    """Holds validation results for reporting."""

    def __init__(self, project_path: str):
        self.project_path = project_path
        self.errors: List[str] = []
        self.warnings: List[str] = []
        self.info: List[str] = []
        self.files_checked = 0
        self.files_valid = 0
        self.placeholders_found: Dict[str, List[str]] = {}

    @property
    def is_valid(self) -> bool:
        return len(self.errors) == 0

    @property
    def completeness(self) -> float:
        total = len(MINIMAL_FILES) + len(STANDARD_FILES)
        return (self.files_valid / total) * 100 if total > 0 else 0

    def add_error(self, msg: str):
        self.errors.append(msg)

    def add_warning(self, msg: str):
        self.warnings.append(msg)

    def add_info(self, msg: str):
        self.info.append(msg)


def check_file_exists(project_path: Path, relative_path: str) -> bool:
    """Check if a file exists in the project."""
    return (project_path / relative_path).exists()


def check_dir_exists(project_path: Path, relative_path: str) -> bool:
    """Check if a directory exists in the project."""
    return (project_path / relative_path).is_dir()


def find_placeholders(file_path: Path) -> List[str]:
    """Find placeholder patterns in a file."""
    placeholders = []
    try:
        content = file_path.read_text(encoding='utf-8')
        for pattern in PLACEHOLDER_PATTERNS:
            matches = re.findall(pattern, content, re.IGNORECASE)
            placeholders.extend(matches)
    except Exception:
        pass
    return placeholders


def check_file_customized(file_path: Path) -> Tuple[bool, List[str]]:
    """Check if a file has been customized (no placeholders)."""
    placeholders = find_placeholders(file_path)
    return len(placeholders) == 0, placeholders


def check_file_not_empty(file_path: Path, min_lines: int = 10) -> bool:
    """Check if a file has substantial content."""
    try:
        content = file_path.read_text(encoding='utf-8')
        lines = [l for l in content.split('\n') if l.strip()]
        return len(lines) >= min_lines
    except Exception:
        return False


def validate_project(project_path: str, strict: bool = False) -> ValidationResult:
    """
    Validate a Recursa project.

    Args:
        project_path: Path to the project directory
        strict: If True, treat warnings as errors

    Returns:
        ValidationResult with all findings
    """
    path = Path(project_path).resolve()
    result = ValidationResult(str(path))

    # Check project directory exists
    if not path.exists():
        result.add_error(f"Project directory does not exist: {path}")
        return result

    if not path.is_dir():
        result.add_error(f"Path is not a directory: {path}")
        return result

    result.add_info(f"Validating project: {path}")

    # Check required directories
    for dir_path in REQUIRED_DIRS:
        if not check_dir_exists(path, dir_path):
            result.add_error(f"Missing required directory: {dir_path}/")

    for dir_path in STANDARD_DIRS:
        if not check_dir_exists(path, dir_path):
            result.add_warning(f"Missing standard directory: {dir_path}/")

    # Check minimal files (required)
    for file_path in MINIMAL_FILES:
        result.files_checked += 1
        full_path = path / file_path

        if not check_file_exists(path, file_path):
            result.add_error(f"Missing required file: {file_path}")
            continue

        if not check_file_not_empty(full_path):
            result.add_error(f"File is empty or too short: {file_path}")
            continue

        is_customized, placeholders = check_file_customized(full_path)
        if not is_customized:
            result.placeholders_found[file_path] = placeholders
            if strict:
                result.add_error(f"File contains placeholders: {file_path}")
            else:
                result.add_warning(f"File contains {len(placeholders)} placeholder(s): {file_path}")

        result.files_valid += 1

    # Check standard files (recommended)
    for file_path in STANDARD_FILES:
        result.files_checked += 1
        full_path = path / file_path

        if not check_file_exists(path, file_path):
            result.add_warning(f"Missing standard file: {file_path}")
            continue

        if not check_file_not_empty(full_path, min_lines=5):
            result.add_warning(f"File appears incomplete: {file_path}")
            continue

        is_customized, placeholders = check_file_customized(full_path)
        if not is_customized:
            result.placeholders_found[file_path] = placeholders
            result.add_warning(f"File contains {len(placeholders)} placeholder(s): {file_path}")

        result.files_valid += 1

    # Check for version file
    version_file = path / ".recursa-version"
    if not version_file.exists():
        result.add_info("No .recursa-version file found (optional)")

    # Check for audit log
    audit_log = path / "guardrails" / "audit" / "action_log.jsonl"
    if audit_log.exists():
        result.add_info("Audit log present")

    return result


def print_result(result: ValidationResult, verbose: bool = False):
    """Print validation results to console."""
    print(f"\n{'='*60}")
    print(f"RECURSA PROJECT VALIDATION")
    print(f"{'='*60}")
    print(f"Project: {result.project_path}")
    print(f"Completeness: {result.completeness:.1f}%")
    print(f"Files checked: {result.files_checked}")
    print(f"Files valid: {result.files_valid}")
    print()

    if result.errors:
        print(f"ERRORS ({len(result.errors)}):")
        for error in result.errors:
            print(f"  [X] {error}")
        print()

    if result.warnings:
        print(f"WARNINGS ({len(result.warnings)}):")
        for warning in result.warnings:
            print(f"  [!] {warning}")
        print()

    if verbose and result.info:
        print(f"INFO:")
        for info in result.info:
            print(f"  [i] {info}")
        print()

    if verbose and result.placeholders_found:
        print("PLACEHOLDERS FOUND:")
        for file_path, placeholders in result.placeholders_found.items():
            print(f"  {file_path}:")
            for p in placeholders[:5]:  # Show first 5
                print(f"    - {p}")
            if len(placeholders) > 5:
                print(f"    ... and {len(placeholders) - 5} more")
        print()

    # Final verdict
    print(f"{'='*60}")
    if result.is_valid:
        print("RESULT: VALID")
        if result.warnings:
            print(f"  (with {len(result.warnings)} warning(s))")
    else:
        print("RESULT: INVALID")
        print(f"  Fix {len(result.errors)} error(s) to pass validation")
    print(f"{'='*60}\n")


def main():
    """CLI entry point."""
    import argparse

    parser = argparse.ArgumentParser(
        description="Validate a Recursa project structure and content"
    )
    parser.add_argument(
        "project_path",
        help="Path to the Recursa project directory"
    )
    parser.add_argument(
        "--strict",
        action="store_true",
        help="Treat warnings as errors (stricter validation)"
    )
    parser.add_argument(
        "--verbose", "-v",
        action="store_true",
        help="Show detailed output including info messages"
    )
    parser.add_argument(
        "--json",
        action="store_true",
        help="Output results as JSON"
    )

    args = parser.parse_args()

    result = validate_project(args.project_path, strict=args.strict)

    if args.json:
        output = {
            "project_path": result.project_path,
            "is_valid": result.is_valid,
            "completeness": result.completeness,
            "files_checked": result.files_checked,
            "files_valid": result.files_valid,
            "errors": result.errors,
            "warnings": result.warnings,
            "placeholders": result.placeholders_found,
        }
        print(json.dumps(output, indent=2))
    else:
        print_result(result, verbose=args.verbose)

    # Exit code: 0 for valid, 1 for invalid
    sys.exit(0 if result.is_valid else 1)


if __name__ == "__main__":
    main()
