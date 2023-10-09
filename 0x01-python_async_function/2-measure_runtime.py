#!/usr/bin/env python3
# 2-measure_runtime.py

"""Measure execution time of a function"""

import time
import asyncio
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """Measures the running time of wait_n
    Args:
        n: number of times wait_n should run
        max_delay: the delay time passed to wait_n
    Returns:
        time taken to execute function wait_n as a float
    """

    start = time.perf_counter()

    asyncio.run(wait_n(n, max_delay))

    exec_time = time.perf_counter() - start

    return float(exec_time / n)
