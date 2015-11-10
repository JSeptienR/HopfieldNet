import random

class HopfieldNet:
	def __init__(self, size, weights=[]):
		self.size = size
		self.weights = weights

	def initialize(self):
		""" Initialize Network """
		size = self.size
		self.weights = [[0 for _ in range(size)] for _ in range(size)]

	def update_weights(self, new_weights):
		""" Update Network Weights """
		for i in range(self.size):
			for j in range(self.size):
				if i == j:
					self.weights[i][j] = 0
				else:
					self.weights[i][j] += new_weights[i][j]

	def train(self, input_vector):
		""" Train Network """
		weights = [[s1*s2 for s1 in input_vector] for s2 in input_vector]
		self.update_weights(weights)

	def test(self, input_vector):
		"""Test Network """
		y = input_vector[:]
		converged = False
		while not converged:
			y_old = y[:]
			random_sequence = list(range(self.size))
			random.shuffle(random_sequence)
			for i in random_sequence:
				y_in = input_vector[i]
				for j in range(self.size):
					y_in += self.weights[i][j] * input_vector[j]
				y[i] = activation(y_in)
			if y_old == y:
				converged = True
		return y


def activation(x):
	if x >= 0:
		return 1
	else:
		return -1


if __name__ == '__main__':
	print('Hopfield Network')
