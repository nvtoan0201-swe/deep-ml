import math

def sigmoid(z: float) -> float:
	#Your code here
	if z >= 0:
		z_exp = math.exp(-z)
		return 1 / (1 + z_exp)
	else:
		z_exp = math.exp(z)
		return z_exp / (1 + z_exp)