#!/usr/bin/env python3
"""
Knowledge health check tool for Recursa-based projects.

Analyzes LEARNING.md and reports on knowledge base health.
Helps prevent knowledge bloat by identifying compaction opportunities.

Usage:
    python tools/knowledge-health.py [project_path]

Example:
    python tools/knowledge-health.py ~/my-recursa-project
"""

import argparse
import re
import sys
from pathlib import Path
from collections import defaultdict


def find_learning_md(project_path: Path) -> Path | None:
    """Find LEARNING.md in common locations."""
    candidates = [
        project_path / 'docs' / 'LEARNING.md',
        project_path / 'LEARNING.md',
        project_path / 'knowledge' / 'LEARNING.md',
    ]
    for path in candidates:
        if path.exists():
            return path
    return None


def analyze_knowledge_file(filepath: Path) -> dict:
    """Analyze the knowledge base and return health metrics."""
    content = filepath.read_text()
    lines = content.split('\n')
    file_size_kb = len(content) / 1024

    # Count knowledge levels
    level_counts = defaultdict(int)
    level_pattern = r'\[([P\*\-\?U])\*?\]'

    for line in lines:
        matches = re.findall(level_pattern, line)
        for match in matches:
            level_counts[match] += 1

    # Calculate health scores
    obs_count = level_counts.get('-', 0)
    pattern_count = level_counts.get('*', 0)
    hypothesis_count = level_counts.get('?', 0)
    principle_count = level_counts.get('P', 0)

    # Ratio calculation (avoid division by zero)
    obs_pattern_ratio = obs_count / max(pattern_count, 1)

    # Detect dead ends and structural ceilings
    dead_end_patterns = [
        r'dead[\s-]*end',
        r'ceiling',
        r'structural(?:ly)?[\s-]+limit',
        r'doesn[\'"]?t\s+work',
        r'not\s+(?:viable|possible|working)',
        r'abandoned',
        r'do\s+not\s+(?:use|revisit)',
    ]
    dead_end_count = 0
    dead_end_lines = []
    for line in lines:
        line_lower = line.lower()
        for pattern in dead_end_patterns:
            if re.search(pattern, line_lower):
                dead_end_count += 1
                if len(dead_end_lines) < 5:  # Track first 5 for reporting
                    dead_end_lines.append(line.strip()[:80])
                break

    # Detect promotion candidates (observations that might be patterns)
    # Look for [-] items that mention "confirmed", "works", "reliable", "consistent"
    promotion_patterns = [
        r'confirmed',
        r'works?\s+(well|reliably|consistently)',
        r'reliable',
        r'consistent(ly)?',
        r'\d+\s*(?:times?|instances?|cases?)',
        r'always\s+works?',
        r'repeatedly',
    ]
    promotion_candidates = []
    for line in lines:
        if '[-]' in line:
            line_lower = line.lower()
            for pattern in promotion_patterns:
                if re.search(pattern, line_lower):
                    promotion_candidates.append(line.strip()[:100])
                    break

    # Health status
    size_status = 'OK'
    if file_size_kb > 500:
        size_status = 'CRITICAL'
    elif file_size_kb > 300:
        size_status = 'WARNING'

    obs_status = 'OK'
    if obs_count > 500:
        obs_status = 'CRITICAL'
    elif obs_count > 300:
        obs_status = 'WARNING'

    ratio_status = 'OK'
    if obs_pattern_ratio > 12:
        ratio_status = 'CRITICAL'
    elif obs_pattern_ratio > 8:
        ratio_status = 'WARNING'

    hyp_status = 'OK'
    if hypothesis_count > 20:
        hyp_status = 'CRITICAL'
    elif hypothesis_count > 10:
        hyp_status = 'WARNING'

    # Knowledge maturity score (0-100)
    # Higher = more mature (more principles/patterns vs hypotheses/observations)
    total_knowledge = principle_count + pattern_count + obs_count + hypothesis_count
    if total_knowledge > 0:
        maturity_score = int(
            ((principle_count * 4) + (pattern_count * 3) + (obs_count * 1) + (hypothesis_count * 0))
            / (total_knowledge * 4) * 100
        )
    else:
        maturity_score = 0

    return {
        'filepath': str(filepath),
        'file_size_kb': file_size_kb,
        'line_count': len(lines),
        'level_counts': dict(level_counts),
        'obs_pattern_ratio': obs_pattern_ratio,
        'dead_end_count': dead_end_count,
        'dead_end_examples': dead_end_lines[:3],
        'promotion_candidates': promotion_candidates[:5],
        'maturity_score': maturity_score,
        'health': {
            'size': size_status,
            'observations': obs_status,
            'ratio': ratio_status,
            'hypotheses': hyp_status,
        },
        'needs_compaction': any(s in ['CRITICAL', 'WARNING'] for s in [
            size_status, obs_status, ratio_status, hyp_status
        ])
    }


def print_report(analysis: dict) -> None:
    """Print a formatted health report."""
    print("=" * 60)
    print("KNOWLEDGE BASE HEALTH CHECK")
    print("=" * 60)
    print(f"File: {analysis['filepath']}")
    print()

    # Metrics table
    print("Metrics:")
    print("-" * 40)
    print(f"  File size:     {analysis['file_size_kb']:.1f} KB [{analysis['health']['size']}]")
    print(f"  Line count:    {analysis['line_count']}")
    print(f"  Maturity:      {analysis['maturity_score']}%")
    print()

    # Knowledge levels
    print("Knowledge Levels:")
    print("-" * 40)
    level_names = {
        'P': 'Principles [P]',
        '*': 'Patterns [*]',
        '-': 'Observations [-]',
        '?': 'Hypotheses [?]',
        'U': 'User-validated [U]'
    }
    for level, name in level_names.items():
        count = analysis['level_counts'].get(level, 0)
        status = ''
        if level == '-':
            status = f" [{analysis['health']['observations']}]"
        elif level == '?':
            status = f" [{analysis['health']['hypotheses']}]"
        print(f"  {name}: {count}{status}")

    print()
    print(f"Observation:Pattern ratio: {analysis['obs_pattern_ratio']:.1f}:1 [{analysis['health']['ratio']}]")

    # Dead ends and maturity indicators
    if analysis.get('dead_end_count', 0) > 0:
        print()
        print("Maturity Indicators:")
        print("-" * 40)
        print(f"  Dead ends documented: {analysis['dead_end_count']}")
        if analysis.get('dead_end_examples'):
            print("  Examples:")
            for ex in analysis['dead_end_examples']:
                print(f"    - {ex[:70]}...")

    # Promotion candidates
    if analysis.get('promotion_candidates'):
        print()
        print("Promotion Candidates ([-] that may warrant [*]):")
        print("-" * 40)
        for candidate in analysis['promotion_candidates'][:3]:
            print(f"  - {candidate[:70]}...")

    # Overall status
    print()
    print("=" * 60)
    if analysis['needs_compaction']:
        print("STATUS: COMPACTION NEEDED")
        print()
        print("Recommendations:")
        if analysis['health']['size'] != 'OK':
            print("  - File too large: merge duplicate entries, trim verbose notes")
        if analysis['health']['observations'] != 'OK':
            print("  - Too many observations: promote confirmed ones to patterns")
        if analysis['health']['ratio'] != 'OK':
            print("  - High obs:pattern ratio: consolidate observations into patterns")
        if analysis['health']['hypotheses'] != 'OK':
            print("  - Stale hypotheses: test or archive untested [?] items")
    else:
        print("STATUS: HEALTHY")
        print("Knowledge base is well-maintained.")
    print("=" * 60)


def main():
    parser = argparse.ArgumentParser(
        description="Check health of LEARNING.md knowledge base",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Health Thresholds:
  File size:      WARNING > 300KB, CRITICAL > 500KB
  Observations:   WARNING > 300, CRITICAL > 500
  Obs:Pattern:    WARNING > 8:1, CRITICAL > 12:1
  Hypotheses:     WARNING > 10, CRITICAL > 20
        """
    )
    parser.add_argument('project_path', nargs='?', default='.',
                        help='Path to Recursa project (default: current directory)')
    parser.add_argument('--json', action='store_true',
                        help='Output as JSON')
    args = parser.parse_args()

    project_path = Path(args.project_path).resolve()

    if not project_path.exists():
        print(f"Error: Project path not found: {project_path}", file=sys.stderr)
        return 1

    learning_path = find_learning_md(project_path)
    if not learning_path:
        print(f"Error: LEARNING.md not found in {project_path}", file=sys.stderr)
        print("Searched: docs/LEARNING.md, LEARNING.md, knowledge/LEARNING.md")
        return 1

    analysis = analyze_knowledge_file(learning_path)

    if args.json:
        import json
        print(json.dumps(analysis, indent=2))
    else:
        print_report(analysis)

    # Exit code: 2 if critical, 1 if warning, 0 if healthy
    if any(s == 'CRITICAL' for s in analysis['health'].values()):
        return 2
    elif any(s == 'WARNING' for s in analysis['health'].values()):
        return 1
    return 0


if __name__ == '__main__':
    sys.exit(main())
