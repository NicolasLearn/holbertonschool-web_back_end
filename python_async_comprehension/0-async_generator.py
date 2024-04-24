#!/usr/bin/env python3
"""This module defines a coroutine < async_generator() >."""
import asyncio
import random
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None, None]:
    """The coroutine loops 10 times, each time asynchronously waiting for 1sec.
    Then it yields a random number between 0 and 10.

    Returns:
        AsyncGenerator[float, None]: Asynchronous generator,
        that yields float numbers between 0 and 10.

    Yields:
        Iterator[AsyncGenerator[float, None]]: Iterator over the asynchronous
        generator that yields float numbers between 0 and 10.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
