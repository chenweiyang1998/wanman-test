# Installation Guide

## Prerequisites

- Python 3.10 or higher
- pip package manager

## Standard Installation

```bash
pip install -e .
```

## Development Installation

For development, install with all development dependencies:

```bash
pip install -e ".[dev]"
```

This will install:
- pytest - Testing framework
- pytest-cov - Coverage reporting
- pytest-asyncio - Async test support
- ruff - Fast Python linter
- mypy - Static type checker

## Verify Installation

```bash
python -c import wanmantest
```

## Uninstall

```bash
pip uninstall wanmantest
```
