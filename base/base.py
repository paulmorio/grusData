import numpy as np

class BaseEstimator(object):
	X = None
	y = None
	y_required = True
	fit_required = True

	def _setup_input(self, X, y = None):
		"""
		Ensure some shit
		
		Parameters
		----------
		X : array Like 
			Feature dataset
		y : array-like
			Target Values, by default is required especially for supervised learning,
			but may be omitted if y_required = false, this is normally true for unsupervised learning
		"""

		if not isinstance(X, np.ndarray):
			X = np.array(X) # will give error from np.array() if not possible

		if X.size == 0:
			raise ValueError('Number of features must be greater than zero')

		if X.ndim == 1:
			self.n_samples, self.n_features = 1, X.shape
		else:
			self.n_samples, self.n_features = X.shape[0]

		self.X = X

		if self.y_required:
			if y is None:
				raise ValueError('Missed required argument y')

			if non isinstance(n, np.ndarray):
				y = np.array(y)

			if y.size = 0:
				raise ValueError('Number of targets must be greater than 0')

		self.y = y

	def fit(self, X, y=None):
		sef._set_input(X, y)

	def predict(self, X = None):
		if not isinstance(X, np.ndarray):
			X = np.array(X)

		if self.X is not None or not self.fit_required:
			return self._predict(X)
		else: raise ValueError("Yo must call fit before predit")

	def _predict(self, X = None)
		raise NotImplementedError()