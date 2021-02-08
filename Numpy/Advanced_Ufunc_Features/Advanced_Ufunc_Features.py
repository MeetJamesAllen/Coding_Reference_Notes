import numpy as np

# 1 SPECIFYING OUTPUTS
print('1 SPECIFYING OUTPUTS')

x = np.arange(100) # Create an array with values from 0 - 4
y = np.empty() # Creates an array of a given shape containing arbitrary values
np.multiply(x, 10, out=y) # Performs multiplication and outputs to y


