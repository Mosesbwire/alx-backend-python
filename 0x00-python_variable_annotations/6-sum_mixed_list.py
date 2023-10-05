#!/usr/bin/env python3

def sum_mixed_list(mxd_list: list[float | int])->float:
    """Takes list of floats and ints, calculate the sum
    Args"
        mxd_list: list of floats and ints
    Returns:
        sum of mxd_list
        sum: float
    """
    return float(sum(mxd_list))