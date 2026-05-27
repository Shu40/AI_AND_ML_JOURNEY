import numpy as np
arr1 = np.arange(1, 10).reshape(3, 3)
arr2 = np.arange(1, 10).reshape(3, 3)

arr3 = arr1 + arr2
print(arr3)


print(np.add(arr1,arr2))


arr4 = arr1 - arr2
print(arr4)

print(np.subtract(arr1,arr2))


arr5 = arr1 * arr2
print(arr5)

print(np.multiply(arr1,arr2))

arr6 = arr1 / arr2
print(arr6)

print(np.divide(arr1,arr2))

arr7 = arr1 @ arr2
print(arr7)

print(np.dot(arr1,arr2))