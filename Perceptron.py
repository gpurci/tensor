#!/usr/local/bin/python3

from tensor import *

class Perceptron:
	"""
	Noroc
	"""
	def __init__(self, harta):
		self.harta = harta
		self.greutate = [ Tensor(1, self.harta[i - 1], self.harta[i], ['random', 'uniform'], [0, 5]) for i in range(1, len(self.harta)) ]
		self.plaseholder = 0
		self.bias = [ Tensor(1, 1, self.harta[i], ['random', 'uniform'], [0, 5]) for i in range(1, len(self.harta)) ]
		self.input = []
		self.ideal = []
		self.f = 0


	def __str__(self):
		h = len(self.harta) - 1
		returnStr = "Perceptron\n harta: " + str(self.harta)
		returnStr += "\n bias: " + [ print(self.bias[i]) for i in range(h)]

		# "\ngreutate: " + str(self.greutate) + "\n plaseholder: " + str(self.plaseholder)
		return returnStr