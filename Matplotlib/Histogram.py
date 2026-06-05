import matplotlib.pyplot as plt
import numpy as np
import random
import matplotlib.style as style

ML_Student_age = np.random.randint(18, 30, 100)  # Generate random ages between 18 and 30 for 100 students
AI_Student_age = np.random.randint(15, 45, 100)  # Generate random ages between 18 and 30 for 100 students  
plt.style.use('ggplot')  # Use ggplot style for better aesthetics
plt.hist([ML_Student_age, AI_Student_age], bins=10, edgecolor='black', color=['skyblue', 'lightcoral'], label=['Age of ML Students', 'Age of AI Students'])
plt.title('Age Distribution of ML and AI Students')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.grid(axis='y', alpha=0.75)
plt.legend()
plt.show()