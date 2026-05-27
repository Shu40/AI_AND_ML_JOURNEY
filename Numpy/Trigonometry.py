import numpy as np
import matplotlib.pyplot as plt

print(np.sin(0)) #sin 0 degree
print(np.cos(0)) #cos 0 degree
print(np.tan(0)) #tan 0 degree


x_sin = np.arange(0, np.pi*2, 0.1) #0 to 2pi with step of 0.1
print(np.sin(x_sin)) #sin values for 0 to 2pi

y_sin = np.sin(x_sin)
print(y_sin)

plt.plot(x_sin, y_sin)
plt.xlabel('x')
plt.ylabel('sin(x)')
plt.title('Sine Function')
plt.show()