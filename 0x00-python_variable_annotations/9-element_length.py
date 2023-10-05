#!/usr/bin/env python3

def element_length(lst: list)->list[tuple]:
    return [(i, len(i)) for i in lst]