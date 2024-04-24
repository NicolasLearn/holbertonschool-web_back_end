#!/usr/bin/env python3
"""This module defines the async function <task_wait_n()>."""
import asyncio
from typing import List

task_wait_random = __import__('0-basic_async_syntax').wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Async routine, that takes 2 'int' arguments.
    Spawn <wait_random()> <n> times with the specified <max_delay>.
    return the list of all the delays, in ascending order.

    Args:
        n (int): Number of iteration.
        max_delay (int): Maximum timeout limit.

    Returns:
        List[float]: List of all delay created, in ascending order.
    """
    list_tasks: List[asyncio.Task] = list()

    # For each iteration, we get a task and add it to <list_tasks>.
    for _ in range(n):
        list_tasks.append(task_wait_random(max_delay))

    list_delays: List[float] = list()

    # Iterates over tasks as they complete, Wait result of the Task.
    # Add it to <list_delays>.
    for task in asyncio.as_completed((list_tasks)):
        delay = await task
        list_delays.append(delay)

    # Return the list of each delay, in ascending order.
    return list_delays
