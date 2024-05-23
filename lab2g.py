#!/usr/bin/env python3
#Author: ISRAEL OLUWAJUWON
#Seneca_ID: IAOLUWAJUWON
#Date Created: 2024/05/23

import sys

# Checking if a command line argument was entered
if len(sys.argv) > 1:

# Using an integer object named timer with a value of 10
    timer = int(sys.argv[1])

else:
    # Assigning the default value of 3 to an object named timer if no argument was entered
    timer = 3

# While loop that repeats until timer equals 0
while timer != 0:
    print(timer)
    timer = timer - 1

# Print the EXACT OUTPUT after the loop
print('blast off!')
