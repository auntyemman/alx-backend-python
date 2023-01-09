#!/usr/bin/env python3

"""Async routine that takes two int arguments"""

import asyncio

from typing import List


task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """The function spawn wait_random in n times with specified amx_delay"""

    tasks = [task_wait_random(max_delay) for _ in range(n)]
    return [await task for task in asyncio.as_completed(tasks)]
