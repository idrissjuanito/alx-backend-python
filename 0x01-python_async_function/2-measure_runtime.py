#!/usr/bin/env python3
""" Measuring execution time """
import time
import asyncio
from typing import List
wait_n = __import__("1-concurrent_coroutines").wait_n


async def measure_time(n: int, max_delay: int) -> float:
    """ measures time function runs """
    start = time.perf_counter()
    await asyncio.run(wait_n(n, max_delay))
    total_time = time.perf_counter() - start
    return start / n
