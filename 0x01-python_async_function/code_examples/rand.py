#!/usr/bin/env python3
#rand.py

import random
import asyncio

#ANSI COLORS
c = (
    "\033[0m",
    "\033[36m",
    "\033[91m",
    "\033[35m",
)

async def make_random(idx: int, threshold: int = 6)-> int:
    print(c[idx + 1] + f"Initiated make_random({idx}).")
    i = random.randint(0, 10)

    while i <= threshold:
        print(c[idx + 1] + f"make_random({idx}) === {i} too low; retrying")
        await asyncio.sleep(idx + 1)
        i = random.randint(0, 10)
    print(c[idx + 1] + f"---> Finished: make_random({idx}) == {i}" + c[0])
    return i

async def main():
    res = await asyncio.gather(*(make_random(i, 10 - i - 1) for i in range(3)))
    return res

if __name__ == "__main__":
    random.seed(444)
    r1, r2, r3 = asyncio.run(main())
    print()

    print(f"r1: {r1}, r2: {r2}, r3: {r3}")