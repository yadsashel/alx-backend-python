# 0x03. Unittests and Integration Tests

## Overview

This project focuses on understanding and implementing both unit and integration testing for Python applications. Unit testing ensures that individual functions perform as expected across various inputs, including corner cases, while integration testing verifies that different components of the application interact correctly. Key concepts include mocking, parameterization, and the distinction between unit and integration tests.

### Key Components
1. **Unit Tests**: Focus on testing isolated functions to ensure they return expected outputs for various inputs.
2. **Integration Tests**: Verify the interactions between different parts of the application, testing code paths end-to-end.
3. **Mocking**: Used to replace certain calls, especially external ones like network or database requests, ensuring the tests run independently of external factors.
4. **Parameterized Testing**: Allows multiple test cases to be run with varying inputs, improving coverage and efficiency.
5. **Fixtures**: Predefined data for consistent testing across multiple tests.

### Learning Objectives
- Understand the difference between unit and integration tests.
- Apply testing patterns such as mocking, parameterization, and fixtures.

### Requirements
- Use Python 3.7 on Ubuntu 18.04 LTS.
- Follow **pycodestyle** style guidelines.
- All files should be executable with correct documentation for modules, classes, and functions.
- Type annotations are required for all functions and coroutines.

## Project Structure
```plaintext
.
├── README.md                    # Project Overview
├── utils.py                     # Utility functions for testing
├── client.py                    # Client functions and classes
├── fixtures.py                  # Predefined data for integration testing
├── test_utils.py                # Unit tests for utils.py
└── test_client.py               # Unit and integration tests for client.py
```

## Tasks Overview

### 1. Parameterize Unit Test for `access_nested_map`
Write a parameterized unit test for the `utils.access_nested_map` function to verify expected outputs across various inputs.

### 2. Exception Testing for `access_nested_map`
Test that the function raises `KeyError` for incorrect paths in nested maps.

### 3. Mocking HTTP Calls
Use `unittest.mock.patch` to mock HTTP calls in `utils.get_json` and verify responses for different URLs.

### 4. Memoization
Create a test for the `memoize` decorator, ensuring the function caches results properly.

### 5. Mocking Properties
Mock the `GithubOrgClient._public_repos_url` to test that it returns the correct URL based on a known payload.

### 6. Integration Testing with Fixtures
Set up an integration test using fixtures to verify end-to-end behavior of `GithubOrgClient.public_repos`.

## Running Tests

To run individual test files, use:
```bash
$ python -m unittest path/to/test_file.py
```
