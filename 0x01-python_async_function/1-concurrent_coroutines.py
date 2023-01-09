#!/usr/bin/env python3

"""Async routine that takes two int arguments"""

import asyncio

from typing import List


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """The function spawn wait_random in n times with specified amx_delay"""

    tasks = [asyncio.create_task(wait_random(max_delay)) for _ in range(n)]
    return [await task for task in asyncio.as_completed(tasks)]
