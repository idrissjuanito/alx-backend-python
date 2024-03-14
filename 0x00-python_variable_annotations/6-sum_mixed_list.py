#!/usr/bin/env python3
""" sum mixed type list """


def sum_mixed_list(mxd_lst: list[int | float]) -> float:
    """ sums up a list of integers and floats """
    return float(sum(mxd_lst))
