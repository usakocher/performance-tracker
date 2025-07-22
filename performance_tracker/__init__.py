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
