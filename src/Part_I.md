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

![Using global env width:30cm height:cm](..\images\git-commits.png)

---
<!--
_class: lead
-->

## Branching and Merging

![Using global env width:30cm height:cm](..\images\git-branch.png)

---
<!--
_class: lead
-->

![Using global env width:cm height:16cm](..\images\local_git.png)

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

![Using global env width:cm height:16cm](..\images\remote-git.png)

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
