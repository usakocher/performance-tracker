# Installation Guide

## Requirements

PyPerformance requires Python 3.9 or higher and has no external dependencies.

### Supported Python Versions
- Python 3.9
- Python 3.10
- Python 3.11
- Python 3.12

### Supported Operating Systems
- Linux (all distributions)
- macOS (10.14+)
- Windows (10+)

## Installation Methods

### Install from PyPI

**Using pip (traditional):**
```bash
pip install pyperformance
```

**Using UV (recommended):**
```bash
# Install UV first (if not already installed)
curl -LsSf https://astral.sh/uv/install.sh | sh

# Add PyPerformance to your project
uv add pyperformance
```

**Using Poetry:**
```bash
poetry add pyperformance
```

### Install from Source

**Using UV:**
```bash
git clone https://github.com/usakocher/python-performance-monitor.git
cd python-performance-monitor
uv sync --all-extras
```

**Using pip:**
```bash
git clone https://github.com/usakocher/python-performance-monitor.git
cd python-performance-monitor
pip install -e .
```

## Development Installation

### UV Setup (Recommended)

UV is a modern Python package manager that's much faster than pip and provides better dependency management.

```bash
# 1. Install UV
curl -LsSf https://astral.sh/uv/install.sh | sh

# 2. Clone repository
git clone https://github.com/usakocher/python-performance-monitor.git
cd python-performance-monitor

# 3. Install all dependencies (automatically creates virtual environment)
uv sync --all-extras

# 4. Verify installation
uv run python -c "import pyperformance; print('Success!')"

# 5. Run tests
uv run pytest

# 6. Install pre-commit hooks
uv run pre-commit install
```

### Traditional pip Setup

```bash
# 1. Clone repository
git clone https://github.com/usakocher/python-performance-monitor.git
cd python-performance-monitor

# 2. Create virtual environment
python -m venv venv

# 3. Activate virtual environment
source venv/bin/activate  # Linux/macOS
# OR
venv\Scripts\activate     # Windows

# 4. Install in development mode
pip install -e .

# 5. Install development dependencies
pip install -r requirements-dev.txt

# 6. Run tests
python -m pytest

# 7. Install pre-commit hooks
pre-commit install
```

## Package Manager Comparison

| Feature | pip | UV | Poetry |
|---------|-----|----| -------|
| Speed | Baseline | 10-100x faster | 2-5x faster |
| Lockfiles | Manual | Automatic | Automatic |
| Virtual envs | Manual | Automatic | Automatic |
| Project management | Limited | Excellent | Excellent |
| Learning curve | Easy | Easy | Moderate |
| Maturity | Very mature | New (2024) | Mature |

## UV Installation Methods

### Primary Installation (Recommended)
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

### Alternative Methods

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

**Using conda:**
```bash
conda install -c conda-forge uv
```

## Verification

### Basic Verification
```python
from pyperformance import performance_monitor
print("PyPerformance installed successfully!")
```

### Full Development Verification

**With UV:**
```bash
cd python-performance-monitor
uv run python -c "
import pyperformance
from pyperformance import performance_monitor, show_performance_report
print('All imports successful!')
"
uv run pytest tests/test_monitor.py -v
```

**With pip:**
```bash
cd python-performance-monitor
python -c "
import pyperformance
from pyperformance import performance_monitor, show_performance_report
print('All imports successful!')
"
python -m pytest tests/test_monitor.py -v
```

## Troubleshooting

### UV Issues

**"uv command not found" after installation:**
```bash
# Restart terminal or reload shell
source ~/.bashrc  # Linux
source ~/.zshrc   # macOS with zsh

# Or add to PATH manually
export PATH="$HOME/.cargo/bin:$PATH"
```

**Permission denied on installation:**
```bash
# Try with user installation
pip install --user uv
```

**UV sync fails:**
```bash
# Clear cache and retry
uv cache clean
uv sync --all-extras
```

### General Issues

**ImportError: No module named 'pyperformance'**
- Ensure you're in the correct virtual environment
- Verify installation: `pip list | grep pyperformance` or `uv list | grep pyperformance`

**Python version incompatibility**
- Check Python version: `python --version`
- PyPerformance requires Python 3.9 or higher

**Tests failing**
- Ensure all development dependencies are installed
- Check that you're in the project root directory
- Try running a single test: `uv run pytest tests/test_monitor.py::TestPerformanceMonitor::test_basic_timing -v`

### Getting Help

If you encounter issues:

1. Check the [FAQ](faq.md)
2. Search [existing issues](https://github.com/usakocher/python-performance-monitor/issues)
3. Create a [new issue](https://github.com/usakocher/python-performance-monitor/issues/new) with:
   - Python version (`python --version`)
   - Operating system
   - Installation method used
   - Complete error message
   - Steps to reproduce
