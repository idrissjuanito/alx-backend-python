#!/usr/bin/env python3
""" element length function """
from typing import Sequence, Iterable, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """ function returns a list of tuples containine element
        of the lst iterable and their length
    """
    return [(i, len(i)) for i in lst]
