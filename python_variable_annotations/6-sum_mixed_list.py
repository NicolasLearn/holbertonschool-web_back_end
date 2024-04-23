#!/usr/bin/env python3
""" This module define the type-annotated function sum_mixed_list(). """
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """ Takes a list of "float" and "int" and sums the elements.

    Args:
        mxd_lst (List[Union[int, float]]): List of number to add.

    Returns:
        float: Sum of items in the list.
    """
    sum: float = 0
    for number in mxd_lst:
        sum += number
    return sum
