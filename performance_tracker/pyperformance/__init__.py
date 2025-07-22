"""
Performance-Tracker - A lightweight Python performance monitoring library
"""

from .monitor import (
    get_performance_stats,
    performance_monitor,
    reset_performance_stats,
    show_performance_report,
)

__version__ = "1.0.0"
__author__ = "Adam Kocher"

__all__ = [
    "performance_monitor",
    "show_performance_report",
    "reset_performance_stats",
    "get_performance_stats",
]
