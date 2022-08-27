from cmath import nan
import math
import matplotlib.pyplot as plt
import numpy as np

print('Choose the treshold!')

c = int(input())
c_inc = c + 1
usefulnessMatrix = []

# Init an n*n matrix with 0-s
for x in range(c_inc):
    row = []
    for y in range(c_inc):
        row.append(nan)
    
    usefulnessMatrix.append(row)

# Set usefulnesses on the main diagonal and below it (y coordinate)
# Above the main diagonal everything stays 0
for x in range(c_inc):
    for y in range(c_inc):
        if (c <= x + y):
            usefulnessMatrix[x][y] = y

# Calculate usefulness above the main diagonal
# NOTE: the following calculations are made by a formula created by Mate Szalai
def calcUsefulness(x, y, p):
    # Calculate the summa which needs to ba maximised later
    sum = 0
    for k in range(c - (x + y)):
        coordX = 2 * (c - (x + y + k))
        coordY = x + k

        try:
            usefulnessPart = usefulnessMatrix[coordX][coordY]

            binomialPart = math.factorial(c - (x + y)) / (math.factorial(c - x - y - k) * math.factorial(k))
            probabilityPart = math.pow(p, c - (x + y) - k) * math.pow(1 - p, k)

            partSolution = usefulnessPart * binomialPart * probabilityPart

            sum = sum + partSolution

        except IndexError:
            sum = y

    return sum

# Find the max usefulness for the given matrix element with the given p by 0.0001 precision
samples = np.linspace(0, 1, 10000)
for x in range(0, c):
    for y in range(0, c - x):
        maxVal = 0
        for p in samples:
            val = calcUsefulness(x, y, p)

            if (val > maxVal):
                maxVal = val

        # Set the calculated max usefulness
        usefulnessMatrix[x][y] = maxVal

# Print matrix
for i in range(c_inc):
    print(usefulnessMatrix[i])