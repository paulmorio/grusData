# Numpy Array Basics

import numpy as np
np.random.seed(0)  # seed for reproducibility

x1 = np.random.randint(10, size=6)  # One-dimensional array
x2 = np.random.randint(10, size=(3, 4))  # Two-dimensional array
x3 = np.random.randint(10, size=(3, 4, 5))  # Three-dimensional array

print("x3 ndim: ", x3.ndim)
print("x3 shape:", x3.shape)
print("x3 size: ", x3.size)
print("dtype:", x3.dtype)
print("itemsize:", x3.itemsize, "bytes")
print("nbytes:", x3.nbytes, "bytes")
# In general, we expect that nbytes is equal to itemsize times size.

# Reshaping of Arrays
# Another useful type of operation is reshaping of arrays. The most flexible way of doing this is with the reshape method. For example, 
# if you want to put the numbers 1 through 9 in a 3×3 grid, you can do the following:
grid = np.arange(1, 10).reshape((3, 3))
print(grid)

# Another common reshaping pattern is the conversion of a one-dimensional array into a two-dimensional row or column matrix. 
# This can be done with the reshape method, 
x = np.array([1, 2, 3])
# row vector via reshape
x.reshape((1, 3))
# row vector via newaxis
x[np.newaxis, :]

