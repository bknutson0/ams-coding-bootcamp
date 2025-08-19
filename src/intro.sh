#!/bin/bash

# Bash script to run a Python file with parameters

# Get the directory where this bash script is located
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# Variables
PYTHON_FILE="$SCRIPT_DIR/intro.py"
NAME="Hafiz"
COLOR="Blue"
LUCKY_NUMBER=4

# Run Python file with arguments
python "$PYTHON_FILE" "$NAME" "$COLOR" "$LUCKY_NUMBER"
