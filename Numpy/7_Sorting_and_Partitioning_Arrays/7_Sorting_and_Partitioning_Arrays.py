import numpy as np


a = np.array([2, 1, 4, 3, 5]) # Set up an unsorted array
np.sort(a) # Sorts the array

b = ([7, 6, 9, 10, 8])
b.sort() # Sorts the array in place

c = np.array([2, 1, 4, 3, 5]) # Create an array
d = np.argsort(c) # Return the postions of the sorted elements
e = c[d] # Create a sorted array using the new array


# Sorting along rows and columns
g = np.random.randint(0, 10, (4, 6))
h = np.sort(g, axis=0) # Sort each column of g
i = np.sort(g, axis=1) # Sort each row of g


# Partitioning
j = np.array([7, 2, 3, 1, 6, 5, 4])
k = np.partition(j, 3) # First three items are the smallest three items order is arbritrary
l = np.partition(g, 2, axis=1) # First 2 slots in each row contain the lowest values