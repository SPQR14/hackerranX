#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'closedPaths' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER number as parameter.
#

def closedPaths(number):
    # Write your code here
    paths = 0
    while(number != 0):
        d = number % 10
        if(d == 0 or d == 4 or d == 6 or d == 9):
            paths = paths + 1
        elif(d == 8):
            paths = paths + 2
        number = number // 10
    return paths

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    number = int(input().strip())

    result = closedPaths(number)

    fptr.write(str(result) + '\n')

    fptr.close()
