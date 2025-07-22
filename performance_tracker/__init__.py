"""
Performance Tracker - Professional Performance Monitoring for Python Applications

A lightweight, developer-friendly library that provides real-time insights into
function execution time, memory usage, and call patterns using simple decorators.

Key Features:
    - Zero-configuration monitoring with @performance_monitor() decorator
    - Real-time feedback and comprehensive reporting
    - Memory leak detection and analysis
    - Recursion-aware tracking for complex algorithms
    - Thread-safe operation for concurrent applications
    - Minimal performance overhead (~1-2 μs per function call)

For complete documentation, visit:
https://github.com/usakocher/python-performance-monitor
"""

from typing import TYPE_CHECKING

from .monitor import (
    get_performance_stats,
    performance_monitor,
    reset_performance_stats,
    show_performance_report,
)

if TYPE_CHECKING:
    from typing import Any, Callable, Dict, TypeVar

    # Type aliases for better IDE support
    PerformanceStats = Dict[str, Dict[str, Any]]
    MonitoredFunction = TypeVar("MonitoredFunction", bound=Callable[..., Any])

__version__ = "1.0.1"
__author__ = "Adam Kocher"

__all__ = [
    "performance_monitor",
    "show_performance_report",
    "reset_performance_stats",
    "get_performance_stats",
    # Type exports for advanced users
    "PerformanceStats",
    "MonitoredFunction",
]

# Module-level docstring attributes for better IDE discovery
performance_monitor.__module__ = __name__
show_performance_report.__module__ = __name__
reset_performance_stats.__module__ = __name__
get_performance_stats.__module__ = __name__
