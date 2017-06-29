from numpy import exp, array, random, dot

class NeuralNetwork():
	def __init__(self):
		# seed the randomg number generator
		random.seed(1)

		# we model a single neuron with 3 input connections and 1 output connections
		# we assign random weights to a 3x1 matrix, with values in the range of -1 to 1
		# and mean 0
		self.synaptic_weights = 2*random.random((3,1)) - 1

	# this is a side note but recall that in python the underscores before and after are kinda
	# convention thing to make sure conflicts dont appear with other things called init,
	# protip dont do it
	# single underscore tries to make functions private
	# double underscores are interesting as they mangle the names and prepend _className
	# to the method.

	# The sigmoid function, which describes an S shaped curve.
	# we pass the weighted sum of the inputs thorugh this function to
	# normalise them between 0 and 1
	def __sigmoid(self, x):
		return 1/(1+exp(-x))

	# The derivative of the sigmoid function
	# this is the gradient of the sigmoid curve.
	# It indicates how confident we are about the existing weight.
	def __sigmoid_derivative(self, x):
		return x * (1 - x)

	# We train the neural network through a process of trial and error.
	# Adjusting the synaptic weights each time
	def train(self, training_set_inputs, training_set_outputs, number_of_training_iterations):
		for iteration in xrange(number_of_training_iterations):
			# pass the training set through our neural network (a single neuron here)
			output = self.thing(training_set_inputs)

			# calculate the error (difference between the desired output and the prediceted output)
			error = training_set_outputs - output

