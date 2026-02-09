# Code Review System

A self-improving code review assistant that learns from feedback to provide better reviews over time.

## Purpose

This system reviews pull requests, identifies issues, suggests improvements, and learns from the outcomes of its suggestions to become more accurate and helpful.

## Quick Start

1. Review system/SOUL.md to understand the reviewer's identity
2. Follow docs/LOOP.md for the review process
3. Track patterns in docs/LEARNING.md
4. Monitor quality via docs/METRICS.md

## Iteration Cycle

```
RECEIVE PR → ANALYZE → COMMENT → TRACK OUTCOME → LEARN
```

Each review is one iteration. After the PR is merged or closed, capture what suggestions were accepted, rejected, or modified.

## Integration

Can be integrated with:
- GitHub Actions (trigger on PR)
- Git hooks (pre-commit, pre-push)
- CI/CD pipelines

## Unique Features

- Tracks acceptance rate of suggestions by category
- Learns codebase-specific patterns
- Adjusts verbosity based on PR size and author experience
