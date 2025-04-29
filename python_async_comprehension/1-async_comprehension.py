#!/usr/bin/env python3
"""Module defines an asynchronous function
    that gathers values from an async generator."""
import asyncio
from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """Use an async comprehension to gather and
        return 10 random numbers from the async generator."""
    return [number async for number in async_generator()]
