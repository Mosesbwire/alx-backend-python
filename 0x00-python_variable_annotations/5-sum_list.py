#!/usr/bin/env python3

def sum_list(input_list: list[float])->float:
    """sums the values in a list
    Args:
        input_list: list[floats]
    Returns:
        sum: float
    """
    return float(sum(input_list))




x = sum_list([1, 2])

if __name__ == "__main__":
    print(type(x))