import numpy as np
from numpy import matrix 
from numpy import convolve 
from numpy import roll

def conv_mat(h, x):
	m = len(h)
	n = len(x)
	row = np.zeros(m+n-1)
	row[0:m] = h[::-1]
	H = np.zeros([m+n-1, n])

	for i in range(m+n-1):
		H[i,:] = row[m-1:m+n-1]
		row = roll(row,1)

	y = np.dot(H,x)
	return (H, y)

# h = [1, 2, 15]
# x = [7, 3, 9, 2, 3, 5]

# print convolve(h,x)
# print conv_mat(h,x)
