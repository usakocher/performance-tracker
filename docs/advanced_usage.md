# Advanced Usage Guide

## Configuration Options

### Decorator Parameters

The `@performance_monitor()` decorator accepts several parameters for customization:

```python
@performance_monitor(
    track_recursion=True,    # Enable/disable recursion tracking
    track_memory=True,       # Enable/disable memory monitoring
    verbose=True            # Enable/disable console output
)
def my_function():
    pass
```

### Parameter Details

#### `track_recursion` (bool, default=True)
Controls how recursive functions are monitored:

```python
# With recursion tracking (default)
@performance_monitor(track_recursion=True)
def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)

# Output shows: "called 1 time, recursive calls: 4"

# Without recursion tracking
@performance_monitor(track_recursion=False)
def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)

# Output shows: "called 5 times" (each recursive call counted)
```

#### `track_memory` (bool, default=True)
Controls memory usage monitoring:

```python
# With memory tracking (default)
@performance_monitor(track_memory=True)
def memory_function():
    return [i for i in range(100000)]

# Output includes: "memory: 0.00MB used, 3.81MB peak"

# Without memory tracking
@performance_monitor(track_memory=False)
def memory_function():
    return [i for i in range(100000)]

# Output: just timing information
```

#### `verbose` (bool, default=True)
Controls real-time console output:

```python
# With verbose output (default)
@performance_monitor(verbose=True)
def my_function():
    pass

# Prints performance info immediately

# Silent monitoring
@performance_monitor(verbose=False)
def my_function():
    pass

# No immediate output, data collected for later analysis
```

## Data Management

### Accessing Raw Statistics

```python
from performance-tracker import get_performance_stats

# Get all collected data
stats = get_performance_stats()

# Access specific function data
function_stats = stats['my_function']
print(f"Total calls: {function_stats['call_count']}")
print(f"Average time: {function_stats['total_time'] / len(function_stats['times'])}")
```

### Resetting Statistics

```python
from performance-tracker import reset_performance_stats

# Clear all collected data
reset_performance_stats()

# Useful for:
# - Starting fresh analysis
# - Clearing data between test runs
# - Preventing memory buildup in long-running applications
```

### Custom Report Generation

```python
from performance-tracker import get_performance_stats

def generate_custom_report():
    stats = get_performance_stats()

    print("Custom Performance Analysis")
    print("-" * 40)

    for func_name, data in stats.items():
        if data['call_count'] > 0:
            avg_time = data['total_time'] / data['call_count']
            print(f"{func_name}:")
            print(f"  Average time: {avg_time:.4f}s")
            print(f"  Success rate: {data['success_count']/data['call_count']*100:.1f}%")

            if data['memory_peaks']:
                avg_memory = sum(data['memory_peaks']) / len(data['memory_peaks'])
                print(f"  Average memory: {avg_memory:.2f}MB")
```

## Integration Patterns

### Web Applications

```python
from flask import Flask
from performance-tracker import performance_monitor

app = Flask(__name__)

@app.route('/api/data')
@performance_monitor(verbose=False)  # Silent in production
def get_data():
    # Your API logic here
    return {"data": "response"}

# Monitor performance via separate endpoint
@app.route('/admin/performance')
def performance_dashboard():
    from performance-tracker import show_performance_report
    import io, sys

    old_stdout = sys.stdout
    sys.stdout = buffer = io.StringIO()
    show_performance_report()
    sys.stdout = old_stdout

    return f"<pre>{buffer.getvalue()}</pre>"
```

### Testing Integration

```python
import pytest
from performance-tracker import performance_monitor, reset_performance_stats, get_performance_stats

class TestPerformance:
    def setup_method(self):
        reset_performance_stats()

    def test_function_performance(self):
        @performance_monitor(verbose=False)
        def test_function():
            # Function under test
            pass

        # Run multiple times
        for _ in range(10):
            test_function()

        # Assert performance criteria
        stats = get_performance_stats()['test_function']
        avg_time = stats['total_time'] / stats['call_count']
        assert avg_time < 0.001, f"Function too slow: {avg_time}s"
```

### Batch Processing

```python
from performance-tracker import performance_monitor, show_performance_report

@performance_monitor(track_memory=True)
def process_batch(items):
    results = []
    for item in items:
        # Process each item
        result = expensive_operation(item)
        results.append(result)
    return results

# Process multiple batches
for batch in data_batches:
    process_batch(batch)

# Analyze performance across all batches
show_performance_report()
```

## Performance Optimization Tips

### Monitoring Overhead

Performance-Tracker is designed to be lightweight, but monitoring does add some overhead:

- **Timing only**: ~1-2 microseconds per call
- **With memory tracking**: ~5-10 microseconds per call
- **With recursion tracking**: ~2-3 microseconds per call

### Best Practices

1. **Use `verbose=False` in production** to reduce I/O overhead
2. **Reset stats periodically** in long-running applications
3. **Monitor selectively** - don't monitor every function
4. **Batch analysis** - collect data over time, then analyze

### Memory Considerations

```python
# Good: Monitor high-level functions
@performance_monitor()
def process_user_request():
    helper_function_1()
    helper_function_2()
    return result

# Avoid: Monitoring every small function
@performance_monitor()  # Too granular
def add_numbers(a, b):
    return a + b
```

## Thread Safety

Performance-Tracker uses thread-local storage for recursion tracking, making it safe for multi-threaded applications:

```python
import threading
from performance-tracker import performance_monitor

@performance_monitor()
def threaded_function(thread_id):
    time.sleep(0.1)
    return f"Thread {thread_id} complete"

# Safe to use in multiple threads
threads = []
for i in range(5):
    t = threading.Thread(target=threaded_function, args=(i,))
    threads.append(t)
    t.start()

for t in threads:
    t.join()

show_performance_report()
```
