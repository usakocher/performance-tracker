# Contributing to Performance-Tracker

Thank you for your interest in contributing to Performance-Tracker! This document provides guidelines and information for contributors.

## Code of Conduct

This project follows a simple code of conduct: be respectful, constructive, and collaborative. We welcome contributions from developers of all experience levels.

## Getting Started

### Development Setup

#### Prerequisites

- Python 3.9 or higher
- Git
- UV (recommended) or pip

#### Setup with UV (Recommended)

UV provides faster dependency resolution and better virtual environment management.

```bash
# 1. Install UV (if not already installed)
curl -LsSf https://astral.sh/uv/install.sh | sh

# 2. Fork and clone the repository
git clone https://github.com/usakocher/performance-tracker.git
cd performance-tracker

# 3. Install all dependencies
uv sync --all-extras

# 4. Install pre-commit hooks
uv run pre-commit install

# 5. Verify setup
uv run pytest
uv run pre-commit run --all-files
```

#### Setup with pip (Traditional)

```bash
# 1. Fork and clone the repository
git clone https://github.com/usakocher/performance-tracker.git
cd performance-tracker

# 2. Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -e .
pip install -r requirements-dev.txt

# 4. Install pre-commit hooks
pre-commit install

# 5. Verify setup
python -m pytest
pre-commit run --all-files
```

## Commit Message Guidelines

We use **Conventional Commits** for consistent commit messages and automated versioning. This enables automatic changelog generation and semantic versioning.

### Commit Message Format

```
<type>[optional scope]: <description>

[optional body]

[optional footer(s)]
```

### Commit Types

| Type | Description | Version Impact |
|------|-------------|----------------|
| `feat` | New features | Minor version bump |
| `fix` | Bug fixes | Patch version bump |
| `docs` | Documentation changes | No version bump |
| `style` | Code style changes (formatting, etc.) | No version bump |
| `refactor` | Code refactoring (no functional changes) | No version bump |
| `perf` | Performance improvements | Patch version bump |
| `test` | Adding or updating tests | No version bump |
| `chore` | Maintenance tasks, dependency updates | No version bump |
| `ci` | CI/CD configuration changes | No version bump |
| `build` | Build system or dependency changes | No version bump |
| `revert` | Reverting previous commits | Depends on reverted change |

### Breaking Changes

For breaking changes, add `!` after the type or add `BREAKING CHANGE:` in the footer:

```bash
feat!: require Python 3.9+ minimum version

BREAKING CHANGE: Dropped support for Python 3.8 and earlier versions.
```

### Examples

#### Good Commit Messages

```bash
feat: add JSON output format for performance reports

fix: resolve memory tracking accuracy in recursive functions

docs: update installation guide with UV examples

test: add integration tests for memory monitoring

perf: optimize performance data collection by 15%

refactor: simplify recursion detection logic

chore: update development dependencies to latest versions

ci: add semantic-release workflow for automated versioning
```

#### Commit Messages with Scope

```bash
feat(monitor): add configurable output formats

fix(memory): resolve leak detection false positives

docs(api): add comprehensive function documentation

test(integration): add multi-threading test scenarios
```

#### Commit Messages with Body

```bash
feat: add JSON export functionality

Add support for exporting performance data in JSON format
for better integration with external monitoring systems.
Includes options for pretty-printing and custom field selection.

Resolves #42
```

### Commit Message Validation

We automatically validate commit messages in pull requests. If your commit message doesn't follow the conventional format, the CI will fail with helpful error messages.

**To fix commit message issues:**

```bash
# If you need to change the last commit message
git commit --amend -m "feat: your corrected message"

# If you need to change multiple commits
git rebase -i HEAD~3  # Replace 3 with number of commits to change
```

### Development Workflow

#### Creating a Feature Branch

```bash
# Start from develop
git checkout develop
git pull origin develop

# Create feature branch
git checkout -b feature/your-feature-name

# Make changes and commit using conventional format
git add .
git commit -m "feat: add your new feature description"

# Push and create pull request
git push -u origin feature/your-feature-name
```

#### Daily Development Commands

**With UV:**
```bash
# Install/update dependencies
uv sync --all-extras

# Run tests
uv run pytest                           # All tests
uv run pytest tests/test_monitor.py     # Specific file
uv run pytest -k test_basic_timing      # Specific test

# Code quality
uv run black .                          # Format code
uv run isort .                          # Sort imports
uv run flake8                           # Lint code
uv run pre-commit run --all-files       # Run all quality checks

# Add dependencies
uv add requests                         # Runtime dependency
uv add --dev pytest-mock                # Development dependency
```

**With pip:**
```bash
# Activate virtual environment
source venv/bin/activate

# Install/update dependencies
pip install -e .
pip install -r requirements-dev.txt

# Run tests
python -m pytest                       # All tests
python -m pytest tests/test_monitor.py # Specific file
python -m pytest -k test_basic_timing  # Specific test

# Code quality
black .                                 # Format code
isort .                                 # Sort imports
flake8                                  # Lint code
pre-commit run --all-files              # Run all quality checks
```

## Release Process

We use automated semantic versioning based on conventional commits:

### How Releases Work

1. **Commits to `develop`** - Normal development
2. **PR from `develop` to `main`** - Triggers release process
3. **Merge to `main`** - Automatic version calculation and release
4. **Automated actions**:
   - Analyze commits for version bump type
   - Update version in `pyproject.toml`
   - Generate changelog entry
   - Create GitHub release
   - Build and upload artifacts

### Version Bumping Rules

| Commit Types | Version Bump | Example |
|--------------|--------------|---------|
| `fix`, `perf` | PATCH | 1.0.0 → 1.0.1 |
| `feat` | MINOR | 1.0.0 → 1.1.0 |
| `feat!`, `BREAKING CHANGE` | MAJOR | 1.0.0 → 2.0.0 |
| `docs`, `style`, `test`, `chore` | None | No release |

### Preparing for Release

When you're ready to release from develop to main:

1. **Ensure all commits follow conventional format**
2. **Create PR**: `develop` → `main`
3. **PR title should be descriptive**: "Release: Add JSON export and fix memory tracking"
4. **Review changes and merge**
5. **Automatic release** will be created

## Types of Contributions

### Bug Reports

When reporting bugs, please include:
- Python version and operating system
- Performance-Tracker version
- Minimal code example that reproduces the issue
- Expected vs. actual behavior
- Error messages or stack traces

**Bug Report Template:**
```
**Environment:**
- Python version: 3.11.5
- Performance-Tracker version: 0.1.0
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
- Consider if the feature fits Performance-Tracker's scope
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
uv run black performance-tracker/ tests/
uv run isort performance-tracker/ tests/
uv run flake8 performance-tracker/ tests/
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
   uv run pytest
   ```

2. **Check code quality**:
   ```bash
   uv run flake8 performance-tracker/ tests/
   uv run black --check performance-tracker/ tests/
   ```

3. **Verify commit messages** follow conventional format

4. **Update documentation** if needed

### Pull Request Template

```
## Description
Brief description of changes

## Type of Change
- [ ] Bug fix (`fix:`)
- [ ] New feature (`feat:`)
- [ ] Documentation update (`docs:`)
- [ ] Performance improvement (`perf:`)
- [ ] Refactoring (`refactor:`)
- [ ] Breaking change (`feat!:` or `BREAKING CHANGE:`)

## Testing
- [ ] Added tests for new functionality
- [ ] All tests pass
- [ ] Manual testing completed

## Checklist
- [ ] Code follows style guidelines
- [ ] Commit messages follow conventional format
- [ ] Self-review completed
- [ ] Documentation updated
```

### Review Process

1. **Automated checks** must pass (CI/CD)
2. **Commit message validation** passes
3. **Code review** by maintainer
4. **Testing** on different environments
5. **Documentation review** if applicable
6. **Merge** after approval

## Development Tools

### Code Quality Tools

All tools are configured to work together and enforce consistent code style:

- **Black**: Code formatting (88 character line length)
- **isort**: Import sorting (Black-compatible profile)
- **flake8**: Linting and style checking
- **pre-commit**: Automated quality checks on commit

### Testing Tools

- **pytest**: Test runner with plugins
- **pytest-cov**: Coverage reporting
- **unittest**: Standard library testing (for simple tests)

### Project Management

- **UV**: Modern package manager (recommended)
- **pip**: Traditional package manager (supported)
- **pyproject.toml**: Project configuration and metadata
- **Semantic Release**: Automated versioning and releases

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
- Automated changelog

Significant contributors may be invited to become maintainers.

## Legal

By contributing, you agree that your contributions will be licensed under the MIT License. You confirm that you have the right to submit your contributions and that they are your original work.
