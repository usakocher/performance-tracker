import tracemalloc
from time import perf_counter, sleep
from threading import local

# Global storage for performance data
performance_stats = {}
_local = local()

def _init_function_stats(func_name):
    """Initialize stats for a function if not exists"""
    if func_name not in performance_stats:
        performance_stats[func_name] = {
            'call_count': 0,
            'total_time': 0.0,
            'min_time': float('inf'),
            'max_time': 0.0,
            'times': [],
            'total_memory_used': 0.0,
            'max_memory_peak': 0.0,
            'memory_peaks': [],
            'success_count': 0,
            'failure_count': 0
        }

def _record_function_stats(func_name, duration, memory_used, memory_peak, success):
    """Record performance data for a function call"""
    stats = performance_stats[func_name]
    
    # Update timing stats
    stats['total_time'] += duration
    stats['min_time'] = min(stats['min_time'], duration)
    stats['max_time'] = max(stats['max_time'], duration)
    stats['times'].append(duration)
    
    # Update memory stats
    stats['total_memory_used'] += memory_used
    stats['max_memory_peak'] = max(stats['max_memory_peak'], memory_peak)
    stats['memory_peaks'].append(memory_peak)
    
    # Update success/failure counts
    if success:
        stats['success_count'] += 1
    else:
        stats['failure_count'] += 1

def performance_monitor(track_recursion=True, track_memory=True, verbose=True):
    def decorator(func):
        def wrapper(*args, **kwargs):
            func_name = func.__name__
            
            # Initialize stats for this function
            _init_function_stats(func_name)
            
            if track_recursion:
                # Complex recursion tracking logic
                recursion_key = f"_in_{func_name}"
                is_recursive_call = getattr(_local, recursion_key, False)
                
                if not is_recursive_call:
                    # Top-level call with recursion tracking
                    setattr(_local, recursion_key, True)
                    setattr(_local, f"_recursive_count_{func_name}", 0)
                    
                    # Memory tracking setup for top-level call
                    if track_memory:
                        if not tracemalloc.is_tracing():
                            tracemalloc.start()
                        tracemalloc.clear_traces()
                        start_memory = tracemalloc.get_traced_memory()[0]
                    
                    start_time = perf_counter()
                    try:
                        result = func(*args, **kwargs)
                        success = True
                    except Exception:
                        success = False
                        raise
                    finally:
                        end_time = perf_counter()
                        duration = end_time - start_time
                        recursive_count = getattr(_local, f"_recursive_count_{func_name}", 0)
                        
                        # Memory calculations
                        memory_used = 0.0
                        memory_peak = 0.0
                        if track_memory:
                            current_memory, peak_memory = tracemalloc.get_traced_memory()
                            memory_used = (current_memory - start_memory) / 1024 / 1024  # MB
                            memory_peak = peak_memory / 1024 / 1024  # MB
                        
                        # Record stats and count this top-level call
                        _record_function_stats(func_name, duration, memory_used, memory_peak, success)
                        performance_stats[func_name]['call_count'] += 1
                        
                        # Print verbose output if enabled
                        if verbose:
                            memory_info = ""
                            if track_memory:
                                memory_info = f", memory: {memory_used:.2f}MB used, {memory_peak:.2f}MB peak"
                            
                            status = "succeeded" if success else "failed"
                            times_text = "time" if performance_stats[func_name]['call_count'] == 1 else "times"
                            print(f"Function {func_name} {status} in {duration:.4f} seconds{memory_info} "
                                  f"(called {performance_stats[func_name]['call_count']} {times_text}, recursive calls: {recursive_count})")
                        
                        setattr(_local, recursion_key, False)
                    return result
                else:
                    # Recursive call - no timing or memory tracking
                    current_count = getattr(_local, f"_recursive_count_{func_name}", 0)
                    setattr(_local, f"_recursive_count_{func_name}", current_count + 1)
                    return func(*args, **kwargs)
            else:
                # Simple mode - time and track memory for every call
                # Memory tracking setup
                if track_memory:
                    if not tracemalloc.is_tracing():
                        tracemalloc.start()
                    tracemalloc.clear_traces()
                    start_memory = tracemalloc.get_traced_memory()[0]
                
                start_time = perf_counter()
                try:
                    result = func(*args, **kwargs)
                    success = True
                except Exception:
                    success = False
                    raise
                finally:
                    end_time = perf_counter()
                    duration = end_time - start_time
                    
                    # Memory calculations
                    memory_used = 0.0
                    memory_peak = 0.0
                    if track_memory:
                        current_memory, peak_memory = tracemalloc.get_traced_memory()
                        memory_used = (current_memory - start_memory) / 1024 / 1024  # MB
                        memory_peak = peak_memory / 1024 / 1024  # MB
                    
                    # Record stats and count this call
                    _record_function_stats(func_name, duration, memory_used, memory_peak, success)
                    performance_stats[func_name]['call_count'] += 1
                    
                    # Print verbose output if enabled
                    if verbose:
                        memory_info = ""
                        if track_memory:
                            memory_info = f", memory: {memory_used:.2f}MB used, {memory_peak:.2f}MB peak"
                        
                        status = "succeeded" if success else "failed"
                        times_text = "time" if performance_stats[func_name]['call_count'] == 1 else "times"
                        print(f"Function {func_name} {status} in {duration:.4f} seconds{memory_info} (called {performance_stats[func_name]['call_count']} {times_text})")
                
                return result
        return wrapper
    return decorator

def show_performance_report():
    """Display a comprehensive performance report for all monitored functions"""
    if not performance_stats:
        print("No performance data collected yet.")
        return
    
    print("\n" + "="*80)
    print("PERFORMANCE REPORT")
    print("="*80)
    
    for func_name, stats in performance_stats.items():
        print(f"\nFunction: {func_name}")
        print("-" * 40)
        
        # Call statistics
        total_calls = stats['call_count']
        success_rate = (stats['success_count'] / total_calls * 100) if total_calls > 0 else 0
        print(f"Total Calls: {total_calls}")
        print(f"Success Rate: {success_rate:.1f}% ({stats['success_count']} succeeded, {stats['failure_count']} failed)")
        
        # Timing statistics
        if stats['times']:
            avg_time = stats['total_time'] / len(stats['times'])
            print(f"Timing:")
            print(f"  Total Time: {stats['total_time']:.4f} seconds")
            print(f"  Average Time: {avg_time:.4f} seconds")
            print(f"  Min Time: {stats['min_time']:.4f} seconds")
            print(f"  Max Time: {stats['max_time']:.4f} seconds")
        
        # Memory statistics
        if stats['memory_peaks']:
            avg_peak = sum(stats['memory_peaks']) / len(stats['memory_peaks'])
            print(f"Memory:")
            print(f"  Total Memory Used: {stats['total_memory_used']:.2f} MB")
            print(f"  Average Peak: {avg_peak:.2f} MB")
            print(f"  Max Peak: {stats['max_memory_peak']:.2f} MB")

def reset_performance_stats():
    """Clear all performance statistics"""
    global performance_stats
    performance_stats.clear()
    print("Performance statistics reset.")

def get_performance_stats():
    """Return raw performance statistics for custom processing"""
    return performance_stats.copy()

# Test functions
@performance_monitor(track_recursion=False, track_memory=True, verbose=True)
def simple_function():
    sleep(0.1)
    return "done"

@performance_monitor(track_memory=True, verbose=True)
def memory_heavy_function():
    big_list = [i for i in range(1000000)]
    return len(big_list)

@performance_monitor(track_memory=True, verbose=True)
def recursive_factorial(n):
    if n <= 1:
        return 1
    return n * recursive_factorial(n - 1)

# Global variable to test memory retention
memory_keeper = []

@performance_monitor(track_memory=True, verbose=True)
def function_that_keeps_memory():
    big_list = [i for i in range(500000)]
    memory_keeper.append(big_list)
    return len(big_list)

@performance_monitor(track_memory=True, verbose=True)  
def function_that_releases_memory():
    big_list = [i for i in range(500000)]
    return len(big_list)

# Example usage
if __name__ == "__main__":
    print("Running performance tests...")
    
    # Test each function multiple times
    simple_function()
    simple_function()
    
    memory_heavy_function()
    memory_heavy_function()
    
    recursive_factorial(5)
    recursive_factorial(3)
    
    function_that_keeps_memory()
    function_that_releases_memory()
    function_that_keeps_memory()
    
    # Show the comprehensive report
    show_performance_report()
    
    print("\n" + "="*50)
    print("Testing report functions...")
    
    # Test reset functionality
    print("\nResetting stats...")
    reset_performance_stats()
    
    # Verify reset worked
    show_performance_report()