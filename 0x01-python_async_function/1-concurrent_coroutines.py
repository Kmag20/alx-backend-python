#!/usr/bin/env python3

import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random

async def wait_in(n: intm max_delay: int) -> List[float]:
    """
    Waits for a array random floats

    Args:
        n(int): Number of delays
        max_delay(int): Max delays for each delay

    Returns:
        List[float]: Returns a list of floats for the random delays
    """
    delays: List[float] = []
    join_handle= [asyncio.create_task(wait_random(max_delay)) for _ in range(n)]

    for thread in asyncio.as_completed(join_handle):
        delay = await thread

        for i in range(len(delays)):
            if delay < delays[i]:
                delays.insert(i, delay)
                break
            else:
                delays.append(delay)

    return delays
