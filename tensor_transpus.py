#!/usr/local/bin/python3

from tensor import *

def tensor_transpus(t):
	"""
	d = adincimea tenzorului
	y = numarul de linii
	x = munarul de coloane
	"""
	tensor1 = t.tensor
	x = t.x
	y = t.y

	def coloana(d, j):
		print("numarul coloane matrix =", j)
		return [ tensor1[d][i][j] for i in range(y) ]

	def linie(d):
		print("linii total =", x)
		return [ coloana(d, i) for i in range(x) ]

	tensor = Tensor(t.d, t.x, t.y)
	tensor.tensor = [ linie(i) for i in range(t.d) ]
	return tensor