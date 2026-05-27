import numpy as np
import random


random=np.random.random(1)
print(random)

random=np.random.randint(1, 10, 5) #start, stop, number of values
print(random)

random=np.random.rand(5) #number of values
print(random)

random=np.random.randn(5) #number of values
print(random)

random = np.random.randint(1, 10, (2, 3)) #start, stop, shape
print(random)
