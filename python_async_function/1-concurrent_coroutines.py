#!/usr/bin/env python3
"""Module with an asynchronous coroutine that waits for multiple delays."""

import asyncio
from typing import List


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Returns a list of delays in the order they were completed."""
    tasks = [asyncio.create_task(wait_random(max_delay)) for _ in range(n)]
    return [result for result in await asyncio.gather(*tasks)]
