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

step_sizes = [100, 10, 1 , 0.1, 0.01, 0.001, 0.0001, 0.00001]

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