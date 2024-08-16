#!/usr/bin/env python3
"""Module with a function to create a tuple from a string and a squared number."""
from typing import Callable, Iterator, Union, Optional, List, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Return a tuple where the first element is the string `k` and the second element is `v` squared as a float"""
    return (k, v**2)