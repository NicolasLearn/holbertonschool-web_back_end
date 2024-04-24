#!/usr/bin/env python3
"""This module defines a coroutine < measure_runtime() >."""
import asyncio
import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """Measures the execution time of running 4 instances
    of the async_comprehension coroutine and return it.

    Returns:
        float: Total execution time in seconds.
    """
    start: float = time.perf_counter()

    # Calls 4 instances of the async_comprehension coroutine asynchronously.
    # Waits for all coroutines to complete before moving to the next step.
    await asyncio.gather(*(async_comprehension() for i in range(4)))

    end: float = time.perf_counter()
    total: float = end - start

    # Returns the total execution time in seconds.
    return total
