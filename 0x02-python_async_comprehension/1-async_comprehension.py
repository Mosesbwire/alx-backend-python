#!/usr/bin/env python3

# 1-async_comprehension.py

""" Async comprehension """

import asyncio

async_generator = __import__("0-async_generator").async_generator


async def async_comprehension():
    """ async comprehension """
    res = [i async for i in async_generator()]
    return res
