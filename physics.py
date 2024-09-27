import numpy as np
import pandas as pd
import matplotlib.pyplot as plt  # Correcting the import for pyplot

# Load the CSV file
df = pd.read_csv("Physics.csv")

# Extracting the last few rows of the second and third columns
x = df.tail().iloc[:, 10]  # Assuming this is the categorical data for the x-axis
y = df.tail().iloc[:, 20]  # Assuming this is the numerical data for the y-axis

# Print x and y to verify
print(x, y)

# Create a bar chart
plt.bar(x, y)

# Add labels and title for better visualization
plt.xlabel('X-axis Label')  # Replace with your actual label
plt.ylabel('Y-axis Label')  # Replace with your actual label
plt.title('Bar Chart Title')  # Replace with your actual title

# Show the plot
plt.show()
