import numpy as np  
ch_name = "Chirag Shah"
print(ch_name)
str1 = "Hello World"
print(str1)

add_str = np.char.add(ch_name, str1) #concatenation of two strings
print(add_str)
mult_str = np.char.multiply(ch_name, 3) #repetition of string
print(mult_str)