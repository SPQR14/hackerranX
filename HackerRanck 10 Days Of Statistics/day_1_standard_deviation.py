#!/bin/python3

#
# Complete the 'stdDev' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def stdDev(arr): 
    mean = sum(arr)/len(arr)
    l = []
    for x in arr:
        print(x - mean)
        l.append((x - mean)**2)
    standard_deviation = (sum(l)/len(arr))**(1/2)
    print("{:.1f}".format(standard_deviation))
    # Print your answers to 1 decimal place within this function

f = [10, 40, 30, 50, 20]
stdDev(f)

"""
if __name__ == '__main__':
    n = int(input().strip())

    vals = list(map(int, input().rstrip().split()))

    stdDev(vals)
"""