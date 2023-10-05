#!/usr/bin/env python3



def to_kv(k: str, v: int | float)-> tuple:
    """creates a tuple with  k and square of v as members
    Args:
        k: str
        v: int or float
    Returns: a tuple with members k and square of v
        (k: string, v:float)
    """
    sq = float(v**v)
    return tuple([k, sq])
