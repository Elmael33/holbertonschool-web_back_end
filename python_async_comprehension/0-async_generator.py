#!/usr/bin/env python3
"""Module defines an async generator
    that yields random numbers after delays."""
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None]:
    """Asynchronously yield 10 random floats between 0 and 10,
        with a 1-second pause between each."""
    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
