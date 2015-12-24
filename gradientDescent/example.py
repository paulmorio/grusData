"""
Example function that we want to minimize/maximize
"""

def sum_of_squares(v):
	"""
	Computers the sum of squared elemetns in v
	"""
	return sum(v_i ** 2 for v_i in v)

# Estimating the gradient
def difference_quotient(f, x, h):
	return (f(x+h) - f(x))/h
	# as h approaches 0

# now for some basic understanding of doing calculus
def square(x): 
	return x*x 

def derivative(x):
	return 2*x

# Example showing that out estimation techniques arent too bad
derivate_estimate = partial(difference_quotient, square, h=0.00001)

#plot to visually show similarity
import matplotlib.pyplot as plotx = range(-10,10)
plt.title("Actual Derivaties vs Estimates")
plt.plot(x, map(derivative,x),'rx', label="Actual")
plt.plot(x, map(derivate_estimate, x), 'b+', label='Estimates')
plt.legend(loc=9)
plt.show()

# when f is a function of many variables, it has multiple partial derivatives, each indicating how f
# changes when we make small changes 

def partial_difference_quotient(f, v, i, h):
	"""
	Compute the ith partial difference quotient of f at v
	"""
	w = [v_j + (h if j== i else 0) 		# add h to just the ith element of h
			for j, v_j in enumerate(v)] 

	return (f(w) - f(v)) / h 

# we can estimate the gradient the same way:

def estimate_gradient(f, v, h=0.00001):
	return [partial_difference_quotient(f, v, i, h)
			for i, _ in enumerate(v)]

