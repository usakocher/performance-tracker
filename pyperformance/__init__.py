"""
PyPerformance - A lightweight Python performance monitoring library
"""

from .monitor import (
    performance_monitor, 
    show_performance_report, 
    reset_performance_stats, 
    get_performance_stats
)

__version__ = "0.1.0"
__author__ = "Your Name"
__email__ = "your.email@example.com"

__all__ = [
    "performance_monitor",
    "show_performance_report", 
    "reset_performance_stats",
    "get_performance_stats"
]