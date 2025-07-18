import unittest
import time
from pyperformance import performance_monitor, reset_performance_stats, get_performance_stats

class TestPerformanceMonitor(unittest.TestCase):
    
    def setUp(self):
        """Reset stats before each test"""
        reset_performance_stats()
    
    def test_basic_timing(self):
        """Test basic function timing"""
        @performance_monitor(verbose=False)
        def test_func():
            time.sleep(0.01)
            return "done"
        
        result = test_func()
        self.assertEqual(result, "done")
        
        stats = get_performance_stats()
        self.assertIn("test_func", stats)
        self.assertEqual(stats["test_func"]["call_count"], 1)
        self.assertEqual(stats["test_func"]["success_count"], 1)
        self.assertGreater(stats["test_func"]["total_time"], 0.008)
    
    def test_memory_tracking(self):
        """Test memory usage tracking"""
        @performance_monitor(track_memory=True, verbose=False)
        def memory_func():
            return [i for i in range(100000)]
        
        result = memory_func()
        self.assertEqual(len(result), 100000)
        
        stats = get_performance_stats()
        self.assertGreater(stats["memory_func"]["max_memory_peak"], 0)
    
    def test_recursion_tracking(self):
        """Test recursion handling"""
        @performance_monitor(track_recursion=True, verbose=False)
        def factorial(n):
            if n <= 1:
                return 1
            return n * factorial(n - 1)
        
        result = factorial(5)
        self.assertEqual(result, 120)
        
        stats = get_performance_stats()
        # Should only count the top-level call
        self.assertEqual(stats["factorial"]["call_count"], 1)
    
    def test_error_handling(self):
        """Test handling of function exceptions"""
        @performance_monitor(verbose=False)
        def failing_func():
            raise ValueError("Test error")
        
        with self.assertRaises(ValueError):
            failing_func()
        
        stats = get_performance_stats()
        self.assertEqual(stats["failing_func"]["failure_count"], 1)
        self.assertEqual(stats["failing_func"]["success_count"], 0)

if __name__ == "__main__":
    unittest.main()