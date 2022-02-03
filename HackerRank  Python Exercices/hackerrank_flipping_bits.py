import math
import os
import random
import re
import sys

#
# Complete the 'flippingBits' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts LONG_INTEGER n as parameter.
#

def flippingBits(n):
    return(int("".join(["1" if i == "0" else "0" 
        for i in "{:032b}".format(n)]), 2))
    # Write your code here

print(flippingBits(3))