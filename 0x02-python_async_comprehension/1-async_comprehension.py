
#!/usr/bin/env python3
""" Takes 2 int args, waits for random delay """

import asyncio
import random
from typing import List
async_generator = __import__('0-async_generator').async_generator

async def async_comprehension() -> List[float]:
    return [i async for i in  async_generator()]

