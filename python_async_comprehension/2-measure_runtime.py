#!/usr/bin/env python3
"""Module defines a coroutine to measure the \
    execution time of multiple async operations."""

import asyncio
from time import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """Run async_comprehension four times in parallel\
          and return how long it takes to complete."""
    start = time()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    return time() - start
