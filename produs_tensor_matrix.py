#!/usr/local/bin/python3

from tensor import *

def produs_tensor(t1, t2):
	"""
	d = adincimea tenzorului
	y = numarul de linii
	x = munarul de coloane
	"""
	# print("noroc")
	# print(t2)
	# print("noroc")

	if t1.d != t2.d or t1.x != t2.y:
		return 
	x = t2.x
	y = t1.y
	tensor1 = t1.tensor
	tensor2 = t2.tensor
	def produs_total(d, y1, y2):
		produs = 0
		for i in range(y):
			produs += tensor1[d][i][y1] * tensor2[d][y2][i]
		return produs


	def produs_coloana(d, y):
		return [ produs_total(d, y1, y2) for i in range(x) ]

	def produs_linii(d):
		return [ produs_coloana(d, i) for i in range(y) ]
	tensor = Tensor(2, 3, 3)
	tensor.tensor = [ produs_linii(i) for i in range(t1.d) ]
	return tensor