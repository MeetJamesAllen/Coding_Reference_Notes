import numpy as np
import pandas as pd

# CREATING AND ACCESSING SERIES OBJECTS
a = pd.Series([0.25, 0.5, 0.75, 1.0]) # Create a series

b = a.values # Access the values of the series

c = a.index # Show the index of the series

d = a[1] # Access second element of series

e = a[1:3] # Access second to third index of series


# CREATING AN INDEX
f = pd.Series([0.5, 1.0, 1.5, 2.0], index = ['a', 'b', 'c', 'd']) # Create a series with a specific index

g = f['b']



# USING SPECIALIZED DICTIONARIES
h = {'California': 3833251,
     'Texas': 26448193,
     'New York': 19651127,
     'Florida': 19552860,
     'Illinois': 12882135} # Create dictionary 

i = pd.Series(h) # Create a series from dictionary. Defaulting to index drawn for sorted keys.

j = i['Texas':'Florida'] # Access certain elements

# Population series only with specific keys of a dictionary
k = pd.Series({2:'a', 1:'b', 3:'c'}, index=[3, 2])



# DATAFRAMES
# Create DataFrame series from dictionary
l = {'California': 423967, 'Texas': 695662, 'New York': 141297,
      'Florida': 170312, 'Illinois': 149995} # Create dictionary
m = pd.Series(l) # Convert to a series with the key as the index by default

n = pd.DataFrame({'Area': l, 'Population': h}) # Bring the two series together to form the DataFrame

o = n.index # Access the index of the DataFrame

p = n.columns # Access the columns attriubute (an index holding the column labels)

q = n['Area'] # Access values


# Create dataframe from a list of dictionaries
r = [{'a': i, 'b': 2 * i}
     for i in range (3)]
s = pd.DataFrame(r)

# DataFrame with missing values
t = pd.DataFrame([{'a':1, 'b':2}, {'b': 3, 'c': 4}])

# Construction from a numpy array
u = pd.DataFrame(np.random.rand(3, 2),
                 columns=['foo', 'bar'],
                 index=['a', 'b', 'c'])



# PANDAS INDEX AS AN OBJECT
v = pd.Index([2, 3, 5, 7, 11]) # Creates an index object

w = v[1] # Access 2nd element of index

x = v[::2] # Access every other element of the index

y = v.size, v.shape, v.ndim, v.dtype # Access attributes of index



# INDEXING AS ORDERED SETS
indA = pd.Index([1, 3, 5, 7, 9])
indB = pd.Index([2, 3, 5, 7, 11])

z = indA & indB # Intersection
aa = indA | indB # Union
ab = indA ^ indB # Symmetric difference














































