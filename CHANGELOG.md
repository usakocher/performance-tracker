## [1.0.2](https://github.com/usakocher/python-performance-monitor/compare/v1.0.1...v1.0.2) (2025-07-21)


### Bug Fixes

* use personal access token for semantic-release permissions ([#8](https://github.com/usakocher/python-performance-monitor/issues/8)) ([3429fd0](https://github.com/usakocher/python-performance-monitor/commit/3429fd019f24f4c80b7f73944b82edd24c902e4e))

## [1.0.1](https://github.com/usakocher/python-performance-monitor/compare/v1.0.0...v1.0.1) (2025-07-21)


### Bug Fixes

* replace placeholder URLs with actual repository information ([#6](https://github.com/usakocher/python-performance-monitor/issues/6)) ([7f7517e](https://github.com/usakocher/python-performance-monitor/commit/7f7517ef1618b0a98fa40117be74050871acea71))

# 1.0.0 (2025-07-18)


### Bug Fixes

* remove npm plugin from semantic-release config ([79c7c20](https://github.com/usakocher/python-performance-monitor/commit/79c7c20934987a442ed754993e81ed4ee6feb3c6))
* replace broken wagoid action with reliable custom workflow ([5ebb5c9](https://github.com/usakocher/python-performance-monitor/commit/5ebb5c9df56f24c5171d63727d62cd1244fed3e9))
* replace broken wagoid action with working custom workflow ([e7479ab](https://github.com/usakocher/python-performance-monitor/commit/e7479abcc7236d37f61eff737ebb66c1fac7474b))


### Features

* implement semantic versioning and automated releases ([fb31758](https://github.com/usakocher/python-performance-monitor/commit/fb31758be96dd82780344e94997ec4ff45ed6dfe))

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
