# Development Guide

## Development Workflow

### 1. Clone and Setup

```bash
git clone <repository-url>
cd wanmantest
pip install -e ".[dev]"
```

### 2. Running Tests

Run all tests:
```bash
pytest
```

Run with coverage:
```bash
pytest --cov=. --cov-report=term-missing
```

Run specific test file:
```bash
pytest tests/test_example.py
```

### 3. Code Quality Checks

Run linter:
```bash
ruff check .
```

Run type checker:
```bash
mypy .
```

Format code:
```bash
ruff format .
```

### 4. Git Workflow

1. Create a feature branch: `git checkout -b feature/my-feature`
2. Make changes and commit
3. Run tests and linting
4. Push and create pull request

## Project Structure

```
wanmantest/
├── .github/workflows/   # CI/CD workflows
├── docs/                # Documentation
├── tests/               # Test suite
├── pyproject.toml       # Project configuration
└── README.md            # Project README
```

## Code Style

This project follows:
- PEP 8 style guidelines (enforced by ruff)
- Type hints for function signatures (checked by mypy)
- Google-style docstrings
