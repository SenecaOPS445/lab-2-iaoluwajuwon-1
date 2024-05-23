#!/usr/bin/env python3
import sys

# Checking if the correct number of command-line arguments are provided
if len(sys.argv) != 3:
    print(f"Usage: {sys.argv[0]} name age")
    sys.exit(0)

# Assigning command-line arguments to variables
name = sys.argv[1]
age = sys.argv[2]

# Proceeding with the script only if exactly 2 arguments are provided
if len(sys.argv) == 3:
    # Printing the output
    print(f"Hi {name}, you are {age} years old.")

