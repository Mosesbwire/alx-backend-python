#!/usr/bin/env python3
# 2-measure_runtime.py

"""Measure the runtime of async comprehension"""

import asyncio
import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime():
    """ measure runtime of running function """

    start = time.perf_counter()

    await async_comprehension()

    run_time = time.perf_counter() - start

    return run_time
