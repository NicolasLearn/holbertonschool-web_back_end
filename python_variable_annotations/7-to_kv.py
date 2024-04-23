#!/usr/bin/python3
""" This module define the type-annotated function to_kv(). """
from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """ Takes string 'k' and int OR float 'v' as args and returns a tuple.

    Args:
        k (str): String arg.
        v (int or float): number arg.

    Returns:
        Tuple: (k: str, square of 'v': float)
    """
    tuple_result: Tuple[str, float] = (k, v**2)
    return tuple_result
