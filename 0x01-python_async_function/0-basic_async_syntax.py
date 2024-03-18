#!/usr/bin/env python3
""" random coroutine function """
import random
import time
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    """ sleep for random sleep time """
    timee = random.uniform(0, max_delay)
    await asyncio.sleep(timee)
    return timee
