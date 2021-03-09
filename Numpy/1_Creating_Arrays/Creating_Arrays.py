import numpy as np


# CREATING ARRAYS FROM LISTS
# Creates a standard array
a = np.array([1, 4, 2, 5, 3])

# Creates a standard array with a specified data type
b = np.array([1, 4, 2, 5, 3], dtype="float32")

# Multi dimensinal array from nested list
c = np.array([range(i, i + 3) for i in [2, 7, 6]])


# CREATING ARRAYS FROM ROUTINES
# Creates an array filled with zeros
d = np.zeros(10, dtype=int)

# Creates an array filled with ones
e = np.ones(10, dtype=int)

# Creates a 4 x 6 array filled with chosen value
f = np.full((4, 6), 28.9)

# Creates a linear sequence starting at 1 ending at 22 (non-inclusive) stepping in 3
g = np.arange(0, 22, 3)

# Creates an array of 25 values evenly spaced between 1 - 4 (inclusive)
h = np.linspace(1, 4, 25)

# Creates a 4 x 6 array of values between 0 and 1
i = np.random.random((4, 6))

# Creates a 5x4 random array of normally distributed values
# with mean 0 and a standard deviation 2
j = np.random.normal(0, 2, (5, 4))

# Creates a 4x4 array of random integers in range 0 - 20
k =  np.random.randint(0, 20, (4, 4))

# Create a 5 x 5 identity matrix
l = np.eye(5)

# Create an unitialised array of 7 integers
# the values will be whatever exists in the memory location.
m = np.empty(7)