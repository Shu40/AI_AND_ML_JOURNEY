import matplotlib.pyplot as plt

import numpy as np
from matplotlib import style

classes = ['Python', 'Java', 'C++', 'Ruby', 'JavaScript']
values = [85, 70, 60, 50, 90]
value2 = [80, 75, 65, 55, 95]
value3 = [90, 80, 70, 60, 100]

style.use('ggplot')

plt.bar(classes,[value2, value3, values], color=['green','red','blue'], label='2021', align = 'center', alpha=0.5,linewidth=[2,2,2], edgecolor='black' )

plt.xlabel('Programming Languages')
plt.ylabel('Popularity')
plt.title('Popularity of Programming Languages')
plt.legend()
plt.show()
