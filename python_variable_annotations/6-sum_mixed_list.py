#!/usr/bin/env python3
"""Module defines a function to sum a list contain integers and floats."""
from typing import Union, List


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """Return sum of all float elements in the input list."""
    return float(sum(mxd_lst))
