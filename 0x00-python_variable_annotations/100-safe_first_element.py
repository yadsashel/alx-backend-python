#!/usr/bin/env python3
"""This function returns the first element of a sequence if it exists,
otherwise returns None."""

from typing import Any, Sequence, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """Return the first element of lst if lst is not empty,
    otherwise return None."""
    if lst:
        return lst[0]
    else:
        return None
