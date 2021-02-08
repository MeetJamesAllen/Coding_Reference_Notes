import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn; seaborn.set()

rng = np.random.RandomState(0)
x = rng.randint(10, size= (3, 4))

print(x)

# Count values less than 6
print("Non-zero values: ", np.count_nonzero(x)) 

# Count values less than 6
print("Less than 6: ", np.count_nonzero(x < 6))

 # Sum of values less than 6(False = 0, True = 1)
print("Less than 6 (Using sum): ", np.sum(x < 6))

# Count values less than 6 in each row
print("Less than 6 in each row: ", np.sum(x < 6, axis=1)) 

# Asks "Are there any values that meet criteria"
print("There is at least one value greater than 8: ", np.any(x > 8))

# Asks "Do all values meet criteria?"
print("All values are less than 10: ", np.all(x < 10))

# Asks "Are all values in each row less than eight?"
print("Are there any values in each row less than eight?", 
      np.all(x < 8, axis = 1))

# Asks "How many values meet the criteria
print("Amount of values between 2 and 6: ", np.sum((x > 2) & (x < 6)))

# Show boolean mask for all values less than 5
print(x < 5)

# Show all values less than 5
print(x[x < 5])