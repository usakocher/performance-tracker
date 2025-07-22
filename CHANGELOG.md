# [2.0.0](https://github.com/usakocher/performance-tracker/compare/v1.0.2...v2.0.0) (2025-07-22)


### Features

* rename package from pyperformance to performance-tracker ([#12](https://github.com/usakocher/performance-tracker/issues/12)) ([e9eb72d](https://github.com/usakocher/performance-tracker/commit/e9eb72d1f8aeabad3a5d4d573a2558044d6569db))


### Release

* Rename to performance-tracker v2.0.0 ([#13](https://github.com/usakocher/performance-tracker/issues/13)) ([4ee50e1](https://github.com/usakocher/performance-tracker/commit/4ee50e13385a0cb4af0749dc8157414a4629f627))


### BREAKING CHANGES

* in the commit message.

## Expected Semantic Release Behavior
- Semantic-release will analyze the `feat:` commit with `BREAKING
CHANGE:` footer
- Calculate MAJOR version bump to 2.0.0
- Update CHANGELOG.md with breaking change details
- Create GitHub release with migration notes
- Update pyproject.toml version automatically

## Breaking Changes
- **Package name changed**: Users must update from `pip install
pyperformance` to `pip install performance-tracker`
- **Import statements changed**: Users must update from `from
pyperformance import ...` to `from performance_tracker import ...`

## Migration Guide
For existing users:
```bash
# Uninstall old package
pip uninstall pyperformance

# Install new package
pip install performance-tracker

# Update import statements in code
# OLD: from pyperformance import performance_monitor
# NEW: from performance_tracker import performance_monitor
* Package name changed from pyperformance to
performance-tracker to avoid naming conflict with official Python
benchmarking suite. Users must update imports from 'pyperformance' to
'performance_tracker'.

## Summary

Brief description of what this PR accomplishes.

## Type of Change

Select the type of change (check all that apply):

- [ ] Bug fix (`fix:`) - non-breaking change that fixes an issue
- [x] New feature (`feat:`) - non-breaking change that adds
functionality
- [x] Breaking change (`feat!:` or `BREAKING CHANGE:`) - fix or feature
that would cause existing functionality to not work as expected
- [x] Documentation update (`docs:`) - changes to documentation only
- [ ] Code style (`style:`) - formatting, missing semi-colons, etc; no
production code change
- [ ] Code refactoring (`refactor:`) - refactoring production code, eg.
renaming a variable
- [ ] Performance improvement (`perf:`) - code change that improves
performance
- [ ] Test update (`test:`) - adding missing tests, refactoring tests;
no production code change
- [ ] Chore (`chore:`) - updating grunt tasks etc; no production code
change
- [ ] CI/CD (`ci:`) - changes to CI configuration files and scripts

## Changes Made

Describe the changes in detail:

- Rename package directory from pyperformance to performance_tracker
- Update pyproject.toml name to performance-tracker
- Update all import statements throughout codebase
- Update documentation and examples with new package name
- Update installation instructions in README and docs

## Testing

Describe how you tested your changes:

- [x] Unit tests added/updated
- [x] Integration tests added/updated
- [x] Manual testing performed
- [x] All existing tests pass
- [x] Performance impact assessed (if applicable)

### Test Details

```bash
# Commands used to test
uv run pytest
uv run pytest --cov=pyperformance
```

## Documentation

- [x] Code is self-documenting with clear variable/function names
- [x] Docstrings added/updated for public functions
- [x] README updated (if needed)
- [x] API documentation updated (if needed)
- [x] Changelog will be updated automatically

## Checklist

Before submitting this PR, please make sure:

- [x] I have read and followed the contributing guidelines
- [x] I have performed a self-review of my code
- [x] I have commented my code, particularly in hard-to-understand areas
- [x] I have made corresponding changes to the documentation
- [x] My changes generate no new warnings
- [x] I have added tests that prove my fix is effective or that my
feature works
- [x] New and existing unit tests pass locally with my changes
- [x] Any dependent changes have been merged and published

## Conventional Commits

This PR follows conventional commit format:

- [x] Commit messages follow the conventional format: `type:
description`
- [x] Breaking changes are marked with `!` or `BREAKING CHANGE:` footer
- [x] Commit messages are descriptive and explain the "what" and "why"

## Related Issues

Closes #
Related to #

## Screenshots (if applicable)

Add screenshots to help explain your changes.

## Additional Notes

Add any other context about the pull request here.

## [1.0.2](https://github.com/usakocher/performance-tracker/compare/v1.0.1...v1.0.2) (2025-07-21)


### Bug Fixes

* use personal access token for semantic-release permissions ([#8](https://github.com/usakocher/performance-tracker/issues/8)) ([3429fd0](https://github.com/usakocher/performance-tracker/commit/3429fd019f24f4c80b7f73944b82edd24c902e4e))

## [1.0.1](https://github.com/usakocher/performance-tracker/compare/v1.0.0...v1.0.1) (2025-07-21)


### Bug Fixes

* replace placeholder URLs with actual repository information ([#6](https://github.com/usakocher/performance-tracker/issues/6)) ([7f7517e](https://github.com/usakocher/performance-tracker/commit/7f7517ef1618b0a98fa40117be74050871acea71))

# 1.0.0 (2025-07-18)


### Bug Fixes

* remove npm plugin from semantic-release config ([79c7c20](https://github.com/usakocher/performance-tracker/commit/79c7c20934987a442ed754993e81ed4ee6feb3c6))
* replace broken wagoid action with reliable custom workflow ([5ebb5c9](https://github.com/usakocher/performance-tracker/commit/5ebb5c9df56f24c5171d63727d62cd1244fed3e9))
* replace broken wagoid action with working custom workflow ([e7479ab](https://github.com/usakocher/performance-tracker/commit/e7479abcc7236d37f61eff737ebb66c1fac7474b))


### Features

* implement semantic versioning and automated releases ([fb31758](https://github.com/usakocher/performance-tracker/commit/fb31758be96dd82780344e94997ec4ff45ed6dfe))

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
- Initial release of Performance-Tracker
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
