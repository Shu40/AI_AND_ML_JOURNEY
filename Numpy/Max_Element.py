import numpy as np
arr1 = np.arange(1,10)
max_element = np.max(arr1)
print(max_element)

argmax_element = np.argmax(arr1)
print(argmax_element)

#every row max element
Rowmax_element = np.max(arr1.reshape(3,3), axis=1)
print(Rowmax_element)

#min element
min_element = np.min(arr1)
print(min_element)

#min row element
Rowmin_element = np.min(arr1.reshape(3,3), axis=1)  
print(Rowmin_element)

#sum element

sum = np.sum(arr1)
print(sum)
