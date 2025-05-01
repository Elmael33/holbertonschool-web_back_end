#!/usr/bin/env python3
"""Module to calculate start and end indices for pagination."""


def index_range(page: int, page_size: int) -> tuple:
    """Returns a tuple containing the start\
        and end indices for pagination."""
    first_index = (page - 1) * page_size
    last_index = first_index + page_size
    return first_index, last_index
