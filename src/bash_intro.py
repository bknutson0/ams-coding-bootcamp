"""
This script takes three command line arguments: name, color, and lucky number.
It then prints a summary of the information provided.

Usage:
    python intro.py <name> <color> <lucky_number>
"""

import sys

if __name__ == "__main__":
    name = sys.argv[1]
    color = sys.argv[2]
    lucky_number = sys.argv[3]
    print(f"My name is: {name}, My favorite color is: {color}, My lucky number is: {lucky_number}")
