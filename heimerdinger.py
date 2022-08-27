import math
import matplotlib.pyplot as plt
import numpy as np

print('Choose the treshold!')

c = int(input())
c_inc = c + 1
usefulnessMatrix = []

for x in range(c_inc):
    row = []
    for y in range(c_inc):
        row.append(0)
    
    usefulnessMatrix.append(row)

# If the given point is on or above the main diagonal, 'h' is the 'y' coordinate of the point
for x in range(c_inc):
    for y in range(c_inc):
        if (c <= x + y):
            usefulnessMatrix[x][y] = y
        elif( c - 1 <= x + y):
            usefulnessMatrix[x][y] = c - 1
        else:
            usefulnessMatrix[x][y] = 0

for i in range(c_inc):
    print(usefulnessMatrix[i])



# def calcBinomial(n, k):
#     return math.factorial(n) / (math.factorial(k) * math.factorial(n - k))

# def maximise(probs):
#     array = []
#     for p in probs:
#         sum = 0
#         for i in range(max_i):
#             # Calculate 'usefulness'
#             h = calcUsefulness(2 * (c - (2 + max_i + i)), max_i + i)
            
            
#             # Calculate further binomial and exponential components
#             exponent = c - (2 + max_i) - i
#             b = calcBinomial(max_i, i) * pow(p, exponent) * pow(1 - p, i)

#             # Put the quation together
#             sum = sum + h * b
#             print(sum)
        
#         array.append(sum)

#     return array