# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.1.0] - 2025-01-18

### Added
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