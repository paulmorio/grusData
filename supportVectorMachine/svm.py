from base.base import BaseEstimator
from supportVectorMachine.kernels import Linear
import numpy as np
import logging

np.random.seed(9999)

"""
References: Mateja Jamnik Course Machine Learning
"""

class SVM(BaseEstimator):
	def __init__(self, C = 1.0, kernel = None, tol = 1e-3, max_iter = 100):
		"""Support vector machines implementation

		Parameters
		----------
	    C : float, default 1.0
	    kernel : Kernel object
	    tol : float , default 1e-3
	    max_iter : int, default 100
	    """
    	self.C = C
    	self.kernel = kernel
    	self.max_iter = max_iter

    	if kernel is None:
    		self.kernel = Linear()
    	else:
    		self.kernel = kernel

    	self.b = 0
    	self.alpha = None
    	self.K = None

    def clip(self, alpha, H, L):
    	if alpha > H:
    		alpha  = H
    	if alpha < L:
    		alpha = L
    	return alpha

    def fit(self, X, y = None):
    	self._setup_input(X,y)
    	self.K = np.zeros((self.n_samples, self.n_samples))
    	for i in range(self.n_samples):
    		self.K[:,i] = self.kernel(self.X, self.X[i, :])


    def _error(self,i):
    	"""Error for single example"""
    	return self._predict_row(self.X[i]) - self.y[i]

    def _find_bounds(self,i,j):
    	"""Find L and H such that L <= alpha <= H.
    	Also, alpha must satisfy the constraint 0 <= alpha <= C.
    	"""
    	if self.y[i] != self.y[j]:
            L = max(0, self.alpha[j] - self.alpha[i])
            H = min(self.C, self.C - self.alpha[i] + self.alpha[j])
        else:
            L = max(0, self.alpha[i] + self.alpha[j] - self.C)
            H = min(self.C, self.alpha[i] + self.alpha[j])
        return L, H

    def random_index(self, z):
    	i = z
    	while i == z:
    		i = np.random.randint(0, self.n_samples - 1)
    	return i