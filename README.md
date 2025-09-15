# AI programming assistant

This is a test project to learn how to create my own AI programming assistant.

## Local development

### Prerequisites
**To iterate on this connector, make sure to complete this prerequisites section.**

#### Minimum Python version required `= 3.10.0`

#### Build & Activate Virtual Environment and install dependencies
From this connector directory, create a virtual environment:
```
python -m venv .venv
```

This will generate a virtualenv for this module in `.venv/`. Make sure this venv is active in your
development environment of choice. To activate it from the terminal, run:
```
source .venv/bin/activate
pip install -r requirements.txt
```

### Locally running 
For working with AI_programming_assistant.ipynb install jupyter or open this file with **[`Google Colab`](https://colab.google/)** 

## Description
This project demonstrates an AI-powered programming assistant built using a large language model (LLM) and LangChain. The assistant is designed to help developers by analyzing code, identifying errors, and providing actionable recommendations for fixing them.

Key features:
- Code error detection – Automatically identifies potential bugs or issues in your code.
- Fix suggestions – Provides clear, actionable recommendations to correct errors.
- LLM-powered – Leverages the capabilities of modern large language models for intelligent code understanding.
- LangChain integration – Uses LangChain to structure prompts, maintain context, and improve interaction quality.
- This project is intended as a learning experiment to explore how AI can assist in programming workflows and code debugging.

The source code consists of two files: my_project/main.py and my_project/utils.py. Several intentional errors were introduced in these files, including both obvious and subtle bugs.

The assistant was asked three questions regarding the code. Below are the questions along with the assistant’s responses:

### Q-1: There is an error in the calculate_area function in main.py. Find it and suggest a fix.

Result:
```
---
Your question: There is an error in the calculate_area function in main.py. Find it and suggest a fix.
---
Answer:
The error in the `calculate_area` function is that it incorrectly calculates the area by adding the `width` and `height` instead of multiplying them. To fix this, you should update the function to multiply the two parameters. 

Here is the corrected function:

python
def calculate_area(width, height):
    return width * height

With this change, the function will correctly calculate the area of a rectangle.

Source code:
--------------------
Файл: my_project\main.py
def calculate_area(width, height):
    return width + height

def greet_user(name):
    print(f"Hello, {name2}!")

if __name__ == "__main__":
    greet_user("Viktor")

    area = calculate_area(5, 10)
    print(f"The area is: {area}")
--------------------
Файл: my_project\utils.py
# utils.py

def list_to_string(input_list):
    """Converts a list of items to a comma-separated string."""
    result = ""
    for item in input_list:
        result += str(item) + ", "
    return result.strip().strip(',')

def add_numbers(a, b):
    return a + b
```

### Q-2: There is add_numbers() functiokn in utils.py file. Create same function for multiplication of variables and use it in calculate_area()

Result:
```
==================================================
Your question: There is add_numbers() functiokn in utils.py file. Create same function for multiplication of variables and use it in calculate_area()
==================================================
Answer:
To create a function for multiplication of variables and use it in the `calculate_area()` function, you can follow these steps:

1. Define a new function called `multiply_numbers` in `utils.py`.
2. Modify the `calculate_area` function to use the new multiplication function, instead of adding the width and height.

Here's the updated code:

python
# utils.py

def list_to_string(input_list):
    """Converts a list of items to a comma-separated string."""
    result = ""
    for item in input_list:
        result += str(item) + ", "
    return result.strip().strip(',')

def add_numbers(a, b):
    return a + b

def multiply_numbers(a, b):
    return a * b  # New multiplication function

# main.py

def calculate_area(width, height):
    return multiply_numbers(width, height)  # Use multiplication for area calculation

def greet_user(name):
    print(f"Hello, {name}!")

if __name__ == "__main__":
    greet_user("Viktor")

    area = calculate_area(5, 10)
    print(f"The area is: {area}")


Now, the `calculate_area` function correctly computes the area by multiplying width and height using the newly created `multiply_numbers` function.

Source code:
--------------------
Файл: my_project\main.py
def calculate_area(width, height):
    return width + height

def greet_user(name):
    print(f"Hello, {name2}!")

if __name__ == "__main__":
    greet_user("Viktor")

    area = calculate_area(5, 10)
    print(f"The area is: {area}")
--------------------
Файл: my_project\utils.py
# utils.py

def list_to_string(input_list):
    """Converts a list of items to a comma-separated string."""
    result = ""
    for item in input_list:
        result += str(item) + ", "
    return result.strip().strip(',')

def add_numbers(a, b):
    return a + b
```

### Q-3: Fix a next bug: 
```
Traceback (most recent call last):
  File "F:\work\AI\LangChain_01\my_project\main.py", line 8, in <module>
    greet_user("Alice")
  File "F:\work\AI\LangChain_01\my_project\main.py", line 5, in greet_user
    print(f"Hello, {name2}!")
NameError: name 'name2' is not defined. Did you mean: 'name'?
```

Result:
```
==================================================
Your question: Fix a next bug: 
Traceback (most recent call last):
  File "F:\work\AI\LangChain_01\my_project\main.py", line 8, in <module>
    greet_user("Alice")
  File "F:\work\AI\LangChain_01\my_project\main.py", line 5, in greet_user
    print(f"Hello, {name2}!")
NameError: name 'name2' is not defined. Did you mean: 'name'?

==================================================
Answer:
To fix the bug, you need to replace `name2` with `name` in the `greet_user` function. Here's the corrected code:

python
def greet_user(name):
    print(f"Hello, {name}!")


Now, the function correctly uses the `name` parameter that is passed to it. After making this change, the code will work without raising a `NameError`.

Source code:
--------------------
Файл: my_project\main.py
def calculate_area(width, height):
    return width + height

def greet_user(name):
    print(f"Hello, {name2}!")

if __name__ == "__main__":
    greet_user("Viktor")

    area = calculate_area(5, 10)
    print(f"The area is: {area}")
--------------------
Файл: my_project\utils.py
# utils.py

def list_to_string(input_list):
    """Converts a list of items to a comma-separated string."""
    result = ""
    for item in input_list:
        result += str(item) + ", "
    return result.strip().strip(',')

def add_numbers(a, b):
    return a + b
```
