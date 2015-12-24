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

import random

def step(v, direction, step_size):
	"""
	move step-size in the direction from v
	"""
	return [v_i + step_size * direction_i
			for v_i, direction_i in zip(v,direction)]

def sum_of_squares_gradient(v):
	return [2 * v_i for v_i in v]

# pick a random starting point
v = [random.randint(-10,10) for i in range(3)]

tolerance = 0.0000001

while True: 
	gradient = sum_of_squares_gradient(v)
	next_v = step(v, gradient, -0.01)

	if distance(next_v, v) < tolerance:
		break

	v = next_v

# Sometimes we want to use different step sizes and there are diferent approaches

"""
Althout the rationale for moving against the gradient is clear, how far to move is not.
Indeed, choosing the right step size is more of an art than a science. Popular options
include:

- Using a fixed step size
- Gradually shrinking the step size over time
- At each step, choosing the size that minimizes the value of the objective function, (error function)

The last sounds optimal but is, in practice, a costly computation. We can approximate it by trying a 
variety of step sizes and choosing the one that results in the smallest value of the objective function
"""

# step_sizes = [100, 10, 1 , 0.1, 0.01, 0.001, 0.0001, 0.00001]

def safe(f):
	"""
	return a new function thats the same as f, except that
	that it outputs infinity whenever f produces an error
	"""
	def safe_f(*args, **kwargs):
		try:
			return f(*args, **kwargs)
		except:
			return float('inf')
		return safe_f

def minimize_batch(target_fn, gradient_fn, theta_0, tolerance = 0.000001):
	"""
	use gradient descent to find theta that minimizes target function
	"""
	step_sizes = [100, 10, 1 , 0.1, 0.01, 0.001, 0.0001, 0.00001]

	theta = theta_0
	target_fn = safe(target_fn)
	value = target_fn(theta)		# the value were minimizing

	while True:
		gradient = gradient_fn(theta)
		next_thetas = [step(theta, gradient, -step_size) for step_size in step_sizes]

		#choose the one that minimuzes the error function (objective function)
		next_theta = min(next_thetas, key=target_fn)
		next_value  = target_fn(next_theta)

		#stop if we're "converging" or coming a steady state
		if abs(value - next_value) < tolerance:
			return theta
		else:
			theate, value = next_theta, next_value

# We call is minimize batch because for each gradient step it looks at the entire data set.
# This is because target_fn returns the error on the whole data set.

# Sometimes we want to maximise a function instead, to do so we only have to negate the target functions
# and find the minimum of that

def negate(f):
	"""
	the same when f returns a list of numbers
	"""
	return lambda *args, **kwargs: -f(*args, **kwargs)

def negate_all(f):
	"""
	the same when f returns a list of numbers
	"""
	return lambda *args, **kwargs: [-y for y in f(*args, **kwargs)]

def maximize_batch(target_fn, gradient_fn, theta_0, tolerance=0.000001):
	return minimize_batch(negate(target_fn),
						  negate_all(gradient_fn),
						  theta_0, 
						  tolerance)



