# wanmantest

> wanman multi-agent system test project

## Overview

wanmantest is a Python project designed to test and validate the wanman multi-agent system capabilities. This project serves as a playground for developing, testing, and benchmarking agent coordination workflows.

## Features

- Multi-agent coordination framework
- Task management and delegation
- Agent communication protocols
- Performance benchmarking tools

## Installation

```bash
# Clone the repository
git clone <repository-url>
cd wanmantest

# Install with development dependencies
pip install -e ".[dev]"

# Or install just the package
pip install -e .
```

## Development Setup

```bash
# Install development dependencies
pip install -e ".[dev]"

# Run tests
pytest

# Run tests with coverage
pytest --cov=. --cov-report=term-missing

# Lint code
ruff check .

# Type check
mypy .
```

## Project Structure

```
wanmantest/
├── .github/           # GitHub configuration (CI/CD workflows)
├── docs/               # Documentation
├── tests/              # Test suite
├── deliverables/       # Project deliverables and artifacts
├── pyproject.toml      # Project configuration
├── LICENSE             # MIT License
└── README.md           # This file
```

## Testing

This project uses pytest with the following configuration:

- Async test support via `pytest-asyncio`
- Coverage reporting via `pytest-cov`
- Automatic async mode enabled

Run all tests:
```bash
pytest
```

Run specific test file:
```bash
pytest tests/test_example.py
```

## Code Quality

We use several tools to maintain code quality:

- **ruff**: Fast Python linter (E, F, I, N, W, UP rules)
- **mypy**: Static type checker

## License

MIT License - see [LICENSE](LICENSE) for details.

## Contributing

Contributions are welcome! Please ensure:
- All tests pass before submitting PRs
- Code follows the project's linting rules
- New features include appropriate tests
