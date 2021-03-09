import numpy as np
np.random.seed(0) # Seed to ensure result can be reproduced

# Create arrays for use in examples
x1 = np.random.randint(10, size=6) # One-dimensional array
x2 = np.random.randint(10, size=(3, 4)) # Two-dimensional array
x3 = np.random.randint(10, size=(3, 4, 5)) # Three-dimensional array

# Show attributes of an array
print("x3 ndim: ", x3.ndim) # Shows count of dimensiona
print("x3 shape:", x3.shape) # Shows shape of array
print("x3 size: ", x3.size) # Shows total number of elements
print("dtype:   ", x3.dtype) # Shows datatype of elements
print("itemsize:", x3.itemsize, "bytes") # Shows size of elements
print("nbytes:  ", x3.nbytes, "bytes", "\n") # Shows total size of array


# ACCESSING SINGLE ELEMENTS OF A ONE-DIMENSIONAL ARRAY
# print(x1) # Uncomment for use

a = x1[0] # Access first element

b = x1[4] # Access fifth element

c = x1[-1] # Access last element

d = x1[-2] # Access penultimate element


# ACCESSING SINGLE ELEMENTS OF A TWO-DIMENSIONAL ARRAY
# print (x2) # Uncomment for use

e = x2[0,0] # Access element in first row and first column

f = x2[2, 0] # Access element in third row, first column

g = x2[2, -1] # Access element in thrid row, last column

x2[0 , 0] = 12 # Modifies value
h = x2[0, 0] # Access new value


# ACCESSING SUB-ARRAY OF A ONE-DIMENSIONAL ARRAY
x = np.arange(10)
# print(x) # Uncomment for use

j = x[:4] # Access all elements up to the fourth

k = x[4:] # Access all elements after the fourth

l = x[4:7] # Access middle array

m = x[::2] # Access every other element in the array

n = x[1::2] # Access every other array starting at 1

o = x[::-1] # Access all arrays in reverse

p = x[5::-2] # Access every other other element, in reverse order, from 5


# ACCESSING SUB-ARRAYS OF MULTI-DIMENSIONAL ARRAYS
q = x2[:2, :3] # First two rows, first three elements

r = x2[:3, ::2] # All rows, every other column

s = x2[::-1, ::-1] # All arrays reversed

t = x2[:, 0] # Access first column

u = x2[0] # Access first column. equivalent to x2[0, :]

# CREATE COPY OF ARRAY
# Editing a sub-array edits the original array
x2_sub_copy = x2[:2, :2].copy()


# RESHAPING ARRAYS
x4 = np.array([1, 2, 3]) # Create single array

x4_row = x4.reshape((1, 3)) # Reshape column into row

x4_row_newaxis = x4[np.newaxis, :] # Create row using 'newaxis' routine

x4_column = x4.reshape((3, 1)) # Reshape row into column

x4_column_newaxis = x4[:, np.newaxis] # Create column using 'newaxis' routine


# ARRAY CONCATENATION
x5 = np.array([1, 2, 3])
y = np.array([3, 2, 1])
z = [99, 99, 99]

v = np.concatenate([x5, y, z]) # Concatenate arrays

# Create grid
grid = np.array([[1, 2, 3],
                 [4, 5, 6]])

w = np.concatenate([grid, grid]) # Concatenate across first axis

x = np.concatenate([grid, grid], axis=1) # Concatenate across second axis

x6 = np.array([1, 2, 3])
grid = np.array([[9, 8, 7],
                 [6, 5, 4]])

y = np.vstack([x6, grid]) # Stack the arrays vertically

x7 = np.array([[99],
              [99]])

z2 = np.hstack([x7, grid])


# SPLITTING ARRAYS
x = [1, 2, 3, 99, 99, 3, 2, 1] # Create an array

a1, a2, a3 = np.split(x, [3, 5]) # Split at index 3 and 5 & assign to a1, a2 & a3

grid = np.arange(16).reshape((4, 4)) # create 4x4 array

upper, lower = np.vsplit(grid, [2]) # Split by second row

left, right = np.hsplit(grid, [2]) # Split by second column



















