#!/usr/bin/env python3

import asyncio

# classic comprehensions - they provide a concise way to create data collections like lists, dicts and sets.

# creating a list using a comprehension

# result_list = [a / 2 for a in range(100)]

# print(result_list)

# # creating a dict using comprehension

# result_dict = {a: i for a, i in zip(['a', 'b', 'c'], range(3))}

# print(result_dict)

# # creating a set

# result_set = {a for a in range(5)}

# print(result_set)


# def generator():
#     yield "My name"

#     yield "is moses"

#     yield "am software engineer"


# gen_obj = generator()

# print(next(gen_obj))


# def cube(num):
#     return num * num * num


# def getCubes(rng):

#     for num in range(rng):
#         yield cube(num)


# print(list(getCubes(5)))


# async def async_generator():
#     for i in range(10):
#         await asyncio.sleep(1)
#         yield i


# async def main():
#     res = [item async for item in async_generator()]

#     print(res)


# asyncio.run(main())


# async def task_coro(value):
#     await asyncio.sleep(1)
#     return value * 10


# async def main_b():
#     awaitables = [task_coro(i) for i in range(10)]

#     results = [await a for a in awaitables]

#     print(results)


# asyncio.run(main_b())

measure_runtime = __import__('2-measure_runtime').measure_runtime


async def main():
    return await(measure_runtime())

print(
    asyncio.run(main())
)
