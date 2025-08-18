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

# BREAK

Take a break and stretch your legs

---

# Part II

- **Environment manager**: **`conda`**, **`uv`**, etc.
- **Formatting & linting**: Tools to make code clean and consistent.
- **Testing**: Ensuring code works as intended.
- **AI coding tools**: Pair coding with intelligent LLMs.

---

# Environment management

- **Motivation:** Make code reproducible by identifying dependencies

- **Examples:** **`pip venv`**, **`conda`**, [**`uv`**](https://docs.astral.sh/uv/)

<!--
Caveat: I am very new to many of these tools, but I will try to share my personal perspective and the tricks I have found useful.
For Python code to run, you need to have the right version of Python and external libraries installed.
In other words, you need to have the right "environment".
Environment managers automate this process. 
Python has a built-in environment manager called "pip venv", but there are also popular third-party tools like "conda" and "uv".
My favorite is "uv" because it is the easiest to use, incredibly fast, and works well with other tools I'll mention later.
Installing and activating an environment is as easy as 
**`uv sync`** 
-->

---

# Environment management with [**`uv`**](https://docs.astral.sh/uv/)

- **Basic commands**: 
    **`uv sync`**
    **`uv add`**

- Control all [**`uv`**](https://docs.astral.sh/uv/) settings in **`pyproject.toml`**

<!--
Installing and activating an environment is as easy as 
**`uv sync`** 
-->

---

# Formatting

- **Motivation:** Enforce consistent style (spacing, line lengths, etc.)

- **Examples:** **`isort`**, **`black`**, [**`ruff`**](https://docs.astral.sh/ruff/)

<!--
Good code is well-organized, stylistically consistent, and free of bugs and errors.
Formatters and linters are tools that help achieve these traits in your code.
Formatters improve the visual appearance of your code without changing functionality.
They enforce consistent style by controlling spacing, line lengths, indentation, etc.
Examples of formatters include isort, black, and ruff.
isort sorts imports alphabetically and automatically separates them into sections.
black reformats entire files, ensuring a consistent style throughout.
ruff is also a general formatter, that can basically do anything isort or black can do but faster, and its my preferred tool.
-->

---

# Linting

- **Motivation:** Identify and fix potential bugs and remove logically unnecesssary code

- **Examples:** **`pylint`**, **`flake8`**, [**`ruff`**](https://docs.astral.sh/ruff/)

<!--
Linters identify style violations, but also potential bugs and errors like unused variables, missing imports, or more subtle bugs beyond obvious syntactic errors.
There are a handful of popular and customizable linters, including flake8, pylint, and ruff.
You'll notice that we see ruff again here because it is both a formatter and a linter.
And yet again, my favorite tool here is "ruff" because it can do almost everything the other tools can but faster.
-->

---

# Formatting & linting with [**`ruff`**](https://docs.astral.sh/ruff/)

- **Format command:**
**`uv run ruff format file_to_be_formatted.py`**

- **Lint command:**
**`uv run ruff check --fix file_to_be_linted.py`**

- Or, simply use VSCode's **`ruff`** extension and format-on-save.

- Control all [**`ruff`**](https://docs.astral.sh/ruff/) settings (i.e. [rules](https://docs.astral.sh/ruff/rules/)) in **`pyproject.toml`**

<!--
To format with ruff, just "uv add ruff" as a dependency, then run "ruff format" on the file as shown.
To lint with ruff, just run "ruff check" on the file as shown.
Linting technically only identifies issues, it doesn't necessarilly fix them.
To have ruff fix any issues for which automatic fixes are available, add the --fix flag.
Lets look at an example.

However, although these commands are relatively straightforward, they are not they way that use ruff.
A big reason I love ruff is that there is a VSCode extension for it.
This allows ruff to provide real-time visual format & lint feedback.
Although we do no have the time to show you, I recommend using format-on-save to automatically format and fix linting issues every time you ctrl+s save a file.
-->

---

# Formatting & linting with [**`ruff`**](https://docs.astral.sh/ruff/)

- **Format command:**
**`uv run ruff format file_to_be_formatted.py`**

- **Lint command:**
**`uv run ruff check --fix file_to_be_linted.py`**

- Or, simply use VSCode's **`ruff`** extension and format-on-save.

- Control all [**`ruff`**](https://docs.astral.sh/ruff/) settings (i.e. [rules](https://docs.astral.sh/ruff/rules/)) in **`pyproject.toml`**

<!--
To format with ruff, just "uv add ruff" as a dependency, then run "ruff format" on the file as shown.
To lint with ruff, just run "ruff check" on the file as shown.
Linting technically only identifies issues, it doesn't necessarilly fix them.
To have ruff fix any issues for which automatic fixes are available, add the --fix flag.

However, although these commands are relatively straightforward, they are not they way that I use ruff.
A big reason I love ruff is that there is a VSCode extension for it.
This allows ruff to provide real-time visual format & lint feedback.
Although we do no have the time to show you, I also recommend using format-on-save to automatically format and fix linting issues every time you ctrl+s save a file.

Finally, all ruff settings, like uv dependencies, are stored in pyproject.toml.

Lets look at an example:
1. Show format_lint_example.py
2. Point out formatting issues
3. Enable ruff extension -- 41 problems!
4. Hover over formatting issues
5. Run `uv run ruff format format_lint_example.py`
6. Use ctrl+z and ctrl+shift+z to undo and redo changes, highlighting specific changes from top to bottom
7. Go to pyproject.toml and highlight ruff format settings
8. Change line-length to 30 (way too short), and show how this immediately causes formatting issues in format_lint_example.py, then change back
9. Point out how there are still yellow squiggles in format_lint_example.py (18 problems); some of these are formatting issues ruff doesn't fix automatically (like "line too long"), but others are actually linting issues because they involve code syntax rather than format (e.g. truth comparison, unused variable)
10. Run 'uv run ruff check --fix --unsafe-fixes format_lint_example.py' to identify linting issues and aggressively fix those for which automatic fixes exist
11. Use ctrl+z and ctrl+shift+z to undo and redo changes, highlighting specific changes from top to bottom
11. Hover over the remaining linting issue, related to returning the condition directly and show an easy fix (also suggested by Copilot)
12. Disable "SIM" ruff rules in pyproject.toml, and show how this is another way to remove the final linting issue
13. Compare before and after


Hopefully this example demonstrates that ruff is an easy, fast, and flexible way to enforce consistent style and catch bugs in your code.
-->

---

# Formatting & linting with [**`ruff`**](https://docs.astral.sh/ruff/)

![width:800px](../images/ruff_before_after.png)

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

- As a student, you can get GitHub Copilot Pro for free via the [Student Developer Pack](https://education.github.com/pack/)

<!--
Pair programming with an AI agent can help you write better code faster.
Agents can provide context-aware autocomplete suggestions, but also assist with code navigation, refactoring, generating tests, and much more.
-->