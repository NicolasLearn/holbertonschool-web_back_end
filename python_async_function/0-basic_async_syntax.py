#!/usr/bin/env python3
"""This module defines the async function <wait_random()>."""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """Asynchronous coroutine that takes an 'int' as argument.
    Waits for a random delay(0 and <max_delay>).
    Returns it.

    Args:
        max_delay (int): Maximum timeout limit. Defaults to 10.

    Returns:
        random_delay (float): Got using the module random.
    """
    random_delay: float = random.uniform(0, max_delay)
    await asyncio.sleep(random_delay)
    return random_delay
