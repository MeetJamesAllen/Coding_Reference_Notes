import numpy as np
import pandas as pd


data1 = pd.Series([0.25, 0.5, 0.75, 1.0],
              index=['a', 'b', 'c', 'd']) # Create a dataframe

# ACCESSING ELEMENTS
b = data1['c'] # Select element

# Search index for value
c = 'a' in data1
d = 0.25 in data1

e = data1.keys() # Access the index

f = data1.items() # Access the values


