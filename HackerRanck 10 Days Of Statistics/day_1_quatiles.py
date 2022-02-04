#!/bin/python3

from statistics import median
#
# Complete the 'quartiles' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

n = int(input())
x = sorted(list(map(int, input().split())))
from statistics import median
print(int(median(x[:n//2])))
print(int(median(x)))
print(int(median(x[(n+1)//2:])))