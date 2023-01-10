#!/usr/bin/env python3

"""A coroutine that takes no arguments"""

import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """The function loops 10 times and wait 1 seconds asynchronously"""

    for _ in range(10):
         await asyncio.sleep(1)
         yield random.uniform(0, 10)
