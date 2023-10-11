#!/usr/bin/env python3
"""
A module for asynchronous tasks using asyncio.
"""

import random
import asyncio

async def wait_random(max_delay=10):
  """Waits for a random delay between 0 and max_delay seconds.

  Args:
    max_delay: The maximum delay in seconds.

  Returns:
    The random delay in seconds.
  """

  delay = random.uniform(0, max_delay)
  await asyncio.sleep(delay)
  return delay
  