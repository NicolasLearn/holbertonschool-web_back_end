#!/usr/bin/env python3
""" This module define the type-annotated function element_length(). """
from typing import Iterable, Sequence, Tuple, List


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """ Takes a list of sequences as input.
    returns a list of tuples containing each element of the input list
    paired with its corresponding length.

    Args:
        lst (Iterable[Sequence]): Input list of sequences.

    Returns:
        List[Tuple[Sequence, int]]: List of tuples containing each element
        of the input list paired with its corresponding length.
    """
    return [(i, len(i)) for i in lst]
