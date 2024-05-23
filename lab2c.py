#!/usr/bin/env python3
import sys

# Checking if the correct number of command-line arguments are provided
if len(sys.argv) != 3:
    print("Usage: ./lab2c.py <name> <age>")
    sys.exit(1)

# Assigning command-line arguments to variables
name = sys.argv[1]
age = int(sys.argv[2])

# Printing the output
print(f"Hi {name}, you are {age} years old.")

