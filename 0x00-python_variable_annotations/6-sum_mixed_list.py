#!/usr/bin/env python3
""" sum mixed type list """
from typing import List


def sum_mixed_list(mxd_lst: List[int , float]) -> float:
    """ sums up a list of integers and floats """
    return float(sum(mxd_lst))
