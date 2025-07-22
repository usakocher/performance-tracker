# Frequently Asked Questions

## General Questions

### What is Performance-Tracker?

Performance-Tracker is a lightweight Python library for monitoring function performance. It provides real-time insights into execution time, memory usage, and call patterns using a simple decorator syntax.

### How is Performance-Tracker different from other profiling tools?

**Compared to cProfile:**
- Much lower overhead (~12x faster)
- Real-time feedback instead of post-execution analysis
- Memory tracking included
- Decorator-based (no code restructuring needed)

**Compared to py-spy:**
- Per-function granularity
- Memory leak detection
- No external process required
- Built-in reporting system

**Compared to memory_profiler:**
- 5x lower overhead
- Combined timing and memory analysis
- Thread-safe operation
- Better integration with development workflow

### Is Performance-Tracker suitable for production use?

Yes, with proper configuration:
- Use `verbose=False` to minimize I/O overhead
- Disable memory tracking if not needed: `track_memory=False`
- Monitor selectively (don't monitor every function)
- Reset statistics periodically in long-running applications

Production overhead is typically <0.1% for reasonable function execution times.

## Installation and Setup

### What Python versions are supported?

Performance-Tracker supports Python 3.9 and newer. We test on:
- Python 3.9, 3.10, 3.11, 3.12
- Linux, macOS, and Windows
- CPython (other implementations not tested)

### Does Performance-Tracker have external dependencies?

No. Performance-Tracker uses only Python's standard library, specifically:
- `time.perf_counter()` for timing
- `tracemalloc` for memory tracking
- `threading.local` for thread safety

### Why can't I install Performance-Tracker?

**Common solutions:**
1. **Check Python version:** `python --version` (must be 3.9+)
2. **Update pip:** `pip install --upgrade pip`
3. **Use virtual environment:** Avoid system-wide installation conflicts
4. **Check network:** Firewall might block PyPI access

## Usage Questions

### How do I monitor a function?

Simple - just add the decorator:

```python
from performance-tracker import performance_monitor

@performance_monitor()
def my_function():
    # Your code here
    pass
```

### Can I monitor class methods?

Yes, Performance-Tracker works with any callable:

```python
class MyClass:
    @performance_monitor()
    def method(self):
        pass

    @performance_monitor()
    @staticmethod
    def static_method():
        pass

    @performance_monitor()
    @classmethod
    def class_method(cls):
        pass
```

### How do I monitor async functions?

Currently, Performance-Tracker doesn't have special async support, but it works with async functions:

```python
import asyncio

@performance_monitor()
async def async_function():
    await asyncio.sleep(0.1)
    return "done"

# Note: Timing includes the entire async operation
```

Dedicated async support is planned for a future release.

### Can I monitor lambda functions?

Lambda functions work, but the name will be `<lambda>`:

```python
# Works but not very useful
monitored_lambda = performance_monitor()(lambda x: x * 2)

# Better approach - use a named function
@performance_monitor()
def multiply_by_two(x):
    return x * 2
```

### How do I get statistics without console output?

Use `verbose=False` and access data programmatically:

```python
@performance_monitor(verbose=False)
def quiet_function():
    pass

# Run your function
quiet_function()

# Get statistics
from performance-tracker import get_performance_stats
stats = get_performance_stats()
print(stats['quiet_function'])
```

## Memory Monitoring

### Why does my function show 0.00MB used but high peak memory?

This is normal Python behavior. Performance-Tracker distinguishes between:
- **Peak memory:** Maximum memory during execution
- **Used memory:** Net memory still allocated when function ends

Example:
```python
@performance_monitor(track_memory=True)
def temporary_memory():
    big_list = [i for i in range(1000000)]  # Peak: ~38MB
    return len(big_list)  # big_list gets garbage collected
    # Used: 0.00MB, Peak: 38MB
```

For memory leaks, you'll see positive "used" values.

### How accurate is memory tracking?

Memory tracking uses Python's `tracemalloc` module:
- **Accurate for:** Python object allocations
- **Not tracked:** C extension memory, system allocations
- **Precision:** Byte-level accuracy for Python objects

For most Python applications, this captures the majority of memory usage.

### Can I track memory for specific operations?

Not directly, but you can structure your code:

```python
@performance_monitor(track_memory=True)
def load_data():
    return expensive_data_loading()

@performance_monitor(track_memory=True)
def process_data(data):
    return expensive_processing(data)
```

## Performance and Overhead

### What's the performance overhead?

Typical overhead per function call:
- **Timing only:** ~1-2 microseconds
- **With memory tracking:** ~5-10 microseconds
- **All features:** ~8-12 microseconds

For context, this is negligible unless you're calling functions millions of times per second.

### Should I monitor every function?

No. Best practices:
- Monitor business logic and slow operations
- Skip very fast utility functions
- Focus on functions you're optimizing
- Use selective monitoring in production

### Does Performance-Tracker affect my function's return value?

No. Performance-Tracker preserves your function's original behavior:
- Return values pass through unchanged
- Exceptions are re-raised normally
- Function signature remains the same

### Can I disable monitoring temporarily?

Yes, several options:

```python
# Conditional decorator
DEBUG = True
@performance_monitor() if DEBUG else lambda f: f
def my_function():
    pass

# Environment-based
import os
if os.getenv('MONITOR_PERFORMANCE'):
    monitor = performance_monitor()
else:
    monitor = lambda f: f

@monitor
def my_function():
    pass
```

## Recursion and Threading

### How does recursion tracking work?

Performance-Tracker distinguishes between logical calls (your code) and recursive calls:

```python
@performance_monitor(track_recursion=True)
def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)

factorial(5)  # Shows: "called 1 time, recursive calls: 4"
```

Without recursion tracking, it would show "called 5 times".

### Is Performance-Tracker thread-safe?

Yes. Performance-Tracker uses:
- Thread-safe global statistics storage
- Thread-local storage for recursion tracking
- No shared mutable state between threads

Each thread's recursive calls are tracked independently.

### Can multiple threads monitor the same function?

Yes. Statistics are aggregated across all threads:

```python
@performance_monitor()
def threaded_function(thread_id):
    time.sleep(0.1)

# Called from 5 threads = 5 total calls in statistics
```

## Error Handling and Debugging

### What happens if my monitored function raises an exception?

Performance-Tracker handles exceptions gracefully:
- Exception is re-raised normally (your error handling still works)
- Function call is counted as failed
- Execution time is still measured
- Statistics include success/failure rates

### Why am I getting import errors?

Common issues:
1. **Wrong Python version:** Check `python --version`
2. **Virtual environment:** Make sure Performance-Tracker is installed in active environment
3. **Module name:** Import from `performance-tracker`, not `performance-tracker`

### My statistics seem wrong. What should I check?

1. **Reset between tests:** Use `reset_performance_stats()`
2. **Check function names:** Verify you're looking at the right function
3. **Thread safety:** Multiple threads aggregate statistics
4. **Recursion mode:** Check if `track_recursion` affects your results

## Integration and Compatibility

### Can I use Performance-Tracker with Flask/Django?

Yes! Example Flask integration:

```python
from flask import Flask
from performance-tracker import performance_monitor

app = Flask(__name__)

@app.route('/api/data')
@performance_monitor(verbose=False)
def get_data():
    return {"data": "response"}
```

See `examples/web_app_example.py` for complete examples.

### Does Performance-Tracker work with pytest?

Yes, great for performance testing:

```python
def test_function_performance():
    @performance_monitor(verbose=False)
    def test_func():
        # Function under test
        pass

    # Run and assert performance criteria
    test_func()
    stats = get_performance_stats()['test_func']
    assert stats['total_time'] < 0.001
```

### Can I integrate with logging frameworks?

Not built-in, but you can create custom reporters:

```python
import logging
from performance-tracker import get_performance_stats

def log_performance_stats():
    stats = get_performance_stats()
    for func_name, data in stats.items():
        avg_time = data['total_time'] / data['call_count']
        logging.info(f"{func_name}: {avg_time:.4f}s average")
```

## Data Management

### How long are statistics stored?

Statistics persist in memory until:
- Process ends
- `reset_performance_stats()` is called
- Python garbage collection (automatic memory management)

### Can I save statistics to a file?

Not built-in, but easy to implement:

```python
import json
from performance-tracker import get_performance_stats

# Save to JSON
stats = get_performance_stats()
with open('performance_data.json', 'w') as f:
    json.dump(stats, f, indent=2)

# Save to CSV
import pandas as pd
df = pd.DataFrame(stats).T
df.to_csv('performance_data.csv')
```

### Can I merge statistics from multiple runs?

You can combine data manually:

```python
# Run 1
run_functions()
stats1 = get_performance_stats()

# Run 2
reset_performance_stats()
run_functions()
stats2 = get_performance_stats()

# Combine (custom logic needed)
combined_stats = merge_performance_stats(stats1, stats2)
```

Built-in merging is planned for a future release.

## Future Development

### What features are planned?

**Version 0.2.0:**
- Async function support
- JSON/CSV output formats
- Performance regression detection

**Version 0.3.0:**
- Historical data storage
- Web dashboard
- CI/CD integration

**Version 1.0.0:**
- C extension for minimal overhead
- Distributed monitoring
- Advanced visualization

### How can I request a feature?

1. Check existing [GitHub issues](https://github.com/usakocher/performance-tracker/issues)
2. Open a new issue with the "feature request" template
3. Describe your use case and proposed solution
4. Participate in discussion and design

### Can I contribute?

Absolutely! See [contributing.md](contributing.md) for:
- Development setup
- Coding standards
- Pull request process
- Areas needing help

Contributions welcome from developers of all experience levels.

## Troubleshooting

### Performance-Tracker isn't showing any output

Check:
1. **Verbose mode:** Use `verbose=True` (default)
2. **Function calls:** Make sure you're actually calling the decorated function
3. **Import:** Verify `from performance-tracker import performance_monitor`

### Statistics are accumulating unexpectedly

- Use `reset_performance_stats()` between test runs
- Check if multiple threads are calling the same function
- Verify you're not monitoring recursive helper functions

### Memory numbers seem too high/low

- Memory tracking shows Python object allocations only
- Peak memory is cumulative during function execution
- Used memory is net allocation (can be negative if garbage collected)

### Performance overhead is too high

- Use `verbose=False` in performance-critical code
- Disable memory tracking: `track_memory=False`
- Monitor fewer functions
- Check if you're monitoring very fast functions (high percentage overhead)

## Getting Help

### Where can I get support?

1. **Documentation:** Start with [docs/](https://github.com/usakocher/performance-tracker/tree/main/docs)
2. **GitHub Issues:** Bug reports and feature requests
3. **GitHub Discussions:** Questions and community help
4. **Email:** Direct contact for complex issues

### How do I report a bug?

1. Check existing issues first
2. Use the bug report template
3. Include minimal reproduction code
4. Specify Python version and environment

### How do I suggest improvements?

1. Open a GitHub issue with "enhancement" label
2. Describe the problem you're trying to solve
3. Propose a solution if you have one
4. Discuss with maintainers and community
