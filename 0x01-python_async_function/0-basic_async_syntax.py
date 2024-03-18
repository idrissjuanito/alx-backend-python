#!/usr/bin/env python3
""" random coroutine function """
import random
import time


async def wait_random(max_delay: int = 10):
    """ sleep for random sleep time """
    timee = random.uniform(0, max_delay)
    time.sleep(timee)
    return timee
