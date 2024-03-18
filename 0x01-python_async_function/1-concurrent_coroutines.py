#!/usr/bin/env python3
""" async io multiple coroutines """
import asyncio
from typing import List
wait_random = __import__("0-basic_async_syntax").wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """ run coroutine n times """
    completed = list()
    for i in range(0, n):
        time_task = await asyncio.create_task(wait_random(max_delay))
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
