#!/usr/bin/env python3
""" Measure the runtime of a function
"""

import asyncio
import random
from time import perf_counter

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """Return the elapsed time"""
    s = pref_counter()
    asyncio.run(wait_n(n, max_delay))
    elapsed = pref_counter() - s
    return elapsed
