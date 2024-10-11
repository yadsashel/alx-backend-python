#!/usr/bin/env python3
"""This function returns a zoomed-in version of a list,
duplicating each element a specified number of times."""

from typing import List


def zoom_array(lst: List[int], factor: int = 2) -> List[int]:
    """Return a list with each element of lst duplicated factor times."""
    zoomed_in: List[int] = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in
