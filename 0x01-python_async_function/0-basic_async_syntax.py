#!/usr/bin/env python3
"""Run async function"""
import asyncio
import random


async def wait_random(max_delay:int =10) -> float:
    """return float value after random delay"""
    rand_val = random.uniform(0, max_delay)
    await asyncio.sleep(rand_val)
    return rand_val
