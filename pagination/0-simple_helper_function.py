#!/usr/bin/env python3
"""Calculate indices for pagination."""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """Calculate start and end indices for a given page"""
    first_index = (page - 1) * page_size
    last_index = first_index + page_size
    return first_index, last_index
