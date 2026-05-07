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
│   └── spdm-data-management/  # SPDM 可视化原型
├── pyproject.toml      # Project configuration
├── LICENSE             # MIT License
└── README.md           # This file
```

## SPDM Prototype

SPDM（Simulation Process & Data Management，仿真过程与数据管理）原型展示了仿真数据的生命周期可视化：

- **交互式数据流图**：使用 p5.js 绘制，包含 BOM、仿真任务、工况、报告等数据节点
- **动画效果**：数据节点和连接线动态展示仿真数据结构
- **设计哲学**："数据流动生命体"的可视化理念

访问方式：
```bash
cd deliverables/spdm-data-management
python -m http.server 8080
# 然后访问 http://localhost:8080
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
