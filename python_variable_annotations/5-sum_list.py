#!/usr/bin/env python3
""" This module define the type-annotated function sum_list(). """
from typing import List


def sum_list(input_list: List[float]) -> float:
    """ Takes a list of floats and returns their sum as a float.

    Args:
        inpu_list (List[float]): List of float to add.

    Returns:
        float: Sum of items in the list.
    """
    sum: float = 0
    for number in input_list:
        sum += number
    return sum
