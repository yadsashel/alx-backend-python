# 0x00. Python - Variable Annotations

## Overview
This project covers the basics of **Python Variable Annotations**. The goal is to learn how to use Python's type annotations to specify the types of function arguments, return values, and variables, as well as to validate code using **mypy**.

### Learning Objectives
By the end of this project, you should be able to:
- Understand the basics of **Type Annotations** in Python.
- Use type annotations to define the function signatures and variable types.
- Apply **duck typing** concepts.
- Use **mypy** to validate code for type correctness.

---

## Project Structure

```
.
├── 0-add.py
├── 1-concat.py
├── 2-floor.py
├── 3-to_str.py
├── 4-define_variables.py
├── 5-sum_list.py
├── 6-sum_mixed_list.py
├── 7-to_kv.py
├── 8-make_multiplier.py
├── 9-element_length.py
└── README.md
```

Each `.py` file contains a specific function with type annotations to fulfill a task. These tasks introduce the fundamentals of type annotations and gradually build towards more complex types like lists, tuples, unions, and functions.

---

## Requirements
- All code files will be interpreted on **Ubuntu 18.04 LTS** using `python3 (version 3.7)`
- **mypy** is used to validate the type annotations.
- Files are formatted according to the **pycodestyle** style guide.
- Proper documentation is required for modules, classes, and methods.

---

## Tasks

1. **Basic annotations - add**
   - Write a function `add(a: float, b: float) -> float` that returns the sum of two floats.

2. **Basic annotations - concat**
   - Write a function `concat(str1: str, str2: str) -> str` that concatenates two strings.

3. **Basic annotations - floor**
   - Write a function `floor(n: float) -> int` that returns the floor of a float.

4. **Basic annotations - to string**
   - Write a function `to_str(n: float) -> str` that converts a float to a string.

5. **Define variables**
   - Define variables with type annotations: 
     - `a: int = 1`
     - `pi: float = 3.14`
     - `i_understand_annotations: bool = True`
     - `school: str = "Holberton"`

6. **Complex types - list of floats**
   - Write a function `sum_list(input_list: List[float]) -> float` that sums a list of floats.

7. **Complex types - mixed list**
   - Write a function `sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float` that sums a mixed list of ints and floats.

8. **Complex types - string and int/float to tuple**
   - Write a function `to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]` that returns a tuple.

9. **Complex types - functions**
   - Write a function `make_multiplier(multiplier: float) -> Callable[[float], float]` that returns a function that multiplies a float.

10. **Let's duck type an iterable object**
    - Annotate a function `element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]` that returns the length of elements in a sequence.

---

## Resources
To complete this project, refer to the following resources:
- [Python 3 typing documentation](https://docs.python.org/3/library/typing.html): Comprehensive guide to Python's type hints and annotations.
- [MyPy Cheat Sheet](https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html): A quick reference to using `mypy` for type checking in Python.

---

## How to Run the Project
1. Ensure you have `python3.7` installed.
2. Validate the type annotations using `mypy` by running:
   ```bash
   mypy file_name.py
   ```
3. Run the Python scripts as usual:
   ```bash
   python3 file_name.py
   ```
