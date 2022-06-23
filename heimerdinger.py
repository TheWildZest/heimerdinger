#Treshold
import math
import matplotlib.pyplot as plt
import numpy as np

print('Adja meg a küszöbértéket!')

#Init variables
c = int(input())
i = c - 2

#If the given point is on or above the main diagonal, 'h' is the 'y' coordinate of the point
#else 'h' is 'c-1'
def calc_hasznossag(x, y):
    if y >= -1 * x + c:
        h = y
    else:
        h = c - 1

    return h

def calc_binomial(n, k):
    return math.factorial(n) / (math.factorial(k) * math.factorial(n - k))

def to_maximise(probs):
    array = []
    for p in probs:
        sum = 0
        for k in range(i):
            #Calculate 'hasznossag'
            h = calc_hasznossag(2 * (c - (2 + i + k)), i + k)
            
            
            #Calculate further binomial and exponential components
            exponent = c - (2 + i) - k
            b = calc_binomial(i, k) * pow(p, exponent) * pow(1 - p, k)

            #Put the quation together
            sum = sum + h * b
            print(sum)
        
        array.append(sum)

    return array


x = np.linspace(0, 1, 1000)
y = to_maximise(x)

# x = np.linspace(0, 2 * np.pi, 200)
# y = np.sin(x)
# print('linespace:', x)
# print('values:', y)

fig, ax = plt.subplots()
ax.plot(x, y)
plt.show()