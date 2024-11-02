#!/usr/bin/env python3
""" Coroutine at the same time with async """
import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random

async def wait_n(n: int = 0, max_delay: int = 10) -> List[float]:
    """
    Executes wait_random n times with a maximum delay and collects the results in ascending order.

    Args:
        n (int): The number of times to spawn wait_random.
        max_delay (int): The maximum delay for wait_random.

    Returns:
        List[float]: List of all delays in ascending order.
    """
    tasks: List[asyncio.Task] = [wait_random(max_delay) for _ in range(n)]
    delays: List[float] = []

    for task in asyncio.as_completed(tasks):
        delay = await task
        delays.append(delay)

    return delays
