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

- **Bash**: Basics of Command line usage
- **Integrated Development Environment (IDE)**: Work in a unified workspace
- **Version control**: Save and manage changes to code
- **Jupyter Notebook**: Interactive computing and data visualization
- **Environment manager**: Conda, uv, etc.
- **Formatter/linter**: Tools to make code clean and consistent.
- **Testing**: Ensuring code works as intended.
- **AI coding tools**: Pair coding with intelligent LLMs.

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

## Part 1

- **Bash**: Basics of Command line usage
- **Integrated Development Environment (IDE)**: Work in a unified workspace.
- **Version control**: Save and manage changes to code.
- **Jupyter Notebook**: Interactive computing and data visualization.

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

**BASH**: a CLI available on most Linux and macOS operating systems, and can be installed on Windows.

- **Key Usage**:
  - Navigating and managing the file system
  - Running commands
  - Redirection and piping
  - Using version control (e.g., `git`)
  - Remote access (e.g., `ssh`, `scp`)
  - Automating tasks with scripts

---

## Example of Bash commands

```bash
# List files in the current directory
ls
# Change directory to 'Documents'
cd Documents
# Create a new directory called 'my_project'
mkdir my_project
# Change directory to 'my_project'
cd my_project
# Create a new file called 'script.sh'
touch script.sh
# Open 'script.sh' in a text editor (e.g., nano)
nano script.sh
# Check the current working directory
pwd
# Copy a file from one directory to another
cp /path/to/source/file.txt /path/to/destination/
# Move a file from one directory to another
mv /path/to/source/file.txt /path/to/destination/
# Remove a file
rm /path/to/file.txt
```

---

## Integrated Development Environment (IDE)

**IDEs** provide a unified workspace for coding, debugging, and testing.

- **Examples**: RStudio, MATLAB, PyCharm, Spyder, **VSCode**.
- **Key VSCode features**:
  - Code editor with syntax highlighting
  - Integrated terminal
  - Version control integration
  - Support for multiple programming languages
  - Installation of extensions for package management, linting, formatting, code completion, debugging, etc.

---

## Version Control

- **Version control**: tracking changes to files over time, allowing you to recall specific versions later.

- **Benefits**:
  - Recall specific versions later
  - Never lose code
  - Implement collaborative workflows

* A **version control system (VCS)** is a tool that helps us do this.

---

## Git and GitHub

- **Git** is a popular version control system
- **GitHub** is a web-based platform for hosting Git repositories, enabling collaboration and sharing of code.
- Other platforms: GitLab, Bitbucket, etc.
- **Key Git commands**:
  - `git init`: Initialize a new Git repository
  - `git clone <repo_url>`: Clone a remote repository
  - `git add <file>`: Stage changes for commit
  - `git commit -m "message"`: Commit staged changes with a message
  - `git push`: Push local commits to the remote repository
  - `git pull`: Fetch and merge changes from the remote repository
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

![Using global env width:cm height:17cm](..\bin\local_git.png)

---
<!--
_class: lead
-->

![Using global env width:15cm height:18cm](..\bin\local_git.png)

---

## Jupyter Notebook

---

## Summary

- Use a linter and formatter (**Ruff**) to maintain a consistent style in your Python code
- Use **uv** to manage virtual environments and dependencies in Python
- Use **GitHub Copilot** to help you write code faster and with fewer errors
- Use **pdocs** to generate documentation for your Python projects
