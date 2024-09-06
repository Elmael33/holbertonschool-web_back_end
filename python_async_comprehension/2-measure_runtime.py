#!/usr/bin/env python3
"""Module defines a coroutine that measures the runtime"""

import asyncio
from time import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """Measure total runtime of executing\
        async_comprehension four times."""
    start = time()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    return time() - start
