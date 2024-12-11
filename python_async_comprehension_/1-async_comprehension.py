#!/usr/bin/env python3
"""module collects random number"""

from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension():
    """collect 10 random numbers using an\
        async comprehensing over async_generator"""
    return [number async for number in async_generator()]
