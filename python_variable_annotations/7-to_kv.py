#!/usr/bin/env python3
"""Module returning a tuple from a string and a squared number."""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Return a tuple, a string and the square of all numbers as a float."""
    return (k, float(v ** 2))
