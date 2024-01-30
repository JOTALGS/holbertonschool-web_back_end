#!/usr/bin/env python3
"""
    Tsdsadas f fdffggthhh  hh
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """ Returns a function that multiplies a float by multiplier """
    def function_multiplier(n: float) -> float:
        """ multiplies a float by multiplier """
        return n * multiplier
    return function_multiplier
