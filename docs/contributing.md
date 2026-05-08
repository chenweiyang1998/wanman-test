# Contributing Guide

We welcome contributions to wanmantest!

## How to Contribute

### Reporting Issues

- Check if the issue already exists
- Provide clear reproduction steps
- Include your environment details

### Submitting Changes

1. **Fork the repository**
2. **Create a feature branch**
   ```bash
   git checkout -b feature/my-feature
   ```
3. **Make your changes**
   - Follow the code style guidelines
   - Add tests for new functionality
   - Update documentation as needed
4. **Run tests and linting**
   ```bash
   pytest
   ruff check .
   mypy .
   ```
5. **Commit your changes**
   ```bash
   git commit -m "Add: brief description of changes"
   ```
6. **Push and create Pull Request**

## Code Style

- Follow PEP 8 guidelines
- Add type hints to function signatures
- Write descriptive docstrings
- Keep functions focused and small

## Testing

- All new features must include tests
- All tests must pass before merging
- Aim for high test coverage

## Questions?

Feel free to open an issue for any questions or discussions.
