import matplotlib.pyplot as plt

# Create a simple plot
plt.pie([10, 20, 30])
plt.title("Simple Pie Chart")
plt.savefig("pie_chart.png", dpi=1000, quality=100, facecolor='green')  # Save the figure as a PNG file
plt.show()  # Display the plot