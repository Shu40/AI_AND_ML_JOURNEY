from matplotlib import pyplot as plt
import numpy as np

days = [1, 2, 3, 4, 5]
temperature = [30, 32, 28, 31, 29]
plt.plot(days, temperature, marker='o', linestyle='-', color='b')
plt.axis([0, 6, 25, 35])  # Set x-axis from 0 to 6 and y-axis from 25 to 35
plt.title('Temperature over 5 Days')
plt.xlabel('Days')
plt.ylabel('Temperature (°C)')
plt.show()
