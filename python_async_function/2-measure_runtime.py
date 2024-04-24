#!/usr/bin/env python3
"""This module defines the function < measure_time() >."""
import asyncio
import time

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """Takes 2 integers <n> and <max_delay> as arguments.
    Measures the total execution time for wait_n(n, max_delay)
    Returns (total_time / n).

    Args:
        n (int): Number of call at wait_random().
        max_delay (int): Maximum timeout limit.

    Returns:
        float: average time of each call at wait_n().
    """
    start: float = time.time()
    asyncio.run(wait_n(n, max_delay))
    end: float = time.time()
    total_time: float = (end - start)
    return (total_time / n)
