#!/usr/bin/env python3

"""A function to measures the total execution time of a program"""

import asyncio
import time


wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """This function returns time elapse over the number n in float"""
    
    start = time.time()
    asyncio.run(wait_n(n, max_delay))
    end = time.time()
    elapse = (end - start) / n
    return elapse