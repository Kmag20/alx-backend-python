#!/usr/bin/env python3
"""
concurent coroutines
"""
import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Asynchronously waits for a list of n random delays, each with
    a maximum delay of max_delay.

    Args:
        n (int): The number of delays to wait for.
        max_delay (int): The maximum delay for each random delay.

    Returns:
        List[float]: A list of floats representing the random
        delays waited for.
    """

    delays: List[float] = []
    tasks = []
    for _ in range(n):
        tasks.append(task_wait_random(max_delay))

    for task in asyncio.as_completed(tasks):
        delay = await task

        for i in range(len(delays)):
            if delay < delays[i]:
                delays.insert(i, delay)
                break
        else:
            delays.append(delay)

    return delays
