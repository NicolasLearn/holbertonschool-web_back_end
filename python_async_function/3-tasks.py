#!/usr/bin/env python3
"""This module defines the function < task_wait_random() >."""
import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """Takes an integer <max_delay> in argument.
    Create Task with asyncio module.
    Return the Task.

    Args:
        max_delay (int): Maximum timeout limit

    Returns:
        asyncio.Task: Task created with calling at < wait_random() >.
    """
    task: asyncio.Task = asyncio.create_task(wait_random(max_delay))
    return task
