#transpose function is used to change the orientation of a multi-dimensional array. It takes no arguments and returns a new array with the same data but with the dimensions reversed.
import numpy as np
arr_2d=np.array([[1, 2, 3], [4, 5, 6]])
arr_transpose=arr_2d.transpose()
print(arr_transpose)