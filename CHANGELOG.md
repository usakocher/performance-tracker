# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added
- Automated semantic versioning with conventional commits
  - Commit message linting for consistent format
  - Automatic version bumping based on commit types
  - Automated changelog generation
  - GitHub release automation
- Conventional commit guidelines in contributing documentation
- Semantic release workflow for main branch
- Version validation in CI/CD pipeline

### Changed
- Development workflow now includes conventional commit format
- Release process automated based on commit message types
- Contributing guide enhanced with commit message standards

## [0.1.0] - 2025-01-18

### Added
- UV package manager support for faster dependency management
  - Modern pyproject.toml configuration with optional dependencies
  - UV lockfile (uv.lock) for reproducible builds
  - Updated GitHub Actions CI to use UV
  - Comprehensive UV documentation in README and installation guide
- Pre-commit hooks for automated code quality checks
  - Black for code formatting
  - isort for import sorting
  - flake8 for linting
  - Built-in hooks for file quality (trailing whitespace, YAML syntax, etc.)
- .flake8 configuration file for consistent linting rules
- Initial release of PyPerformance
- Function timing with microsecond precision using perf_counter()
- Memory usage monitoring with peak and net allocation tracking
- Recursion-aware function monitoring
- Comprehensive performance reporting with statistics
- Thread-safe operation using thread-local storage
- Configurable verbosity and feature toggles
- Zero external dependencies
- Complete test suite
- Documentation and examples

### Changed
- **BREAKING:** Minimum Python version requirement is 3.9+
- Development workflow now uses UV commands for faster dependency resolution
- Documentation updated to recommend UV while maintaining pip compatibility
- Enhanced project configuration in pyproject.toml with comprehensive metadata
- Pre-commit hooks work with UV environment
- Contributing guide updated with UV and pip workflows

### Fixed
- Removed unused `global performance_stats` statement in `reset_performance_stats()`
- Fixed line length violations throughout codebase
- Removed unused imports (Union from typing, request/json from Flask example)
- Fixed function name conflict in web app example
- Cleaned up f-string usage where placeholders weren't needed

### Developer Experience
- `uv sync --all-extras` replaces `pip install -r requirements-dev.txt`
- `uv run pytest` replaces `python -m pytest`
- 10-100x faster dependency resolution and installation
- Automatic virtual environment management
- Better error messages and debugging
- Consistent commit message format with automated validation
- Automated release management

### Features
- `@performance_monitor()` decorator for function monitoring
- `show_performance_report()` for aggregate statistics
- `reset_performance_stats()` for clearing collected data
- `get_performance_stats()` for programmatic access to data
- Support for Python 3.9+

### Technical Notes
- Python 3.9+ requirement enables use of modern Python features
- Simplified CI/CD pipeline and maintenance
- Older Python versions are no longer recommended for new projects
- Semantic versioning enables predictable releases and upgrade paths
