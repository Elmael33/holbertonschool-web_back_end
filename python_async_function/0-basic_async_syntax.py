#!/usr/bin/env python3
"""Module with an asynchronous coroutine that waits for a random delay."""

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """Wait for a random delay between 0 and\
        max_delay seconds, then return the delay."""
    return await asyncio.sleep(random.uniform(0, max_delay))\
        or random.uniform(0, max_delay)
