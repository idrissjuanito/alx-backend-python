#!/usr/bin/env python3
""" async comprehensionn measure function """
import time
import asyncio
async_comprehension = __import__('1-async_comprehension').async_comprehension


def measure_runtime():
    """ measures the total time taken to run number of async coroutines """
    start = time.perf_counter()
    asyncio.gather(*[async_comprehension() for i in range(4)])
    total_time = time.perf_counter() - start
    return total_time
