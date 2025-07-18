# API Reference

## Decorators

### `@performance_monitor()`

The main decorator for monitoring function performance.

**Signature:**
```python
performance_monitor(track_recursion=True, track_memory=True, verbose=True)
```

**Parameters:**
- `track_recursion` (bool): Enable recursion-aware monitoring. Default: `True`
- `track_memory` (bool): Enable memory usage tracking. Default: `True`
- `verbose` (bool): Enable real-time console output. Default: `True`

**Returns:**
- Decorated function with monitoring capabilities

**Example:**
```python
@performance_monitor(track_memory=True, verbose=False)
def my_function():
    return "Hello, World!"
```

## Reporting Functions

### `show_performance_report()`

Display a comprehensive performance report for all monitored functions.

**Signature:**
```python
show_performance_report() -> None
```

**Output Format:**
```
================================================================================
PERFORMANCE REPORT
================================================================================

Function: function_name
----------------------------------------
Total Calls: 5
Success Rate: 100.0% (5 succeeded, 0 failed)
Timing:
  Total Time: 0.5234 seconds
  Average Time: 0.1047 seconds
  Min Time: 0.0987 seconds
  Max Time: 0.1123 seconds
Memory:
  Total Memory Used: 0.00 MB
  Average Peak: 15.23 MB
  Max Peak: 18.45 MB
```

### `reset_performance_stats()`

Clear all collected performance statistics.

**Signature:**
```python
reset_performance_stats() -> None
```

**Usage:**
```python
reset_performance_stats()
print("Statistics cleared.")
```

### `get_performance_stats()`

Get raw performance statistics for programmatic access.

**Signature:**
```python
get_performance_stats() -> dict
```

**Returns:**
Dictionary containing performance data for all monitored functions.

**Return Structure:**
```python
{
    'function_name': {
        'call_count': int,
        'total_time': float,
        'min_time': float,
        'max_time': float,
        'times': list[float],
        'total_memory_used': float,
        'max_memory_peak': float,
        'memory_peaks': list[float],
        'success_count': int,
        'failure_count': int
    }
}
```

**Example:**
```python
stats = get_performance_stats()
for func_name, data in stats.items():
    print(f"{func_name}: {data['call_count']} calls")
```

## Data Structures

### Performance Statistics Schema

Each monitored function generates the following statistics:

| Field | Type | Description |
|-------|------|-------------|
| `call_count` | int | Total number of function calls |
| `total_time` | float | Cumulative execution time (seconds) |
| `min_time` | float | Fastest execution time (seconds) |
| `max_time` | float | Slowest execution time (seconds) |
| `times` | list[float] | Individual execution times |
| `total_memory_used` | float | Net memory allocated (MB) |
| `max_memory_peak` | float | Highest memory usage (MB) |
| `memory_peaks` | list[float] | Peak memory for each call |
| `success_count` | int | Number of successful calls |
| `failure_count` | int | Number of failed calls |

### Calculated Metrics

You can derive additional metrics from the raw data:

```python
stats = get_performance_stats()['my_function']

# Average execution time
avg_time = stats['total_time'] / stats['call_count']

# Success rate percentage
success_rate = stats['success_count'] / stats['call_count'] * 100

# Average peak memory
avg_memory = sum(stats['memory_peaks']) / len(stats['memory_peaks'])

# Standard deviation of execution times
import statistics
time_std_dev = statistics.stdev(stats['times'])
```

## Error Handling

PyPerformance handles function exceptions gracefully:

```python
@performance_monitor()
def failing_function():
    raise ValueError("Something went wrong")

try:
    failing_function()
except ValueError:
    pass

# Statistics still recorded:
# - failure_count incremented
# - Execution time measured
# - Exception re-raised normally
```

## Thread Safety

All PyPerformance functions are thread-safe:
- Global statistics use thread-safe data structures
- Recursion tracking uses thread-local storage
- Multiple threads can monitor functions simultaneously

## Memory Management

PyPerformance manages memory efficiently:
- Statistics stored in memory only (no disk I/O)
- Memory usage scales with number of monitored functions
- Use `reset_performance_stats()` to free memory in long-running applications

## Version Compatibility

| PyPerformance Version | Python Versions | Features |
|----------------------|-----------------|----------|
| 0.1.0+ | 3.9+ | All current features |

## Limitations

1. **Memory tracking accuracy**: Uses `tracemalloc`, which tracks Python object allocations only
2. **Overhead**: Monitoring adds small performance overhead (~1-10 microseconds per call)
3. **Thread-local recursion**: Recursion tracking is per-thread, not global
4. **No persistence**: Statistics are lost when process ends

## Examples

### Basic Usage
```python
from pyperformance import performance_monitor

@performance_monitor()
def example_function():
    import time
    time.sleep(0.1)
    return "done"

result = example_function()
```

### Advanced Configuration
```python
@performance_monitor(
    track_recursion=False,  # Disable recursion tracking
    track_memory=True,      # Enable memory monitoring
    verbose=False          # Silent operation
)
def advanced_function():
    return [i**2 for i in range(100000)]
```

### Custom Analysis
```python
from pyperformance import get_performance_stats

def analyze_performance():
    stats = get_performance_stats()

    for func_name, data in stats.items():
        if data['call_count'] > 0:
            avg_time = data['total_time'] / data['call_count']
            print(f"{func_name}: {avg_time:.4f}s average")
```
