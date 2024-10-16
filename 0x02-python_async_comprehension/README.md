# 0x02. Python - Async Comprehension

## Project Overview
This project is focused on learning asynchronous programming in Python, specifically dealing with asynchronous comprehensions and generators. You will learn how to efficiently handle asynchronous tasks and work with `asyncio`, Python’s library for writing concurrent code using the async/await syntax.

## Learning Objectives
By the end of this project, you should be able to explain the following concepts clearly:
- How to write an asynchronous generator.
- How to use async comprehensions.
- How to type-annotate generators and coroutines.

## Project Requirements
- All code will be written in Python 3.7.
- Use Ubuntu 18.04 LTS for development and testing.
- All Python scripts should start with `#!/usr/bin/env python3`.
- You must follow the **pycodestyle** (PEP 8) guidelines for code style.
- All files must end with a new line.
- Ensure each module and function has a docstring explaining its purpose.
- All functions and coroutines must be type-annotated.

## Project Structure
```
0x02-python_async_comprehension/
│
├── 0-async_generator.py
├── 1-async_comprehension.py
├── 2-measure_runtime.py
├── 0-main.py
├── 1-main.py
├── 2-main.py
└── README.md
```

## Tasks

### Task 0: Async Generator
**File**: `0-async_generator.py`

Write a coroutine called `async_generator` that takes no arguments.
- This coroutine will loop 10 times, each time asynchronously wait 1 second, then yield a random float between 0 and 10.
  
**Usage Example**:
```python
import asyncio
from 0-async_generator import async_generator

async def print_yielded_values():
    async for i in async_generator():
        print(i)

asyncio.run(print_yielded_values())
```

### Task 1: Async Comprehensions
**File**: `1-async_comprehension.py`

Write a coroutine called `async_comprehension` that collects 10 random numbers using an async comprehension over the coroutine `async_generator` and returns them.

**Usage Example**:
```python
import asyncio
from 1-async_comprehension import async_comprehension

async def main():
    result = await async_comprehension()
    print(result)

asyncio.run(main())
```

### Task 2: Run time for four parallel comprehensions
**File**: `2-measure_runtime.py`

Write a coroutine `measure_runtime` that will execute `async_comprehension` four times in parallel using `asyncio.gather` and measure the total runtime.
- The function should return the total time taken for the parallel execution.

**Usage Example**:
```python
import asyncio
from 2-measure_runtime import measure_runtime

async def main():
    runtime = await measure_runtime()
    print(f"Total runtime: {runtime} seconds")

asyncio.run(main())
```

## Concepts Covered
- **Asynchronous Generators**: A special type of generator that allows the `yield` keyword to work with `await`, allowing asynchronous iteration.
- **Async Comprehensions**: Comprehensions using `async for` which enables fetching results asynchronously, improving efficiency.
- **Concurrency with `asyncio.gather`**: Running coroutines in parallel and handling multiple tasks at once.

## Resources
- [PEP 530 – Asynchronous Comprehensions](https://www.python.org/dev/peps/pep-0530/)
- [What’s New in Python: Asynchronous Comprehensions / Generators](https://docs.python.org/3/whatsnew/3.6.html#pep-530-asynchronous-comprehensions)
- [Type-hints for generators](https://docs.python.org/3/library/typing.html#typing.Generator)
