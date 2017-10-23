import numpy as np

# old way to do it, make 3 different arrays of data. The downside of this is that it doesnt necessarily 
# tell us that these 3 are related data sets. Though then again its quite simple if you're not an idiot
name = ["Alice", "Bob", "Cathy", "Doug"]
age = [25, 45, 37, 19]
weight = [55.0, 85.5, 68.0, 61.5]

# Now we can use a compound data type for structured arrays, creating
# a structured array with zeros of the 10character, 4byte integer, and 8byte float
data = np.zeros(4, dtype={'names':('name', 'age', 'weight'),
						  'formats':('U10', 'i4', 'f8')})
print(data.dtype)

# now we can fill up this structured array. Hey this is R almost
data['name'] = name
data['age'] = age
data['weight'] = weight
print(data)

# this is cool as it is now arranged as a np object and arragend in one contigious block of memory
# moreover all this stuff is nw accessible by name/index
# all names eg
data['name']

# This allows us to to cool filtering 
# get names where age is under 30
data[data['age'] < 30]['name']

# Pandas basically greatly expands on the functionality and usefulness of these structures
# with proper input/output control and stuff

## Super advanced compound types
# it is possile to define even more advanced compound types. For example you fcan create a type 
# where each element contains an array or matrix of values
# here will create a data type with a mat component consisting of a 3x3 floating point matrix

# wow
tp = np.dtype([('id', 'i8'), ('mat', 'f8', (3,3))])
X = np.zeros(1,dtype = tp)
print(X[0])
print(X['mat'][0])
