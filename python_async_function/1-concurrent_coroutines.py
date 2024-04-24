#!/usr/bin/env python3
"""This module defines the async function <wait_n()>."""
import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Async routine, that takes 2 'int' arguments.
    Spawn <wait_random()> <n> times with the specified <max_delay>.
    return the list of all the delays, in ascending order.

    Args:
        n (int): Number of iteration.
        max_delay (int): Maximum timeout limit.

    Returns:
        List[float]: List of all delay created, in ascending order.
    """
    list_random_delay = list()
    # On each iteration, generate random async task, and adds it at the list.
    for i in range(n):
        list_random_delay.append(wait_random(max_delay))

    # Return a list of each async task completed, in ascending order.
    return [await delay for delay in asyncio.as_completed(list_random_delay)]
