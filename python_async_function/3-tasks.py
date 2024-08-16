#!/usr/bin/env python3
"""Module to create an asyncio Task from a coroutine."""

from asyncio import Task, create_task


wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> Task:
    """Return an asyncio Task object that is running wait_random."""
    return create_task(wait_random(max_delay))
