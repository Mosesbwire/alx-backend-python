#!/usr/bin/env python3
from collections.abc import Callable
def make_multiplier(multiplier: float)-> Callable[[float], float]:
    """creates a function that multiplys multiplier by a float
    Args:
        multiplier: float
    Returns: a function taking a single float argument
        func: function
    """
    def inner(n: float)->float:
        return float(n * multiplier)

    return inner

