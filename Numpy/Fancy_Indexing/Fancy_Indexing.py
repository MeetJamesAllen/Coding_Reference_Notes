import numpy as np

rand = np.random.RandomState(42)

x = rand.randint(100, size=10)

print(x)


print([x[3], x[7], x[2]]) # Accessing multiple elements


ind = [3, 7, 4] # Create an index array
print(x[ind]) # Use list to access array


ind = np.array([[3, 7],
               [4, 5]]) # Create a 2-dimensional index array


print(x[ind]) # Create new array with the shape of the index array and values of the original array


X = np.arange(12).reshape((3, 4)) # Create 2d array
print(X)

# Access multiple parts of the array
row = np.array([0, 1, 2])
col = np.array([2, 1, 3])

print(X[row, col])


X1 = (X[row[:, np.newaxis], col]) # Runs column request across each row
print(X1)

"""
print(X[2, [2, 0, 1]]) # Access row 2, elements 2, 0 and 1
print(X[1:, [2, 0, 1]]) # Access all rows from 1 and elements 2, 0 and 1
"""