# Contributing to PyPerformance

Thank you for your interest in contributing to PyPerformance! This document provides guidelines and information for contributors.

## Code of Conduct

This project follows a simple code of conduct: be respectful, constructive, and collaborative. We welcome contributions from developers of all experience levels.

## Getting Started

### Development Setup

1. **Fork the repository** on GitHub
2. **Clone your fork** locally:
   ```bash
   git clone https://github.com/yourusername/python-performance-monitor.git
   cd python-performance-monitor
   ```

3. **Create a virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

4. **Install development dependencies**:
   ```bash
   pip install -r requirements-dev.txt
   pip install -e .
   ```

5. **Verify the setup**:
   ```bash
   python -m pytest tests/
   python -m flake8 pyperformance/
   python -m black --check pyperformance/
   ```

### Development Workflow

1. **Create a branch** for your feature or bug fix:
   ```bash
   git checkout -b feature/your-feature-name
   ```

2. **Make your changes** following the coding standards below

3. **Add or update tests** for your changes

4. **Run the test suite**:
   ```bash
   python -m pytest tests/ -v
   python -m pytest tests/ --cov=pyperformance
   ```

5. **Check code quality**:
   ```bash
   python -m flake8 pyperformance/ tests/
   python -m black pyperformance/ tests/
   python -m isort pyperformance/ tests/
   ```

6. **Commit your changes**:
   ```bash
   git add .
   git commit -m "Add feature: your feature description"
   ```

7. **Push to your fork** and **create a pull request**

## Types of Contributions

### Bug Reports

When reporting bugs, please include:
- Python version and operating system
- PyPerformance version
- Minimal code example that reproduces the issue
- Expected vs. actual behavior
- Error messages or stack traces

**Bug Report Template:**
```
**Environment:**
- Python version: 3.11.5
- PyPerformance version: 0.1.0
- OS: Ubuntu 20.04

**Description:**
Brief description of the bug

**Reproduction Steps:**
1. Step one
2. Step two
3. Step three

**Expected Behavior:**
What should happen

**Actual Behavior:**
What actually happens

**Code Example:**
```python
# Minimal code that reproduces the issue
```

### Feature Requests

Before proposing new features:
- Check existing issues to avoid duplicates
- Consider if the feature fits PyPerformance's scope
- Think about backward compatibility

**Feature Request Template:**
```
**Problem:**
What problem does this feature solve?

**Proposed Solution:**
Describe your proposed solution

**Alternatives:**
What alternatives have you considered?

**Use Cases:**
Real-world scenarios where this would be useful
```

### Documentation Improvements

Documentation contributions are highly valued:
- Fix typos and grammar
- Improve clarity and examples
- Add missing documentation
- Update outdated information

### Code Contributions

#### Areas for Contribution

**Core Features:**
- Performance optimizations
- Memory tracking improvements
- Better error handling
- Thread safety enhancements

**New Features:**
- Additional output formats (JSON, CSV)
- Integration with logging frameworks
- Performance regression detection
- Historical data storage

**Testing:**
- Increase test coverage
- Add performance benchmarks
- Test edge cases
- Cross-platform testing

**Developer Experience:**
- Better error messages
- Improved documentation
- Example applications
- IDE integration

## Coding Standards

### Python Style

We follow PEP 8 with these specifics:
- Line length: 88 characters (Black default)
- Use type hints for public APIs
- Docstrings for all public functions and classes

### Code Formatting

We use automated tools:
- **Black** for code formatting
- **isort** for import sorting
- **flake8** for linting

Run before committing:
```bash
black pyperformance/ tests/
isort pyperformance/ tests/
flake8 pyperformance/ tests/
```

### Documentation Style

- Use clear, concise language
- Include code examples for complex features
- Keep examples runnable and testable
- Use consistent terminology

### Testing Requirements

All contributions must include tests:
- **Unit tests** for new functionality
- **Integration tests** for complex features
- **Performance tests** for optimization changes
- **Edge case testing** for robustness

Test structure:
```python
def test_feature_name():
    """Test description explaining what is being tested"""
    # Arrange
    setup_code()
    
    # Act
    result = function_under_test()
    
    # Assert
    assert result == expected_value
```

## Pull Request Process

### Before Submitting

1. **Ensure tests pass**:
   ```bash
   python -m pytest tests/ -v
   ```

2. **Check code quality**:
   ```bash
   python -m flake8 pyperformance/ tests/
   python -m black --check pyperformance/ tests/
   ```

3. **Update documentation** if needed

4. **Add changelog entry** for user-facing changes

### Pull Request Template

```
## Description
Brief description of changes

## Type of Change
- [ ] Bug fix
- [ ] New feature
- [ ] Documentation update
- [ ] Performance improvement
- [ ] Refactoring

## Testing
- [ ] Added tests for new functionality
- [ ] All tests pass
- [ ] Manual testing completed

## Checklist
- [ ] Code follows style guidelines
- [ ] Self-review completed
- [ ] Documentation updated
- [ ] Changelog updated (if needed)
```

### Review Process

1. **Automated checks** must pass (CI/CD)
2. **Code review** by maintainer
3. **Testing** on different environments
4. **Documentation review** if applicable
5. **Merge** after approval

## Project Structure

Understanding the codebase:

```
pyperformance/
├── __init__.py          # Public API exports
├── monitor.py           # Core monitoring functionality
└── utils.py            # Utility functions

tests/
├── test_monitor.py      # Core functionality tests
├── test_utils.py       # Utility function tests
└── test_integration.py  # Integration tests

examples/
├── basic_usage.py       # Simple examples
├── web_app_example.py   # Flask integration
└── memory_analysis.py   # Memory monitoring examples

docs/
├── installation.md      # Setup instructions
├── advanced_usage.md    # Complex scenarios
├── api_reference.md     # Complete API docs
├── contributing.md      # This file
├── performance_benchmarks.md
└── faq.md
```

## Design Principles

When contributing, keep these principles in mind:

### Simplicity
- Prefer simple solutions over complex ones
- Minimize configuration required
- Clear, obvious APIs

### Performance
- Minimal overhead when monitoring is disabled
- Efficient data structures
- No unnecessary allocations

### Reliability
- Graceful error handling
- Thread-safe operations
- Backward compatibility

### Developer Experience
- Clear error messages
- Comprehensive documentation
- Runnable examples

## Release Process

### Versioning

We use [Semantic Versioning](https://semver.org/):
- **MAJOR**: Breaking changes
- **MINOR**: New features, backward compatible
- **PATCH**: Bug fixes, backward compatible

### Release Checklist

1. Update version in `setup.py` and `__init__.py`
2. Update `CHANGELOG.md`
3. Create release tag
4. Build and upload to PyPI
5. Update documentation

## Getting Help

### Questions and Discussion

- **GitHub Issues**: Bug reports and feature requests
- **GitHub Discussions**: General questions and ideas
- **Email**: Direct contact for sensitive issues

### Mentorship

New contributors are welcome! If you're new to open source:
- Start with documentation improvements
- Look for "good first issue" labels
- Ask questions in discussions
- Join code reviews as a learning opportunity

## Recognition

Contributors are recognized in:
- `CONTRIBUTORS.md` file
- Release notes
- GitHub contributors page

Significant contributors may be invited to become maintainers.

## Legal

By contributing, you agree that your contributions will be licensed under the MIT License. You confirm that you have the right to submit your contributions and that they are your original work.