#!/usr/bin/python3
"""
Async function in Python
"""

import asyncio
import random

async def wait_random(max_delay: int = 10) -> float:
    """
    Asynchronously coroutine taking an integer and
    waits for a random delay between 0 and max_delay
    and eventually returns it.

    Args:
        max_delay (int, optional): Max delay

    Returns:
        float: Delayed seconds
    """

    random_delay = random.uniform(0, max_delay)
    await asyncio.sleep(random_delay)
    return random_delay
