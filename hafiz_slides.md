---
marp: true
theme: gaia
paginate: true
_paginate: skip
backgroundColor: #fff
color: #000
size: 16:9
# header: 'Header content'
# footer: 'Footer content'
---
<!--
_class: lead
-->
# AMS Bootcamp 2025: Bash Shell, GitHub, and Python

---

## Outline

- **Bash**: Basics of Bash scripting and command line usage.
- **Integrated Development Environment (IDE)**: Code in a unified workspace.
- **Version control**: GitHub, GitLab, Bitbucket, etc.
- **Jupyter Notebook**: Interactive computing and data visualization.
- **Environment manager**: Conda, uv, etc.
- **Formatter/linter**: Tools to make code clean and consistent.
- **Testing**: Ensuring code works as intended.
- **AI coding tools**: Pair coding with intelligent LLMs.

---

## Part 1

- **Bash**: Basics of Bash scripting and command line usage.
- **Integrated Development Environment (IDE)**: Code in a unified workspace.
- **Version control**: GitHub, GitLab, Bitbucket, etc.
- **Jupyter Notebook**: Interactive computing and data visualization.

---

## BASH (Bourne-Again **SHell**)

> **Shell** is an interface between the user and the operating system, allowing users to interact with the system through commands.
* Can be a:
  * **command-line interface (CLI)** or a 
  * **graphical user interface (GUI)**.

---

## **Bash** (Bourne-Again SHell)

> **Bash**: A command-line interface (CLI) for interacting with the operating system.

- **Why**: To use git and GitHub, and for remote access.
- **Examples**: Bash (Linux/MacOS), PowerShell (Windows).
- **Key concepts**:
  - Navigating the file system
  - Running commands
  - Creating and editing files
  - Scripting basics
  - Using environment variables
  - Redirection and piping
  - File permissions
  - Using command-line tools
  - Using package managers (e.g., `apt`, `brew`)
  - Using version control (e.g., `git`)
  - Remote access (e.g., `ssh`, `scp`)
  - Using text editors (e.g., `nano`, `vim`, `emacs`)
  - Using command-line utilities (e.g., `grep`, `sed`, `awk`)
  - Using command-line tools for data processing (e.g., `cut`, `sort`, `uniq`)
  - Using command-line tools for file management (e.g., `find`, `xargs`, `tar`)
  - Using command-line tools for system monitoring (e.g., `top`, `htop`, `ps`)

---

## Project Directory Structure

* **`src`**: Code directly related to project.
* **`scripts`**: Specific implementations of code.
* **`tests`**: Tests for your project.
* **`data`**: Data for your project.
* **`docs`**: Documentation for your project.
* **Environment files**: `requirements.txt`, `environment.yml`, or `pyproject.toml`.
* **`LICENSE`**: Guide for how your project can be used by others.
* **`README`**: Information about your project.
<!-- - **.gitignore file**: The file that contains the files and directories that should be ignored by Git. It should be named `.gitignore`. -->

---

## Python Style

**PEP 8** gives the coding conventions for the Python code. Some style considerations included in PEP8 are:

- **Naming conventions**
- **Documentation**
- **Code layout and whitespaces**

---

## Naming conventions

Naming conventions help to make the code more  understandable.

- **Use representative names for variables, functions, and classes.**

```python
def calculate_area(radius):
    return 3.14 * radius ** 2
```

- **Variables**: `lowercase_with_underscores`.
- **Constants**: `UPPERCASE_WITH_UNDERSCORES`.
- **Classes**: `CamelCase`.
- **Functions**: `lowercase_with_underscores`.
<!-- - **Modules**: `lowercase_with_underscores`. -->

<!-- ```python
def my_function():
    pass

class MyClass:
    pass

``` -->

---

## Documentation

- Functions, scripts and classes should have docstrings that describe their purpose and usage.
- Common docstring formats include:
  - **Google style**: [Google Python Style Guide](https://google.github.io/styleguide/pyguide.html)
  - **NumPy/SciPy style**: [Numpy Documentation Style Guide](https://numpydoc.readthedocs.io/en/latest/format.html)
  - **reStructuredText**: [reStructuredText Markup Specification](https://docutils.sourceforge.io/rst.html)
  
- **Typehints**: Type hints are a way to indicate the expected types of function arguments and return values. They make it easier to debug code

---

## Example of docstring and type hints

```python
def calculate_area(radius: float) -> float:
    """
    Calculate the area of a circle.

    Parameters
    ----------
    radius : float
        The radius of the circle.

    Returns
    -------
    float
        The area of the circle.
    """
    return 3.14 * radius ** 2
```

---

## Environment Reproducibility

- Create virtual environments to isolate environments for projects.
- This isolation helps to:
  - install of packages and dependencies without affecting the system-wide Python installation
  - avoid version conflicts between different projects.
  - ensure we can reproduce the environment in which a piece of software was developed or tested.
- Create **requirements.txt** and **environment.yml** files to specify the dependencies of your project. **pyproject.toml** also has project configuration
<!-- - Use **pyproject.toml** to specify the dependencies and project configuration. -->

---

![Using global env width:30cm height:17cm](bin\virtual_env1.png)

---

![Using global env width:30cm height:17cm](bin\virtual_env2.png)

---

## Tools to make your life easier

Popular tools that can help manage python projects and environments:

- **uv**: A command-line utility for managing virtual environments.
- **GitHub Copilot**: AI-powered code completion tool that can help you write code faster.
- **ruff**: For formatting and linting Python code.
- **pdocs**: A documentation generator for Python projects that can help you create high-quality documentation quickly and easily.

---

## Using uv

To start a new project using uv, run the command:

```bash
uv init
```

To install a package using uv, run the command:

```bash
uv add <package>
```

To create a requirements.txt file using uv, run the command:

```bash
uv pip compile pyproject.toml -o requirements.txt
```

---

### Using Ruff

Ruff is easy to use and can be installed using conda/pip:

```bash
pip install ruff
conda install ruff
```

To lint a Python file using Ruff, you can run the command:

```bash
ruff check <filename>
```

To format a Python file using Ruff, you can run the command:

```bash
ruff format <filename>
```

---

## Using pdocs

pdocs is a documentation generator for Python projects that can help you create high-quality documentation quickly and easily.

```bash
pip install pdocs
```

To generate documentation for a Python project using pdocs, you can run the command:

```bash
pdocs --html <project_directory> --output-dir <output_directory>
```

---

## Summary

- Use a linter and formatter (**Ruff**) to maintain a consistent style in your Python code
- Use **uv** to manage virtual environments and dependencies in Python
- Use **GitHub Copilot** to help you write code faster and with fewer errors
- Use **pdocs** to generate documentation for your Python projects
