#!/usr/bin/python3
""" This module define the type-annotated function make_multiplier(). """
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """ Takes float <multiplier> as argument,
    returns a function that multiplies a float by multiplier.

    Args:
        multiplier (float): Number to be multiplied.

    Returns:
        Callable[[float], float]: Lambda function that multiplies its argument
        by the multiplier.
    """
    return (lambda x: multiplier * x)
