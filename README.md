# PyPerformance

A lightweight, developer-friendly Python performance monitoring library that provides real-time insights into function execution time, memory usage, and call patterns.

## Why PyPerformance?

Traditional Python profiling tools are either too complex for everyday use or lack the real-time feedback developers need during development. PyPerformance bridges this gap by offering:

- **Zero-configuration monitoring** - Just add a decorator
- **Real-time feedback** - See performance data as your code runs
- **Memory leak detection** - Distinguish between temporary and permanent memory usage
- **Recursion-aware tracking** - Intelligent handling of recursive functions
- **Comprehensive reporting** - Aggregate statistics across all monitored functions

## Quick Start

```python
from pyperformance import performance_monitor, show_performance_report

@performance_monitor()
def slow_function():
    import time
    time.sleep(0.1)
    return "done"

@performance_monitor(track_memory=True)
def memory_intensive():
    return [i for i in range(1000000)]

# Use your functions normally
slow_function()
memory_intensive()

# View comprehensive performance report
show_performance_report()
```

## Installation

### Install PyPerformance

**Using pip:**
```bash
pip install pyperformance
```

**Using UV (recommended):**
```bash
uv add pyperformance
```

### Verify Installation

```python
from pyperformance import performance_monitor
print("PyPerformance installed successfully!")
```

## Development Setup

### Quick Start with UV (Recommended)

UV is a modern, fast Python package manager. It's 10-100x faster than pip and provides better dependency management.

```bash
# 1. Install UV
curl -LsSf https://astral.sh/uv/install.sh | sh

# 2. Clone and setup project
git clone https://github.com/usakocher/python-performance-monitor.git
cd python-performance-monitor

# 3. Install all dependencies (creates virtual environment automatically)
uv sync --all-extras

# 4. Run tests to verify setup
uv run pytest

# 5. Install pre-commit hooks
uv run pre-commit install
```

### Traditional Setup with pip

```bash
# 1. Clone repository
git clone https://github.com/usakocher/python-performance-monitor.git
cd python-performance-monitor

# 2. Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -e .
pip install -r requirements-dev.txt  # For development

# 4. Run tests
python -m pytest

# 5. Install pre-commit hooks
pre-commit install
```

## Development Commands

### With UV
| Task | Command |
|------|---------|
| Run tests | `uv run pytest` |
| Run tests with coverage | `uv run pytest --cov=pyperformance` |
| Format code | `uv run black .` |
| Check formatting | `uv run black --check .` |
| Lint code | `uv run flake8` |
| Sort imports | `uv run isort .` |
| Run pre-commit | `uv run pre-commit run --all-files` |
| Add dependency | `uv add requests` |
| Add dev dependency | `uv add --dev pytest-mock` |
| Update dependencies | `uv sync --upgrade` |

### With pip
| Task | Command |
|------|---------|
| Run tests | `python -m pytest` |
| Run tests with coverage | `python -m pytest --cov=pyperformance` |
| Format code | `black .` |
| Check formatting | `black --check .` |
| Lint code | `flake8` |
| Sort imports | `isort .` |
| Run pre-commit | `pre-commit run --all-files` |

## Why UV?

- **10-100x faster** dependency resolution than pip
- **Automatic virtual environment** management
- **Reproducible builds** with lockfiles
- **Modern Python packaging** standards
- **Better error messages** and debugging
- **Compatible** with existing pip workflows

## Features

### Function Timing
Track execution time with microsecond precision using Python's `perf_counter()`.

```python
@performance_monitor()
def timed_function():
    # Your code here
    pass
```

### Memory Monitoring
Monitor both peak memory usage and permanent memory allocations.

```python
@performance_monitor(track_memory=True)
def memory_function():
    big_data = [i for i in range(1000000)]
    return big_data
```

### Recursion Tracking
Intelligent monitoring of recursive functions that shows total time and recursive call count.

```python
@performance_monitor(track_recursion=True)
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)
```

### Silent Monitoring
Collect performance data without console output for production use.

```python
@performance_monitor(verbose=False)
def production_function():
    # Monitored silently
    pass

# Later, view collected data
show_performance_report()
```

### Error Handling
Track both successful and failed function calls with success rates.

```python
@performance_monitor()
def unreliable_function():
    import random
    if random.random() < 0.5:
        raise Exception("Random failure")
    return "success"
```

## Advanced Usage

### Custom Configuration

```python
# Minimal monitoring - timing only
@performance_monitor(track_memory=False, track_recursion=False)
def simple_timing():
    pass

# Comprehensive monitoring
@performance_monitor(track_memory=True, track_recursion=True, verbose=True)
def full_monitoring():
    pass
```

### Report Management

```python
from pyperformance import reset_performance_stats, get_performance_stats

# Get raw statistics for custom processing
stats = get_performance_stats()

# Reset all collected data
reset_performance_stats()
```

## Use Cases

### Development Workflow
Monitor functions during development to catch performance regressions early.

### Memory Leak Detection
Identify functions that permanently allocate memory vs. those that clean up properly.

### API Performance Testing
Track response times and memory usage of API endpoints.

### Algorithm Optimization
Compare performance of different implementations with detailed timing statistics.

## Performance Impact

PyPerformance is designed to have minimal overhead:
- Timing overhead: ~1-2 microseconds per function call
- Memory tracking overhead: ~5-10 microseconds when enabled
- No impact when monitoring is disabled

## Requirements

- Python 3.9+
- No external dependencies (uses only standard library)

## Troubleshooting

### UV Installation Issues

**macOS with Homebrew:**
```bash
brew install uv
```

**Windows:**
```powershell
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
```

**Using pip:**
```bash
pip install uv
```

### Common Issues

**"uv command not found"**
- Restart your terminal after installation
- Add UV to PATH: `echo 'export PATH="$HOME/.cargo/bin:$PATH"' >> ~/.bashrc`

**Dependencies not found**
- Make sure you're in the project directory
- Run `uv sync --all-extras` to install all dependencies

**Pre-commit not working**
- Reinstall hooks: `uv run pre-commit install`
- Clear cache: `uv run pre-commit clean`

## Documentation

- [Installation Guide](docs/installation.md)
- [Advanced Usage](docs/advanced_usage.md)
- [API Reference](docs/api_reference.md)

## Examples

Check out the [examples directory](examples/) for practical usage scenarios:
- [Basic Usage](examples/basic_usage.py)
- [Web Application Monitoring](examples/web_app_example.py)
- [Memory Analysis](examples/memory_analysis.py)

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

### Development Setup

```bash
git clone https://github.com/usakocher/python-performance-monitor.git
cd python-performance-monitor
uv sync --all-extras
uv run pytest
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Changelog

See [CHANGELOG.md](CHANGELOG.md) for version history and changes.

## Support

If you encounter any problems or have questions, please [open an issue](https://github.com/usakocher/python-performance-monitor/issues) on GitHub.
