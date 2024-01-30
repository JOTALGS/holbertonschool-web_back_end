#!/usr/bin/env python3
"""
    Measure_runtime coroutine that will execute async_comprehension four times
    in parallel using asyncio.gather.
"""
import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """ Coroutine that measures the total runtime of async_comprehension. """
    first_time = time.time()
    await asyncio.gather(
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
        async_comprehension()
        )
    last_time = time.time()
    total_time = last_time - first_time
    return total_time
