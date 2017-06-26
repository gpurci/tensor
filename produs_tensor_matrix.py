#!/usr/local/bin/python3

from tensor import *

def produs_tensor_matrix(t1, t2):
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
	xp = t1.x
	xd = t2.x
	y = t1.y
	tensor1 = t1.tensor
	tensor2 = t2.tensor

	# print("xp", xp)
	# print("xd", xd)
	# print("y", y)

	def produs_total(d, y1, y2):
		# print("num coloane real =", xp)
		# print("y1 =", y1)
		# print("y2 =", y2)
		produs = 0
		for i in range(xp):
			produs += tensor1[d][y1][i] * tensor2[d][i][y2]
		return produs

	def produs_coloana(d, y):
		# print("numarul coloane matrix =", xd)
		return [ produs_total(d, y, i) for i in range(xd) ]

	def produs_linii(d):
		# print("linii total =", y)
		return [ produs_coloana(d, i) for i in range(y) ]

	tensor = Tensor(t1.d, y, xd)
	tensor.tensor = [ produs_linii(i) for i in range(t1.d) ]
	return tensor