#!/usr/local/bin/python3

from produs import *

class Tensor:
	"""
	d = adincimea tenzorului
	y = numarul de linii
	x = munarul de coloane
	dot = produsul dintre doi tensori prin metoda dot
	"""
	def __init__(self, x = 1, y = 1, d = 1, func = 'random'):
		self.d = d
		self.y = y
		self.x = x
		self.data = 0

	def __str__(self):
		returnStr = "Tensor\n adincime: " + str(self.d) + "\n linii:    " + str(self.y)
		returnStr += "\n coloane:  " + str(self.x)
		returnStr += "\n" + str(self.data)
		return returnStr

	def __mul__(self, t):
	if self.d != t.d or self.x != t.x or self.y != t.y:
		return 
	x = self.x
	y = self.y
	tensor1 = self.data
	tensor2 = t.data
	def coloana(d, y):
		return [ tensor1[d][y][i] * tensor2[d][y][i] for i in range(x) ]

	def linii(d):
		return [ produs_coloana(d, i) for i in range(y) ]

	tensor = Tensor(self.d, y, x)
	tensor.data = [ produs_linii(i) for i in range(t1.d) ]
	return tensor

	def __add__(self, t):



	def generare_1d(x, lst):
	return [ lst[2](lst[0], lst[1]) for i in range(x) ]

	def generare_2d(y, x, lst):
		return [ generare_1d(x, lst) for i in range(y) ]

	def generare_3d(d, y, x, lst):
		return [ generare_2d(y, x, lst) for i in range(d) ]




	def produs_tensor_matrix(t1, t2):
	if t1.d != t2.d or t1.x != t2.y:
		return
	xp = t1.x
	xd = t2.x
	y = t1.y
	tensor1 = t1.tensor
	tensor2 = t2.tensor

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


t1 = Tensor(2, 2, {"func": asdasd})