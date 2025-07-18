import unittest
import time
from typing import Any
from pyperformance import performance_monitor, reset_performance_stats, get_performance_stats

class TestPerformanceMonitor(unittest.TestCase):
    
    def setUp(self) -> None:
        """Reset stats before each test"""
        reset_performance_stats()
    
    def test_basic_timing(self) -> None:
        """Test basic function timing"""
        @performance_monitor(verbose=False)
        def test_func() -> str:
            time.sleep(0.01)
            return "done"
        
        result = test_func()
        self.assertEqual(result, "done")
        
        stats = get_performance_stats()
        self.assertIn("test_func", stats)
        self.assertEqual(stats["test_func"]["call_count"], 1)
        self.assertEqual(stats["test_func"]["success_count"], 1)
        self.assertGreater(stats["test_func"]["total_time"], 0.008)
    
    def test_memory_tracking(self) -> None:
        """Test memory usage tracking"""
        @performance_monitor(track_memory=True, verbose=False)
        def memory_func() -> list[int]:
            return [i for i in range(100000)]
        
        result = memory_func()
        self.assertEqual(len(result), 100000)
        
        stats = get_performance_stats()
        self.assertGreater(stats["memory_func"]["max_memory_peak"], 0)
    
    def test_recursion_tracking(self) -> None:
        """Test recursion handling"""
        @performance_monitor(track_recursion=True, verbose=False)
        def factorial(n: int) -> int:
            if n <= 1:
                return 1
            return n * factorial(n - 1)
        
        result = factorial(5)
        self.assertEqual(result, 120)
        
        stats = get_performance_stats()
        # Should only count the top-level call
        self.assertEqual(stats["factorial"]["call_count"], 1)
    
    def test_error_handling(self) -> None:
        """Test handling of function exceptions"""
        @performance_monitor(verbose=False)
        def failing_func() -> str:
            raise ValueError("Test error")
        
        with self.assertRaises(ValueError):
            failing_func()
        
        stats = get_performance_stats()
        self.assertEqual(stats["failing_func"]["failure_count"], 1)
        self.assertEqual(stats["failing_func"]["success_count"], 0)
    
    def test_multiple_calls(self) -> None:
        """Test statistics accumulation across multiple calls"""
        @performance_monitor(verbose=False)
        def multi_call_func(x: int) -> int:
            time.sleep(0.001)
            return x * 2
        
        # Call multiple times
        for i in range(5):
            result = multi_call_func(i)
            self.assertEqual(result, i * 2)
        
        stats = get_performance_stats()
        self.assertEqual(stats["multi_call_func"]["call_count"], 5)
        self.assertEqual(stats["multi_call_func"]["success_count"], 5)
        self.assertEqual(len(stats["multi_call_func"]["times"]), 5)
    
    def test_success_rate_calculation(self) -> None:
        """Test success rate with mixed success/failure"""
        call_count = 0
        
        @performance_monitor(verbose=False)
        def unreliable_func() -> str:
            nonlocal call_count
            call_count += 1
            if call_count % 2 == 0:
                raise RuntimeError("Even call failure")
            return "success"
        
        # Call function 4 times (2 success, 2 failure)
        for _ in range(4):
            try:
                unreliable_func()
            except RuntimeError:
                pass
        
        stats = get_performance_stats()
        self.assertEqual(stats["unreliable_func"]["call_count"], 4)
        self.assertEqual(stats["unreliable_func"]["success_count"], 2)
        self.assertEqual(stats["unreliable_func"]["failure_count"], 2)
    
    def test_configuration_options(self) -> None:
        """Test different configuration combinations"""
        @performance_monitor(track_memory=False, track_recursion=False, verbose=False)
        def simple_func() -> int:
            return 42
        
        @performance_monitor(track_memory=True, track_recursion=True, verbose=False)
        def full_func() -> int:
            return 42
        
        simple_func()
        full_func()
        
        stats = get_performance_stats()
        self.assertIn("simple_func", stats)
        self.assertIn("full_func", stats)
        
        # Both should have basic timing stats
        for func_name in ["simple_func", "full_func"]:
            self.assertEqual(stats[func_name]["call_count"], 1)
            self.assertGreater(stats[func_name]["total_time"], 0)
    
    def test_stats_reset(self) -> None:
        """Test resetting performance statistics"""
        @performance_monitor(verbose=False)
        def test_func() -> None:
            pass
        
        test_func()
        stats_before = get_performance_stats()
        self.assertIn("test_func", stats_before)
        
        reset_performance_stats()
        stats_after = get_performance_stats()
        self.assertEqual(len(stats_after), 0)
    
    def test_return_value_preservation(self) -> None:
        """Test that decorated functions return original values"""
        @performance_monitor(verbose=False)
        def return_dict() -> dict[str, int]:
            return {"key": 123}
        
        @performance_monitor(verbose=False)
        def return_none() -> None:
            return None
        
        @performance_monitor(verbose=False)
        def return_tuple() -> tuple[int, str]:
            return (1, "test")
        
        dict_result = return_dict()
        none_result = return_none()
        tuple_result = return_tuple()
        
        self.assertEqual(dict_result, {"key": 123})
        self.assertIsNone(none_result)
        self.assertEqual(tuple_result, (1, "test"))
    
    def test_function_with_args_kwargs(self) -> None:
        """Test monitoring functions with various argument patterns"""
        @performance_monitor(verbose=False)
        def args_kwargs_func(a: int, b: str, *args: Any, **kwargs: Any) -> dict[str, Any]:
            return {"a": a, "b": b, "args": args, "kwargs": kwargs}
        
        result = args_kwargs_func(1, "test", 3, 4, key1="value1", key2="value2")
        expected = {
            "a": 1, 
            "b": "test", 
            "args": (3, 4), 
            "kwargs": {"key1": "value1", "key2": "value2"}
        }
        self.assertEqual(result, expected)
        
        stats = get_performance_stats()
        self.assertEqual(stats["args_kwargs_func"]["call_count"], 1)

if __name__ == "__main__":
    unittest.main()