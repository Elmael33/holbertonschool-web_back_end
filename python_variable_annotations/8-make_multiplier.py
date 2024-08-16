#!/usr/bin/env python3
"""Module with a function that returns a multiplier function."""
from typing import Callable, Iterator, Union, Optional, List, Tuple


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Return a function that multiplies a float by the multiplier."""
    def f(n: float) -> float:
        """Return the result of n multiplied by the multiplier."""
        return float(n * multiplier)

    return f