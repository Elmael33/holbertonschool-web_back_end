#!/usr/bin/env python3
"""Module to measure the average execution time of an asynchronous function."""

from asyncio import run
from time import time


wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """Returns the average time per call in seconds."""
    start = time()
    run(wait_n(n, max_delay))
    end = time()
    return (end - start) / n
