import numpy as np 

np.__version__

# make list from 0-9
L = list(range(10))
L
type(L[0])

# Use list comprehension to cast ints as strings
L2 = [str(c) for c in L]
L2
type(L2[0])

# Creating Arrays from Python Lists
# integer array:
np.array([1,4,2,5,2])

# np.arrays can only contain one type of info, so if there is
# a mix of types it will try to typecast them into a single one
np.array([3.14, 2, 3, 4]) # will result in all being floats

# you can also be quite explicit
np.array([1, 2, 3, 4], dtype='float32')

# finally, unlike python lists, numpy arrays can explicitly be multidimensional:
# nested lists results in multidimensional arrays
np.array([range(i,i+3) for i in [2,4,6]]) # nb the inner lists, are treated as rows of the resulting two_dimesnional array

# Creating Arrays from scratch
## for larger arrays it is more efficient to create arrays from scratch using routines built into Numpy

# Create a length-10 integer array filled with zeros
np.zeros(10, dtype=int)

# Create a 3x5 floating-point array filled with ones
np.ones((3, 5), dtype=float)

# Create a 3x5 array filled with 3.14
np.full((3, 5), 3.14)

# Create an array filled with a linear sequence
# Starting at 0, ending at 20, stepping by 2
# (this is similar to the built-in range() function)
np.arange(0, 20, 2)

# Create an array of five values evenly spaced between 0 and 1
np.linspace(0, 1, 5)

# Create a 3x3 array of uniformly distributed
# random values between 0 and 1
np.random.random((3, 3))

# Create a 3x3 array of normally distributed random values
# with mean 0 and standard deviation 1
np.random.normal(0, 1, (3, 3))

# Create a 3x3 array of random integers in the interval [0, 10)
np.random.randint(0, 10, (3, 3))

# Create a 3x3 identity matrix
np.eye(3)

# Create an uninitialized array of three integers
# The values will be whatever happens to already exist at that memory location
np.empty(3)

# The standard NumPy data types are listed in the following table. 
# Note that when constructing an array, they can be specified using a string:
np.zeros(10, dtype='int16')
# or using the associated NumPy object:
np.zeros(10, dtype=np.int16)