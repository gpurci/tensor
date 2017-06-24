#!/usr/local/bin/python3

from produs import *

class Tensor:
	"""
	d = adincimea tenzorului
	y = numarul de linii
	x = munarul de coloane
	"""
	def __init__(self, d, y, x):
		self.d = d
		self.y = y
		self.x = x
		self.tensor = 0

	def __str__(self):
		returnStr = "Tensor\n adincime: " + str(self.d) + "\n linii:    " + str(self.y)
		returnStr += "\n coloane:  " + str(self.x)
		returnStr += "\n" + str(self.tensor)
		return returnStr
