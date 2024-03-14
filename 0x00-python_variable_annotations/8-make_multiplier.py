#!/usr/bin/env python3
""" function multiplier """
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """ returns a multiplier function that uses it's argument """
    return lambda x: x * multiplier
