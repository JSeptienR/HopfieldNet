class HopfieldNet:
	def __init__(self, size):
		self.size = size
		self.weights = []

	def initialize(self):
		""" Initialize Network """
		size = self.size
		self.weights = [[0 for _ in range(size)] for _ in range(size)]

	def update_weights(self, new_weights):
		""" Update Network Weights """
		for i in range(self.size):
			for j in range(self.size):
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
			for i in range(self.size):
				y_in = 0
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
	hop_net = HopfieldNet(3)
	hop_net.initialize()
	
	pattern = [1, 1, -1]
	pattern2 = [-1, -1, 1]
	hop_net.train(pattern)
	hop_net.train(pattern2)
	
	t1 = [1, 0, -1]
	t2 = [-1, 0, 1]
	result = hop_net.test(t1)
	result2 = hop_net.test(t2)
	print(hop_net.weights)
	print(result)
	print(result2)
	
