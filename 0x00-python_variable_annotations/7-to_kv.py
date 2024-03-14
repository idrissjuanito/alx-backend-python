#!/usr/bin/env python3
""" to_kv function """
from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """ returns a tuple with values passed as argument """
    return (k, v**2)
