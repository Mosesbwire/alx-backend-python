#!/usr/bin/env python3

# 1-concurrent_coroutines.py

"""Demonstrate how to run concurrent coroutines asynchronously"""
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> list[float]:
    """Spwans wait_random n times with the specified max_delay
    Args:
        n: number of times to spawn wait_random
        max_delay: the maximum delay to pass to wait_random
    Returns:
        A list of all the delays (float values) in ascending order 
    """

    sorted_list: list[float] = []
    return sorted_list
