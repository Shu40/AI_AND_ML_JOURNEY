# reshape function is used to change the shape of an array without changing its data. It takes a tuple as an argument which specifies the new shape of the array. The total number of elements in the new shape must be the same as the total number of elements in the original array.
import numpy as np

arr_1d=np.array([1, 2, 3, 4, 5, 6])
arr_2d=arr_1d.reshape(2, 3) #new shape (row, column)
print(arr_2d)