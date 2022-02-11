#!/bin/python3
import math
import os
import random
import re
import sys



#
# Complete the 'number_in_sequence' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. LONG_INTEGER a
#  2. LONG_INTEGER b
#  3. LONG_INTEGER c
#

def number_in_sequence(a, b, c):
    if c == 0:
        if a == b:
            return "YES"
        else:
            return "NO"
    elif((b - a) % c == 0):
        return "YES"
    else:
        return "NO"
    pass
    # Write your code here

print(number_in_sequence(-56, 100, 5))

"""
s_1 = 1
s_2 = 1 + 3 = 4 
s_3 = 4 + 3 = 7

Por lo tanto 7 pertenece a la secuencia y retorna "YES"

a = s_1
c = s_i+1, s_i-1
b = s_i 


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a, b, c = map(int, input().strip().split(" "))

    result = number_in_sequence(a, b, c)

    fptr.write(result + '\n')

    fptr.close()
"""