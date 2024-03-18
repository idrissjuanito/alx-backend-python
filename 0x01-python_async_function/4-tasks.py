#!/usr/bin/env python3
""" Measuring execution time """
import time
import asyncio
from typing import List
task_wait_random = __import__("3-tasks").task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """ run coroutine n times """
    completed = list()
    for i in range(0, n):
        time_task = await task_wait_random(max_delay)
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
