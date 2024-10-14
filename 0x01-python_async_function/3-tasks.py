#!/usr/bin/env python3
""""
tasks
"""
import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Creates a new asyncio task that waits for a random delay
    before calling the `wait_random` function.

    Args:
        max_delay (int): The maximum delay in seconds.

    Returns:
        asyncio.Task: The created asyncio task.

    """
    return asyncio.create_task(wait_random(max_delay))
