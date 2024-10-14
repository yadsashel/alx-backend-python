# 0x01. Python - Async

## Overview

This project covers the basics of asynchronous programming in Python using `asyncio`. The tasks demonstrate how to work with coroutines, tasks, and how to execute concurrent code efficiently.

### Learning Objectives

- Understand `async` and `await` syntax.
- Learn how to run concurrent coroutines.
- Use asyncio tasks to manage asynchronous executions.
- Measure the runtime of asynchronous code.
- Gain familiarity with Python's `random` and `time` modules in async functions.

## Requirements

- Python 3.7+
- `pycodestyle` style for code quality.
- Each Python file should be executable with a proper shebang (`#!/usr/bin/env python3`).
- All functions and coroutines must have type annotations and proper documentation.

## Tasks

### Task 0: The basics of async

Write an asynchronous coroutine that waits for a random delay and returns it.

- **File:** `0-basic_async_syntax.py`
- **Function:** `async def wait_random(max_delay: int = 10) -> float:`

### Task 1: Execute multiple coroutines

Run multiple coroutines concurrently and return their delays in ascending order.

- **File:** `1-concurrent_coroutines.py`
- **Function:** `async def wait_n(n: int, max_delay: int) -> List[float]:`

### Task 2: Measure runtime

Measure the total runtime for executing multiple coroutines concurrently and return the average time per coroutine.

- **File:** `2-measure_runtime.py`
- **Function:** `def measure_time(n: int, max_delay: int) -> float:`

### Task 3: Tasks

Create an asyncio task for an asynchronous coroutine.

- **File:** `3-tasks.py`
- **Function:** `def task_wait_random(max_delay: int) -> asyncio.Task:`

### Task 4: More tasks

Execute multiple asyncio tasks concurrently and return their delays in ascending order.

- **File:** `4-tasks.py`
- **Function:** `async def task_wait_n(n: int, max_delay: int) -> List[float]:`

