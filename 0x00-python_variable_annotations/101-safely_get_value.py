#!/usr/bin/env python3
""" returns values of a dictionary """
from typing import Any, TypeVar, Mapping, Union


T = TypeVar("T")
def safely_get_value(dct: Mapping, key: Any, default: Union[T, None]) -> Union[Any, T]:
    """ returns values of a dictionary """
    if key in dct:
        return dct[key]
    else:
        return default
