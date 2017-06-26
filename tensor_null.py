#!/usr/local/bin/python3

from tensor import *

def tensor_null(d, y, x):
	"""
	returneaza tensor null
	d = adincimea tenzorului
	y = numarul de linii
	x = munarul de coloane
	"""
	def coloana():
		# print("numarul coloane matrix =", x)
		return [ 0 for i in range(x) ]

	def linie():
		# print("linii total =", y)
		return [ coloana() for i in range(y) ]

	tensor = Tensor(d, x, y)
	tensor.tensor = [ linie() for i in range(d) ]
	return tensor