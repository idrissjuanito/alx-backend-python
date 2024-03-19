#!/usr/bin/env python3
""" generator coroutine """
import random
import asyncio


async def async_generator():
    """ async generator
        yields random number every second
    """
    for i in range(10):
        await asyncio.sleep(1)
        yield(random.uniform(0, 10))
