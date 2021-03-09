# -*- coding: utf-8 -*-
"""
Created on Mon Jan 25 06:49:30 2021

@author: james
"""

import numpy as np
import matplotlib.pyplot as plt
np.random.seed(0)

def compute_reciprocals(values):
    output = np.empty(len(values))
    for i in range(len(values)):
        output[i] = 1.0 / values[i]
    return output

values = np.random.randint(1, 10, size=5)
compute_reciprocals(values)

big_array = np.random.randint(1, 100, size=1000000)

print(compute_reciprocals(values))
print(1.0 / values)

x = np.arange(4)
print("x     =", x)
print("x + 5 =", x + 5)
print("x - 5 =", x - 5)
print("x * 5 =", x * 2)

x = np.array([3 - 4j, 4 -  3j, 2 + 0j, 0 + 1j])
x = np.abs(x)
y = len(x)

theta = np.linspace(0, np.pi, 3)