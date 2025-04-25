#!/usr/bin/env python3
"""Module defines a function to sum a list of floats."""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """Return sum of all elements in the input list."""
    return float(sum(input_list))
