import matplotlib.pyplot as plt

classes = ['Python', 'Java', 'C++', 'Ruby', 'JavaScript']
values = [85, 70, 60, 50, 90]
explode = (0.1, 0, 0, 0, 0)  # explode the first slice

plt.pie(values, labels=classes, autopct='%1.1f%%', startangle=140 ,explode=explode, shadow=True)
plt.title('Popularity of Programming Languages')
plt.show()
