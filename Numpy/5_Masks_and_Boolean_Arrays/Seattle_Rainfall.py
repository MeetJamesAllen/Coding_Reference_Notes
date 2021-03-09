import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn; seaborn.set()

rainfall = pd.read_csv('Seattle2014.csv')
inches = rainfall["PRCP"] / 254


print("Number of days without rain:    ", np.sum(inches == 0))
print("Number of days with rain:       ", np.sum(inches != 0))
print("Days with more than 0.5 inches: ", np.sum(inches > 0.5))
print("Rainy days with < 0.1 inches:   ", np.sum((inches > 0) & (inches < 0.2)))


# Construct a mask of all rainy days
rainy = inches > 0

# Contruct a mask of all summer days
summer = (np.arange(365) - 172 < 90) & (np.arange(365) - 172 > 0)


# Compare masks
print("Median precip on rainy days in 2014 (inches):    ",
      np.median(inches[rainy]))
      
print("Median precip on summer days in 2014 (inches):   ",
      np.median(inches[summer]))

print("Maximum precip on summer days in 2014 (inches::   ",
      np.max(inches[summer]))

print("Median precip on non-summer rainy days (inches):  ",
      np.median(inches[rainy & summer]))