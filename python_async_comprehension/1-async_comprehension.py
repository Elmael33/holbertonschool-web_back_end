#!/usr/bin/env python3
"""module defines a coroutine that collects\
    random numbers using async comprehension."""
    
from typing import List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """Collect 10 random numbers using an async\
        comprehending over async_generator."""
    return [number async for number in async_generator()]
