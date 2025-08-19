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

- **BASH**
- **Integrated Development Environment (IDE)**
- **Version control**
- **Jupyter Notebook**
- **Environment manager**
- **Formatter/linter**
- **Testing**
- **AI coding tools**

<!--
PART I

1:00pm - Social introduction, icebreakers (name, mac/windows/linux, favorite programming language)

1:10pm - Introduction, bash slide

1:17pm - Bash example

1:20pm - IDEs

1:25pm - Suggest installing VSCode

1:35pm - GitHub slide

1:40pm - GitHub example (clone our repo)

1:45pm - Jupyter Notebook

1:50pm - Jupyter Notebook example

PART II

2:00pm - Break

2:05pm - Environment management

2:10pm - Environment management example

2:15pm - Formatter/linter

2:20pm - Formatter/linter example

2:25pm - Testing

2:30pm - Testing example

2:40pm - AI coding tools

2:50pm - GitHub Copilot example

-->

---

### Resources

- AMS Bootcamp GitHub Repository: [https://github.com/bknutson0/ams-coding-bootcamp](https://github.com/bknutson0/ams-coding-bootcamp)
- Michael's bootcamp repo ([https://github.com/mivanit/bash-git-bootcamp](https://github.com/mivanit/bash-git-bootcamp)) and python projects template repo ([https://github.com/mivanit/python-project-makefile-template](https://github.com/mivanit/python-project-makefile-template))
- Course for scientific computing in python: [https://opensourcecourse.dev/osc_intro/intro.html](https://opensourcecourse.dev/osc_intro/intro.html)
- Microsoft introduction to Python: [https://vscodeedu.com/courses/intro-to-python](https://vscodeedu.com/courses/intro-to-python)
- Mines HPC guide: [https://rc-docs.mines.edu/pages/user_guides/new_user_guide.html](https://rc-docs.mines.edu/pages/user_guides/new_user_guide.html)

---

## Part 1 - Learning Objectives

- **Bash**: Basic Command line usage
- **Integrated Development Environment (IDE)**: Work in a unified workspace
- **Version control**: Track changes to code
- **Jupyter Notebook**: Interactive computing and data visualization

---

## BASH (Bourne-Again **SHell**)

**Shell** is an interface between the user and the operating system, allowing users to interact with the system through commands.

* Can be a:
  * Graphical User Interface (GUI) or a
  * **Command-Line Interface (CLI)**, examples include:
    * **BASH** (Linux/MacOS)
    * PowerShell, Command Prompt (Windows)
    * Zsh (Z Shell), Fish (Friendly Interactive Shell), Csh (C Shell), etc.

---

## **BASH** (Bourne-Again SHell)

**BASH**: a CLI available on most Linux and macOS operating systems. Can be installed on Windows  (e.g., via Git Bash ([https://git-scm.com/](https://git-scm.com/)))

* **Key Uses**:
  * Navigating and managing the file system
  * Running commands
  * Automating tasks with scripts
  * Using version control (e.g., `git`)
  * Remote access (e.g., `ssh`, `scp`)
  * Redirection and piping

---

## Example of Bash commands

- `ls` - list files in the current directory
- `cd` - change directory
- `pwd` - print working directory
- `mkdir` - make a new directory
- `touch` - create a new file
- `rm` - remove a file or directory
- `cp`/`mv` - copy/move files or directories
- `cat` - concatenate and display file contents
- other commands...

---

## Activity: Bash Commands

1. Open your terminal (Bash shell).
2. Print your current working directory.
3. Create a new directory called `ams_bootcamp`.
4. Change into the `ams_bootcamp` directory.
5. Create a new file called `hello_world.txt`.
6. Open `hello_world.txt` in a text editor (e.g., vim, nano).
7. Write "Hello, AMS Bootcamp!" in the file.
8. Save and exit the text editor.
9. List contents of `ams_bootcamp` directory to verify file was created.
<!-- 10. Remove the `hello_world.txt` file.
11. List the contents of the `ams_bootcamp` directory again to verify the file was removed.
12. Change back to your home directory.
13. Remove the `ams_bootcamp` directory.
14. List the contents of your home directory to verify the `ams_bootcamp` directory was removed. -->

---

## Demo: Automating tasks with scripts

Run `bash_intro.py` in the terminal

Run `bash_intro.sh` to illustrate how to automate tasks with scripts.

---

## Integrated Development Environment (IDE)

**IDEs** provide a unified workspace for coding, debugging, and testing.

* **Examples**: RStudio, MATLAB, PyCharm, Spyder, **VSCode**.
* **Key VSCode features**:
  * Code editor with syntax highlighting
  * Integrated terminal
  * Version control integration
  * Support for multiple programming languages
  * Installation of extensions for package management, linting, formatting, code completion, debugging, etc.

---

## Activity: Install VSCode

1. Download and install **Visual Studio Code** from [https://code.visualstudio.com/](https://code.visualstudio.com/).
<!-- 3. Install the following extensions:
   - Python
   - Jupyter
   - GitLens (for Git integration)
   - Pylance (for Python language support)
   - Prettier (for code formatting) -->
2. Create a new Python file (e.g., `hello.py`) and write a simple print statement:`print("Hello, AMS Bootcamp!")`
3. Open the integrated terminal in VSCode (View > Terminal).
4. Run the Python file using the integrated terminal:

   ```bash
   python hello.py
   ```

---

## Version Control

**Version control**: tracking changes to files over time.

- **Benefits**:
  - Recall specific versions later
  - Never lose code
  - Implement collaborative workflows

* A **version control system (VCS)** is a tool that helps us do this.

---

## Git

- **Git** is a popular version control system

- **Key Git commands**:
  - `git init`: Initialize a new Git repository
  - `git add <file>`: Stage changes for commit
  - `git commit -m "message"`: Commit staged changes
  - `git branch`: List, create, or delete branches

---
<!--
_class: lead
-->

## Version Tracking with Git

![Using global env width:30cm height:cm](..\bin\git-commits.png)

---
<!--
_class: lead
-->

## Branching and Merging

![Using global env width:30cm height:cm](..\bin\git-branch.png)

---
<!--
_class: lead
-->

![Using global env width:cm height:16cm](..\bin\local_git.png)

---

## Activity: Git

1. Open your terminal (Bash shell).
2. Create a new directory called `ams_git_demo`.
3. Change into the `ams_git_demo` directory.
4. Initialize a new Git repository in this directory using `git init`.
5. Create a new file called `README.md` and add some content to it.
6. Stage the file using `git add README.md`.
7. Commit the changes with a message using `git commit -m "Initial commit"`.
8. Check the status of your Git repository using `git status`.

---

**GitHub** is a web-based platform for hosting Git repositories, enabling collaboration and sharing of code.

* **Common Remote Repository Commands**:
  - `git clone <repo_url>`: Clone a remote repository
  - `git push`: Push local commits to the remote repository
  - `git pull`: Fetch and merge changes from the remote repository

---
<!--
_class: lead
-->

![Using global env width:cm height:16cm](..\bin\remote-git.png)

---

## Activity: Clone a GitHub Repository

- Clone the AMS Bootcamp repository ([https://github.com/bknutson0/ams-coding-bootcamp](https://github.com/bknutson0/ams-coding-bootcamp)) from GitHub to your local machine
* You can make changes but you cannot push them back to the original repository
* If you want to make changes, you can fork the repository to your own GitHub account and then clone that forked repository

---

## Extra Activity: GitHub

1. Create a GitHub account if you don't have one.
2. Create a new GitHub repository (e.g., `ams-bootcamp`).
3. Clone the repository to your local machine.
4. Create a new file in the cloned repository (e.g., `README.md`) and add some content.
5. Stage and commit your changes.
6. Push your changes to the remote repository on GitHub.
7. Verify that the changes appear in your GitHub repository.

---

## Jupyter Notebooks/Google Colab

- Interactive environments for data analysis and visualization
- Support for rich media output (e.g., plots, images)
- Easy sharing and collaboration

**Activity**: Open a Jupyter Notebook or Google Colab and copy and paste the content of the `bootcamp_example.py` file into various cells.

---

## Summary

- **BASH** provides a text-based interface to interact with the operating system
- IDEs like **VSCode** offer a unified workspace for coding, debugging, and testing
- Version control with **Git** and **GitHub** allows tracking changes to code and collaboration
- **Jupyter Notebook/Google Colab** enables prototyping, interactive computing, and data visualization

---

# Break

Take a 5 min break and stretch your legs

---

# Part II

- **Environment management**: make code reproducible
- **Formatting & linting**: make code clean and consistent
- **Testing**: ensure code works as intended
- **AI coding agents**: pair code with AI

<!-- 
Caveat: I am very new to many of these tools, but I will try to share my personal perspective and the tricks I have found useful.
Feel free to ask questions at any point.
-->

---

# Environment management

- **Motivation:** Make code reproducible by identifying and solving dependencies

- **Examples:** **`pip venv`**, **`conda`**, [**`uv`**](https://docs.astral.sh/uv/)

<!--
We begin with environment management.
For Python code to run, you need to have the right version of Python and external libraries/packages/dependencies installed.
In other words, you need to have the right "environment".
Environment managers automate and simplify this process. 
Python has a built-in environment manager called "pip venv", but there are also popular third-party tools like "conda" and "uv".
My favorite is "uv" because it is the easiest to use, installs incredibly fast, and works well with other tools -- but we'll talk about that later.
-->

---

# Environment management
![center](../images/dependency_graph.png)

<!--
An environment manager will try to install all dependencies.Most packages depend on other packages, creating a dependency graph as shown. 
Suppose we need to install packages A and B, and both depend on package C.
Then the environment will need to install all three.
Luckily, A requires C version greater than 1.2.3, and B requires C version less than 2.0.0, so any version inbetween will do.
-->

---

# Environment management
![center](../images/dependency_graph_conflict.png)

<!--
But sometimes packages have conflicting requirements.
For example, if package A requires version < 1.2.3 of package C, and package B requires version > 2.0.0 of package C, then there is a conflict.
In such cases, you may need to manually resolve the conflict by adjusting versions or even using alternative packages.
-->

---

# Environment management with [**`uv`**](https://docs.astral.sh/uv/)

- Install [**`uv`**](https://docs.astral.sh/uv/) [here](https://docs.astral.sh/uv/getting-started/installation/)

- **Basic commands**: 
**`uv init`**: create a new project
**`uv add <package>`**: add a dependency to the project
**`uv sync`**: install all dependencies
**`uv run <script.py>`**: run a script
**`uv help`**: display help information for uv commands

- Control all [**`uv`**](https://docs.astral.sh/uv/) settings and dependencies in **`pyproject.toml`**

<!--
Here are some basic uv commands ... 
To initialize uv in a new project, run "uv init".
To add a dependency, run "uv add" then the package name.
The command "uv sync" will rapidly install all dependencies, much faster than other environment managers.
To run a script, you would use "uv run" then the script name.
If you want to know what other commands are available, use the command "uv help".
-->

---

# Environment management with [**`uv`**](https://docs.astral.sh/uv/)

Let's practice using [**`uv`**](https://docs.astral.sh/uv/) and **`pyproject.toml`** to manage our environment.

<!--
1. uv init
2. uv tree
3. pyproject.toml
4. uv sync
5. uncomment "urllib3==2.0.0"
6. uv sync -> dependency conflict
7. remove version requirement or comment out (can edit pyproject.toml or use uv remove)
8. uv sync -> dependency resolved
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

However, although these commands are relatively straightforward, they are not they way that I use ruff.
A big reason I love ruff is that there is a VSCode extension for it.
This allows ruff to provide real-time visual format & lint feedback.
Although we do no have the time to show you, I also recommend using format-on-save to automatically format and fix linting issues every time you ctrl+s save a file.

Finally, all ruff settings, like uv dependencies, are stored in pyproject.toml.
-->

---

# Formatting & linting with [**`ruff`**](https://docs.astral.sh/ruff/)

Let's practice using [**`ruff`**](https://docs.astral.sh/ruff/) and **`pyproject.toml`** to format and lint **`src/format_lint_example.py`**.

<!--
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

![width:1100px](../images/ruff_before_after.png)

---

# Testing

- **Motivation:** Ensure code is working as intended

- **Examples:** ... **`pytest`**

- **To run tests:** save tests as **`tests/test_<name>.py`** then run the command **`uv run pytest`**

<!--
Good code is not just nicely formatted and free of obvious bugs and errors -- it actually works as intended.
Tests are essential for ensuring the code is behaving correctly.
This could mean that a function in a file works as you'd expect, or it could mean testing that one component of your code works correctly with another component.
Frequent testing ensures that as you make changes to your code, you don't break anything.
And if you do break something, you can quickly identify and fix the problem.
-->

---

# Testing

- You can create a [GitHub Action workflow](https://github.com/bknutson0/ams-coding-bootcamp/actions) so that GitHub automatically runs your tests on every push and pull request

- To do so, add **`.github/workflows/<name>.yml`** to your repo and enable Actions in your GitHub repository settings

- See the example in this repo

---

# AI agent 

- **Motivation:** Pair coding with an agent is the way of the future

- **Examples:** OpenAI Codex, Claude Code, GitHub Copilot

- AI agents can read your repo and suggest changes based on conversation

<!--
Pair programming with an AI agent can help you write better code faster.
Agents can provide context-aware autocomplete suggestions, but also assist with code navigation, refactoring, generating tests, and much more.
One convenience of these agents is that they have direct read access to your repo, so you don't have to do what I use to do: copy-paste blocks of code into ChatGPT.
Of course, it is important to review and understand suggested changes before accepting, especially for important parts of your code.
My usual workflow is to first have a conversation with the agent about high-level strategy.
As a relatively inexperienced programmer, I use this conversation to learn about software engineering best practices.
Then I decide on an approach and describe in as much detail as I can what I want the agent to implement.
The first implementation it generates is usually decent, but upon reviewing suggestions I almost always have to request modifications.
Overall, I have found this workflow helps me to power through small technical details, allowing me to spend more time on interesting problems.
Of course, just like with humans, sometimes agents suggest code with bugs that slip past inspection.
So proper testing to ensure the code is serving its purpose becomes even more important.
-->

---

# AI agent

- GitHub Copilot is a VS Code extension with a built-in interface that lets you select different models

- As a student, you can get GitHub Copilot Pro **for free** via GitHub's [Student Developer Pack](https://education.github.com/pack/), which gives you access to more advanced models

<!--
GitHub Copilot is a VS Code extension with a built-in interface that lets you select different models.
It is very convenient to have your main coding environment and the agent conversation integrated in one interface.
As a student, you can get GitHub Copilot Pro for free via the Student Developer Pack.
This gives you access to more advanced models, including GPT-5 and Claude Sonnet 4.
I have found that using advanced models can very dramatically improve the quality of conversation and suggestions made by the agent. 
There is a particular synergy between ruff and GitHub Copilot, because the agent can see the formatting and linting problems when it reads your code, and then automatically fix them when creating its suggestion.
This is particularly useful for easy problems that ruff cannot automatically fix like lines that are too long or simple logical reductions.
-->

---

# AI agent

Let's use GitHub Copilot to add a test for the `is_even()` function.

---

# Thank you!

If you enjoyed this presentation, please consider giving a star to our [GitHub repository](https://github.com/bknutson0/ams-coding-bootcamp)