#!/usr/bin/env python3
"""This module defines a coroutine < async_generator() >."""
from typing import List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """Asynchronously generates a list of random float between 0 and 10.

    Returns:
        List[float]: A list of random float between 0 and 10,
        generated asynchronously.
    """
    return [number async for number in async_generator()]
