#!/usr/bin/env python3
""" safe_first_element function """
from types import NoneType
from typing import Union, Any, Sequence


def safe_first_element(lst: Sequence[Any]) -> Union[Any, NoneType]:
    """ returns first element of a sequence """
    if lst:
        return lst[0]
    else:
        return None
