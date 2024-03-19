#!/usr/bin/env python3
""" Measuring execution time """
import time
import asyncio
from typing import List
wait_n = __import__("1-concurrent_coroutines").wait_n


async def measure_time(n: int, max_delay: int) -> List[float]:
    """ run coroutine n times """
    completed = list()
    for i in range(0, n):
        time_task = await wait_n(n, max_delay)
        if len(completed) < 1:
            completed.append(time_task)
            continue
        for j in range(len(completed)):
            if completed[j] > time_task:
                completed.insert(j, time_task)
                break
            if j == len(completed) - 1:
                completed.append(time_task)
    return completed
