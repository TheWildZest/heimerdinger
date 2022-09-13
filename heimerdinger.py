from cmath import nan
import math
import numpy as np

import random


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


# Calculate usefulness above the main diagonal
# NOTE: the following calculations are made by a formula created by Mate Szalai
def calcUsefulness(j, i, p):
    # select all the possible target positions
    targetPoints = []
    for ind in range(j + 1):
        tp_j = 2 * (j - ind)
        tp_i = i + ind
        
        targetPoint = {}
        targetPoint['j'] = tp_j
        targetPoint['i'] = tp_i
        
        targetPoints.append(targetPoint)
    
    
    
    # Calculate a "heuristic" for each targetpoint and add them together
    sum = 0
    for k in range(len(targetPoints)):
        tp_j = targetPoints[k]["j"]
        tp_i = targetPoints[k]["i"]

        try:
            # The choosen targetpoint's usefulnes
            h = usefulnessMatrix[tp_j][tp_i]
            
            # # h = random.randint(0, c -1)
            # print("From: ", j, ", ", i)
            # print("To:   ", h_j, ", ", h_i, ": ", h)
            # print("--------------------")
        except IndexError:
            h = tp_i

        binomialPart = math.factorial(j) / (math.factorial(j - (j - k)) * math.factorial(j - k))
        probabilityPart = ( p ** (j - k) ) * ( (1-p) ** k)

        partSolution = h * binomialPart * probabilityPart

        sum = sum + partSolution


    return sum



for x in range(c_inc):
    for y in range(c_inc):
        # Set usefulnesses in the first row (y coordinate)
        if (x == 0):
            usefulnessMatrix[x][y] = y
        
        # Set usefulnesses on the main diagonal and below it (y coordinate)
        elif (c <= x + y):
            usefulnessMatrix[x][y] = y


for diag_index in range(c-1, 0, -1):
    for j in range(diag_index, 0, - 1):
        # Find the max usefulness for the given matrix element with the given p by 0.0001 precision
        samples = np.linspace(0, 1, 10000)
        
        i = diag_index - j
        
        maxVal = 0
        for p in samples:
            val = calcUsefulness(j, i, p)

            if (val > maxVal):
                maxVal = val


        # Set the calculated max usefulness
        usefulnessMatrix[j][i] = maxVal


# Print matrix
print('\n')
for i in range(c_inc):
    for j in range(len(usefulnessMatrix[i])):
        print(f'{usefulnessMatrix[i][j]:9.2f}', end="")
    
    print('\n')
