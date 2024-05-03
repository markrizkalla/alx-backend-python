#!/usr/bin/env python3
"""return sum as a float"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[float, int]]) -> float:
    """sum of a list"""
    return float(sum(mxd_lst))
