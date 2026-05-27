#ravel function is used to flatten a multi-dimensional array into a one-dimensional array.
import numpy as np
arr_2d=np.array([[1, 2, 3], [4, 5, 6]])
arr_1d=arr_2d.ravel()
print(arr_1d)