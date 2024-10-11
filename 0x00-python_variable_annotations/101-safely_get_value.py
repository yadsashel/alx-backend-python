#!/usr/bin/env python3
"""This function safely retrieves a value from a dictionary
given a key, returning a default value if the key is not found."""

from typing import Mapping, Any, Optional, TypeVar

T = TypeVar('T')


def safely_get_value(dct: Mapping[Any, T], key: Any,
                     default: Optional[T] = None) -> Optional[T]:
    """Return the value associated with key in the dictionary dct
    or default if the key is not found."""
    if key in dct:
        return dct[key]
    else:
        return default
