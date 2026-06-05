from matplotlib import pyplot as plt
from matplotlib import style

days = [1, 2, 3, 4, 5]
temperature = [30, 32, 28, 31, 29]
style.use('ggplot')

plt.plot(days, temperature, marker='o', linestyle='--', color='r',linewidth=2, markersize=8)
plt.axis([0, 6, 25, 35])  # Set x-axis from 0 to 6 and y-axis from 25 to 35
plt.title('Temperature over 5 Days', fontdict={'fontsize': 16, 'fontweight': 'bold', 'color': 'blue'})
plt.xlabel('Days')
plt.ylabel('Temperature (°C)')
plt.legend(['Temperature'], loc='upper left', fontsize=12, frameon=True, shadow=True, borderpad=1)
plt.show()
