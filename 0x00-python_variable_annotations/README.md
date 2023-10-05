## Python Variable Annotation

This repository contains Python code and examples that I use to learn about variable annotation in Python. Variable annotation is a way to specify the expected type of a variable. This can help to make code more readable and maintainable, and it can also be used to catch errors early.

## Type annotations in Python 3

Python 3.5 introduced type annotations, which are a way to specify the expected type of a variable. Type annotations are optional, but they can be very helpful for making code more readable and maintainable.

To add a type annotation to a variable, simply add a colon (`:`), followed by the type of the variable. For example, the following code declares a variable `my_name` of type `str`:

```python
my_name: str = "Bard"


Type annotations can also be used for function parameters and return values. For example, the following code declares a function `add()` that takes two `int` parameters and returns an `int`:

python
def add(a: int, b: int) -> int:
  """Returns the sum of a and b."""
  return a + b


## Duck typing

Duck typing is a programming concept that states that the type of an object is determined by its behavior, rather than its declared type. In other words, if an object behaves like a duck, then it is a duck.

Python is a dynamically typed language, but it also supports duck typing. This means that you can use objects of different types in the same way, as long as they have the same methods.


## Validating code with Mypy

Mypy is a static type checker for Python. It can be used to validate your code and catch errors early.

mypy requires Python 3.8 and later to run

To use Mypy, simply install it with pip:


python3 -m pip install mypy

Then run mypy on files as:
`mypy code.py``
