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

- **Bash**: Basics of Bash scripting and command line usage.
- **Integrated Development Environment (IDE)**: Code in a unified workspace.
- **Version control**: GitHub, GitLab, Bitbucket, etc.
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

- **Why**: To use git and GitHub, and for remote access.
- **Key concepts**:
  - Navigating and managing the file system
  - Running commands
  - Scripting basics
  - Using environment variables
  - Redirection and piping
  - File permissions
  - Using version control (e.g., `git`)
  - Remote access (e.g., `ssh`, `scp`)

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
# Run the script
bash script.sh
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

- **Why**: Provides a unified workspace for coding, debugging, and testing.
- **Examples**: RStudio, MATLAB, PyCharm, Spyder, VSCode.
- **Key features**:
  - Code editor with syntax highlighting
  - Integrated terminal
  - Debugging tools
  - Version control integration
  - Package management
  - Code completion and suggestions
  - Project management
  - Support for multiple programming languages
- **Recommendation**: Install VSCode for a versatile and powerful IDE experience.
- **Extensions**: Explore the VSCode marketplace for extensions that enhance your development workflow.

---

## Version Control

- **Why**: Never lose code, and track history.

---

## Summary

- Use a linter and formatter (**Ruff**) to maintain a consistent style in your Python code
- Use **uv** to manage virtual environments and dependencies in Python
- Use **GitHub Copilot** to help you write code faster and with fewer errors
- Use **pdocs** to generate documentation for your Python projects
