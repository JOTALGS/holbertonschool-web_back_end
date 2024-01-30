#!/usr/bin/env python3
"""
    sdsadas fdsafd
"""
import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """ Returns the list of all the delays in ascending order """
    deleys: List = [task_wait_random(max_delay) for _ in range(n)]
    all_deleys: List = await asyncio.gather(*deleys)
    sorted_deleys: List = []
    for _ in range(n):
        min_deley = min(all_deleys)
        sorted_deleys.append(min_deley)
        all_deleys.remove(min_deley)
    return sorted_deleys
