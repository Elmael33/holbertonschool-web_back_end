#!/usr/bin/env python3
"""module measures the runtime"""

import asyncio
from time import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """measure_runtime should measure\
        the total runtime and return it"""
    clock = time()
    await asyncio.gather(*(async_comprehension() for x in range(4)))
    return time() - clock
