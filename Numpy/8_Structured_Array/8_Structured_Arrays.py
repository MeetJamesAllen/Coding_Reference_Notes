import numpy as np

# Create lists to be used in structured array
name = ['Alice', 'Bob', 'Cathy', 'Doug']
age = ['25', '45', '37', '19']
weight = [55.0, 85.5, 68.0, 61.5]



# Create empty container array that includes data type specifications
data  = np.zeros(4, dtype={'names':('name', 'age', 'weight'), 
                           'formats':('U10', 'i4', 'f8')})

data['name'] = name
data['age'] = age
data['weight'] = weight

# Retrieve data

all_names = data['name'] # Retrieve all names
first_row = data[0] # Retrieve first row
final_name = data[-1]['name'] # Retrieve final name in list
age_range = data[data['age']< 30]['name'] # Retrieve name within age range

