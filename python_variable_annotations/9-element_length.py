#!/usr/bin/env python3
"""Module returns the length of elements in an iterable."""
from typing import Sequence, Iterable, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Return a list of tuples, each containing an element and its length."""
    return [(i, len(i)) for i in lst]
