"""
Basic usage examples for PyPerformance

This file demonstrates the core functionality of the performance monitor
in simple, easy-to-understand scenarios.
"""

from pyperformance import performance_monitor, show_performance_report, reset_performance_stats
import time
import random

# Example 1: Basic timing
@performance_monitor()
def slow_function():
    """A function that takes some time to execute"""
    time.sleep(0.1)
    return "Task completed"

# Example 2: Memory monitoring
@performance_monitor(track_memory=True)
def memory_intensive_function():
    """A function that uses significant memory"""
    # Create a large list
    data = [i * i for i in range(500000)]
    return len(data)

# Example 3: Recursion tracking
@performance_monitor(track_recursion=True)
def fibonacci(n):
    """Calculate fibonacci number recursively"""
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

# Example 4: Error handling
@performance_monitor()
def unreliable_function():
    """A function that sometimes fails"""
    if random.random() < 0.3:
        raise ValueError("Random failure occurred")
    time.sleep(0.05)
    return "Success"

# Example 5: Silent monitoring
@performance_monitor(verbose=False)
def background_task():
    """A function monitored silently for later analysis"""
    data = []
    for i in range(10000):
        data.append(i ** 2)
    return sum(data)

def main():
    """Run all examples and show results"""
    print("PyPerformance Basic Usage Examples")
    print("=" * 50)
    
    # Reset any previous data
    reset_performance_stats()
    
    print("\n1. Testing basic timing...")
    result1 = slow_function()
    print(f"Result: {result1}")
    
    print("\n2. Testing memory monitoring...")
    result2 = memory_intensive_function()
    print(f"Processed {result2} items")
    
    print("\n3. Testing recursion tracking...")
    result3 = fibonacci(10)
    print(f"Fibonacci(10) = {result3}")
    
    print("\n4. Testing error handling...")
    for i in range(5):
        try:
            result4 = unreliable_function()
            print(f"Attempt {i+1}: {result4}")
        except ValueError as e:
            print(f"Attempt {i+1}: Failed - {e}")
    
    print("\n5. Testing silent monitoring...")
    result5 = background_task()
    print(f"Background calculation result: {result5}")
    
    print("\n" + "=" * 50)
    print("COMPREHENSIVE PERFORMANCE REPORT")
    print("=" * 50)
    show_performance_report()

if __name__ == "__main__":
    main()