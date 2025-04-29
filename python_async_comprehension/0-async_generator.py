#!/usr/bin/env python3
"""Module defines an async generator
    that yields random numbers after delays."""
import asyncio
import random
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:
    """Asynchronously yield 10 random floats between 0 and 10,
        with a 1-second pause between each."""
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
