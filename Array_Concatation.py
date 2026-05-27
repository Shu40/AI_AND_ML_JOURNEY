import numpy as np

arr1 = np.arange(1, 10).reshape(3, 3)
print(arr1)
arr2 = np.arange(10, 19).reshape(3, 3)
print(arr2)

#concatenate two arrays
arr_concat = np.concatenate((arr1, arr2), axis=0) #axis=0 for row-wise concatenation, axis=1 for column-wise concatenation
print(arr_concat)   

arr_concat = np.concatenate((arr1, arr2), axis=1) #axis=0 for row-wise concatenation, axis=1 for column-wise concatenation
print(arr_concat)

#hstack and vstack functions
arr_hstack = np.hstack((arr1, arr2)) #hstack for column wise concatenation
print(arr_hstack)   

arr_vstack = np.vstack((arr1, arr2)) #vstack for row wise concatenation
print(arr_vstack)