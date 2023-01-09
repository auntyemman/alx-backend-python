#!/usr/bin/env python3

"""A normal function that takes and an integer max_delay"""

from asyncio import Task, create_task


wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> Task:
    """The function returns a class asyncio.Task"""

    task = create_task(wait_random(max_delay))
    return task
