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

# Array concatenation
## One dimesnsion
x = np.array([1, 2, 3])
y = np.array([3, 2, 1])
np.concatenate([x, y]) # makes one longer array

z = [99, 99, 99]
print(np.concatenate([x, y, z])) # concatenate more than two arrays at once

# two dimension
grid = np.array([[1, 2, 3],
                 [4, 5, 6]])

# concatenate along the first axis
np.concatenate([grid, grid])

# $output
# array([[1, 2, 3],
#        [4, 5, 6],
#        [1, 2, 3],
#        [4, 5, 6]])

# concatenate along the second axis (zero-indexed)
np.concatenate([grid, grid], axis=1)
# $output
# array([[1, 2, 3, 1, 2, 3],
#        [4, 5, 6, 4, 5, 6]])

# it might be eaiser to understand np.vstack and np.hstack functions
x = np.array([1, 2, 3])
grid = np.array([[9, 8, 7],
                 [6, 5, 4]])

# vertically stack the arrays
np.vstack([x, grid])
# ## output
# array([[1, 2, 3],
#        [9, 8, 7],
#        [6, 5, 4]])

# horizontally stack the arrays
y = np.array([[99],
              [99]])
np.hstack([grid, y])

# # output
# array([[ 9,  8,  7, 99],
#        [ 6,  5,  4, 99]])

# np.dstack will stack arrays along the third axis, there are obviously more possible dimensions
# but it really starts to make little sense at this point.

# Splitting
x = [1, 2, 3, 99, 99, 3, 2, 1]
x1, x2, x3 = np.split(x, [3, 5])
print(x1, x2, x3)

grid = np.arange(16).reshape((4, 4))
grid

# vertical split
upper, lower = np.vsplit(grid, [2])
print(upper)
print(lower)

# horizontal split
left, right = np.hsplit(grid, [2])
print(left)
print(right)