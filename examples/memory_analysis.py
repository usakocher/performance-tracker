"""
Memory analysis examples using Performance-Tracker

This demonstrates how to use Performance-Tracker to detect and analyze
different types of memory usage patterns.
"""

import gc

from performance_tracker import (
    performance_monitor,
    reset_performance_stats,
    show_performance_report,
)

# Global storage to demonstrate memory leaks
memory_holder = []


@performance_monitor(track_memory=True)
def memory_leak_function():
    """Function that permanently allocates memory"""
    # Create data and store reference globally
    data = [i for i in range(100000)]
    memory_holder.append(data)
    return len(data)


@performance_monitor(track_memory=True)
def temporary_memory_function():
    """Function that uses memory temporarily"""
    # Create large data structure
    data = [i for i in range(100000)]
    # Process it
    result = sum(data)
    # data goes out of scope and gets garbage collected
    return result


@performance_monitor(track_memory=True)
def efficient_memory_function():
    """Function that uses memory efficiently"""
    # Use generator for memory efficiency
    result = sum(i for i in range(100000))
    return result


@performance_monitor(track_memory=True)
def nested_data_function():
    """Function that creates nested data structures"""
    data = {"level1": {"level2": {"data": [i**2 for i in range(50000)]}}}
    return len(data["level1"]["level2"]["data"])


@performance_monitor(track_memory=True, track_recursion=True)
def recursive_memory_function(depth, data_size=1000):
    """Recursive function that allocates memory at each level"""
    if depth <= 0:
        return []

    # Allocate memory at this level
    local_data = list(range(data_size))

    # Recurse
    nested_result = recursive_memory_function(depth - 1, data_size)

    return local_data + nested_result


def analyze_memory_patterns():
    """Run different functions and analyze their memory patterns"""
    print("Memory Analysis with Performance-Tracker")
    print("=" * 50)

    reset_performance_stats()

    print("\n1. Testing memory leak pattern...")
    for i in range(3):
        result = memory_leak_function()
        print(f"Call {i+1}: Created {result} items")

    print("\n2. Testing temporary memory pattern...")
    for i in range(3):
        result = temporary_memory_function()
        print(f"Call {i+1}: Sum = {result}")

    print("\n3. Testing efficient memory pattern...")
    for i in range(3):
        result = efficient_memory_function()
        print(f"Call {i+1}: Sum = {result}")

    print("\n4. Testing nested data structures...")
    result = nested_data_function()
    print(f"Nested data items: {result}")

    print("\n5. Testing recursive memory allocation...")
    result = recursive_memory_function(3, 500)
    print(f"Recursive result length: {len(result)}")

    # Force garbage collection to see the difference
    print("\n6. Forcing garbage collection...")
    gc.collect()

    # Test again to see if memory usage changes
    print("Testing temporary memory after GC...")
    result = temporary_memory_function()
    print(f"Post-GC sum: {result}")

    print("\n" + "=" * 50)
    print("MEMORY ANALYSIS REPORT")
    print("=" * 50)
    print("Key insights to look for:")
    print("- Functions with positive 'Total Memory Used' may have memory leaks")
    print("- Functions with 0 'Total Memory Used' but high peaks use temporary memory")
    print(
        "- Compare peak memory usage between efficient vs. inefficient implementations"
    )
    print()

    show_performance_report()


def demonstrate_memory_optimization():
    """Show how to optimize memory usage"""
    print("\n" + "=" * 50)
    print("MEMORY OPTIMIZATION COMPARISON")
    print("=" * 50)

    reset_performance_stats()

    # Inefficient approach
    @performance_monitor(track_memory=True)
    def inefficient_sum():
        return sum([i**2 for i in range(100000)])

    # Efficient approach
    @performance_monitor(track_memory=True)
    def efficient_sum():
        return sum(i**2 for i in range(100000))

    print("Comparing list comprehension vs generator:")
    result1 = inefficient_sum()
    result2 = efficient_sum()

    print(f"Both results equal: {result1 == result2}")
    show_performance_report()


if __name__ == "__main__":
    analyze_memory_patterns()
    demonstrate_memory_optimization()
