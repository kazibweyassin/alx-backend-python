# ALX Backend Python Curriculum

## Overview

This project focuses on Python Variable Annotations, providing you with tasks to improve your understanding of type annotations in Python. It covers general programming concepts and advanced Python topics such as type hints, Duck typing, and code validation using `mypy`. The structure of the curriculum also includes learning resources, a breakdown of the curriculum, and practical exercises to solidify the knowledge.

### Table of Contents

1. [Home](#home)
2. [My Planning](#my-planning)
3. [Projects](#projects)
4. [QA Reviews I can make](#qa-reviews-i-can-make)
5. [Evaluation Quizzes](#evaluation-quizzes)
6. [Curriculums](#curriculums)
7. [Concepts](#concepts)
8. [Conference Rooms](#conference-rooms)
9. [Servers](#servers)
10. [Sandboxes](#sandboxes)
11. [Tools](#tools)
12. [Video on Demand](#video-on-demand)
13. [Peers](#peers)
14. [Discord](#discord)
15. [My Profile](#my-profile)

---

## Curriculum

**Average Specialization Score:** 115.54%

### 0x00. Python - Variable Annotations

**Category:** Python, Back-end  
**Weight:** 1  
**Project Duration:** Mar 14, 2024, 6:00 AM – Mar 15, 2024, 6:00 AM  
**Review:** An auto-review will be conducted at the deadline

---

## Concepts

**For this project, you are expected to review:**

- [Advanced Python](#)

---

## Resources

Read or watch the following:

- [Python 3 Typing Documentation](https://docs.python.org/3/library/typing.html)
- [MyPy Cheat Sheet](https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html)

---

## Learning Objectives

By the end of this project, you will be able to:

1. Explain type annotations in Python 3.
2. Use type annotations to specify function signatures and variable types.
3. Understand Duck typing.
4. Validate your code using `mypy`.

---

## Requirements

### General

- Use `vi`, `vim`, or `emacs` as editors.
- Code will be interpreted/compiled on **Ubuntu 18.04 LTS** using **Python 3.7**.
- Files must end with a new line and start with `#!/usr/bin/env python3`.
- A `README.md` file is mandatory.
- Follow the `pycodestyle` style (version 2.5).
- All files must be executable.
- Include documentation for all modules, classes, and functions.

---

## Tasks

### 0. Basic Annotations - Add

Create a type-annotated function `add(a: float, b: float) -> float` that returns the sum of two floats.

**File:** `0-add.py`

### 1. Basic Annotations - Concat

Create a type-annotated function `concat(str1: str, str2: str) -> str` that concatenates two strings.

**File:** `1-concat.py`

### 2. Basic Annotations - Floor

Create a type-annotated function `floor(n: float) -> int` that returns the floor of a float.

**File:** `2-floor.py`

### 3. Basic Annotations - To String

Create a type-annotated function `to_str(n: float) -> str` that returns the string representation of a float.

**File:** `3-to_str.py`

### 4. Define Variables

Define and annotate the following variables:

- `a: int = 1`
- `pi: float = 3.14`
- `i_understand_annotations: bool = True`
- `school: str = "Holberton"`

**File:** `4-define_variables.py`

### 5. Complex Types - List of Floats

Create a type-annotated function `sum_list(input_list: List[float]) -> float` that returns the sum of a list of floats.

**File:** `5-sum_list.py`

### 6. Complex Types - Mixed List

Create a type-annotated function `sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float` that returns the sum of a mixed list.

**File:** `6-sum_mixed_list.py`

### 7. Complex Types - String and Int/Float to Tuple

Create a type-annotated function `to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]` that returns a tuple where the second element is the square of the int/float.

**File:** `7-to_kv.py`

### 8. Complex Types - Functions

Create a type-annotated function `make_multiplier(multiplier: float) -> Callable[[float], float]` that returns a function multiplying a float by `multiplier`.

**File:** `8-make_multiplier.py`

### 9. Let's Duck Type an Iterable Object

Annotate the parameters and return values of the function `element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]`.

**File:** `9-element_length.py`

---

## Author

Copyright © 2024 ALX, All rights reserved.
