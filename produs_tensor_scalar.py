#!/usr/local/bin/python3

from tensor import *

def produs_tensor_scalar(t, scalar):
	"""
	d = adincimea tenzorului
	y = numarul de linii
	x = munarul de coloane
	"""
	# print("noroc")
	# print(t2)
	# print("noroc")
	tensor = Tensor(t.d, t.y, t.x)
	def produs_coloana(d, y, scalar):
		return [ t.tensor[d][y][i] * scalar for i in range(t.x) ]

	def produs_linii(d, scalar):
		return [ produs_coloana(d, y, scalar) for y in range(t.y) ]

	tensor.tensor = [ produs_linii(d, scalar) for d in range(t.d) ]
	return tensor