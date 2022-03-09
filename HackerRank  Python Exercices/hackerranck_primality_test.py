#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'primality' function below.
#
# The function is expected to return a STRING.
# The function accepts INTEGER n as parameter.
#

def primality(n):
    if n == 1:
        return "Not prime"
    for x in range(2,int(n**(1/2)+ 1)):
        if n %  x== 0:
            return "Not prime"
    return "Prime"
    # Write your code here

print(primality(104729))