#!/usr/bin/env python3
"""
From the previous file, import wait_n into 2-measure_runtime.py.
"""
import asyncio
import time

wait_n = __import__("1-concurrent_coroutines").wait_n

"""
Create a measure_time function with integers n and max_delay as arguments that measures the total execution time for wait_n(n, max_delay), and returns total_time / n. Your function should return a float.
"""
def measure_time(n: int, max_delay: int = 10) -> float:
    """
    Returns total time / n for wait_n() execution
    """

    s = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    elapsed = time.perf_counter() - s
    return elapsed / n
