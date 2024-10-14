#!/usr/bin/env python3
"""Execute multiple async coroutines concurrently and return their delays."""

import asyncio
from typing import List
from 0 - basic_async_syntax import wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Spawns wait_random n times and returns the list of delays."""
    delays = await asyncio.gather(*(wait_random(max_delay) for _ in range(n)))
    return sorted(delays)
