import matplotlib.pyplot as plt
import matplotlib.image as mpimg

img = mpimg.imread("C:\\Users\\HP\\Desktop\\Python-DataScience-Journey\\Matplotlib\\pie_chart.png")  # Read an image file
print(img)

print(type(img))  # Print the type of the image object
print(img.shape)  # Print the shape of the image (height, width, color channels
print(img.ndim)  # Print the number of dimensions of the image
print(img.dtype)  # Print the data type of the image array

single_channel = img[:, :, 1]  # Extract the red channel (or any single channel)
plt.figure(figsize=(10, 10))  # Set the figure size
plt.axis('off')  # Hide the axes
plt.imshow(single_channel, cmap = "gray")  # Show the single channel image
plt.colorbar()  # Add a colorbar to the image
plt.show()  # Show the plot with the image