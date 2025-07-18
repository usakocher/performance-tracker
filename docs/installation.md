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

### Install from PyPI (Recommended)

```bash
pip install pyperformance
```

### Install from Source

```bash
git clone https://github.com/yourusername/python-performance-monitor.git
cd python-performance-monitor
pip install -e .
```

### Install for Development

```bash
git clone https://github.com/yourusername/python-performance-monitor.git
cd python-performance-monitor
pip install -r requirements-dev.txt
pip install -e .
```

## Verification

Verify your installation by running:

```python
from pyperformance import performance_monitor
print("PyPerformance installed successfully!")
```

## Virtual Environment Setup

We recommend using a virtual environment:

```bash
# Create virtual environment
python -m venv pyperformance-env

# Activate (Linux/macOS)
source pyperformance-env/bin/activate

# Activate (Windows)
pyperformance-env\Scripts\activate

# Install PyPerformance
pip install pyperformance
```

## Troubleshooting

### Common Issues

**ImportError: No module named 'pyperformance'**
- Make sure you've activated the correct virtual environment
- Verify installation with `pip list | grep pyperformance`

**Permission denied during installation**
- Use `pip install --user pyperformance` to install for current user only
- Or use `sudo pip install pyperformance` (not recommended)

**Python version incompatibility**
- Check your Python version: `python --version`
- PyPerformance requires Python 3.9 or higher
