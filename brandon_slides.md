---
marp: true
theme: gaia
paginate: true
backgroundColor: #ffffffff
color: #292531ff
size: 16:9
style: |
  code {
    color: #0969da;
    background-color: #ffffffff;
    padding: 2px 4px;
    border-radius: 3px;
  }

---

# Environment management

- **Motivation:** Make code reproducible by identifying dependencies

- **Examples:** **`pip venv`**, **`conda`**, **`uv`**

- **Basic commands**: 
    **`uv sync`**
    **`uv add`**

- Control all **`uv`** settings in **`pyproject.toml`**

<!--
For Python code to run, you need to have the right version of Python and external libraries installed.
In other words, you need to have the right "environment".
Environment managers automate this process. 
Python has a built-in environment manager called "pip venv", but there are also popular third-party tools like "conda" and "uv".
My favorite is "uv" because it is the easiest to use, incredibly fast, and works well with other tools I'll mention later.
Installing and activating an environment is as easy as 
**`uv sync`** 
-->

---

# Formatting & linting

- **Motivation:** Make code clean and consistent

- **Examples:** **`isort`**, **`black`**, **`pylint`**, **`mypy`**, **`ruff`**

- Control all **`ruff`** settings in **`pyproject.toml`**

<!--
Good code is well-organized, consistent, and free of bugs and errors.
Formatters and linters are tools that help achieve these traits in your code.
Formatters improve the visual appearance of your code without changing functionality.
They enforce consistent style by controlling spacing, line lengths, indententation, etc.
Linters identify style violations, but also potential bugs and errors like unused variables, missing imports, or more subtle bugs beyond obvious syntactic errors.
Linters add lint, or yellow squiggles, under potentially problematic code.
There are many kinds of formatters & linters that have different purposes.
My favorite is "ruff", made by the creators of "uv", because it is very fast and easy to use, and it does both formatting and linting.
ruff can do almost everything the other tools can.
-->

---

# Testing

- **Motivation:** Ensure code is working as intended

- **Examples:** **`pytest`**, GitHub Actions

<!--
Good code is not just nicely formatted and free of obvious bugs and errors -- it actually works as intended.
The 
-->
---

# AI coding tools

- **Motivation:** Pair coding with an intelligent LLM is the way of the future

- **Examples:** OpenAI Codex, Claude Code, GitHub Copilot