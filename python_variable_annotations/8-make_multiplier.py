#!/usr/bin/env python3
"""Module defines a returning multiplier function."""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Return function that multiplies a float by the multiplier."""
    def none(n: float) -> float:
        """Result of n being multipliate"""
        return float(n * multiplier)

    return none
