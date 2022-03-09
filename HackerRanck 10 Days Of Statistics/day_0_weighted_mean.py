#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'weightedMean' function below.
#
# The function accepts following parameters:
#  1. INTEGER_ARRAY X
#  2. INTEGER_ARRAY W
#

def weightedMean(X, W):
    l = []
    for x, w in zip(X, W):
        l.append(x * w)
    return "{:.1f}".format(sum(l)/sum(W))
    pass
    # Write your code here


X = [10, 40, 30, 50, 20, 10, 40, 30, 50, 20]
W = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(weightedMean(X,W))


if __name__ == '__main__':
    n = int(input().strip())

    vals = list(map(int, input().rstrip().split()))

    weights = list(map(int, input().rstrip().split()))

    weightedMean(vals, weights)
