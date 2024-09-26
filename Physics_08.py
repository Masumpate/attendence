import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Load the data from the CSV file
df = pd.read_csv("Physics.csv")

# Section 1: Find the student with the highest attendance in the first five rows
# We'll use .head() to get the first five rows, and then find the row with the max attendance
first_five = df.head(5)
highest_attendance_first_five = first_five.loc[first_five.iloc[:, -1].idxmax()]
print("Highest attendance student in first five rows:")
print(highest_attendance_first_five)

# Section 2: Find the student with the highest attendance in the last five rows
# Using .tail() to get the last five rows and find the student with the highest attendance
last_five = df.tail(5)
highest_attendance_last_five = last_five.loc[last_five.iloc[:, -1].idxmax()]
print("\nHighest attendance student in last five rows:")
print(highest_attendance_last_five)

# Section 3: Find the student with the highest attendance between rows 10 and 20
# Here, we'll slice the DataFrame using .iloc to select rows 10 to 20 (which are indices 9 to 19)
rows_10_to_20 = df.iloc[9:20]  # Python index starts at 0, so row 10 is index 9
highest_attendance_10_to_20 = rows_10_to_20.loc[rows_10_to_20.iloc[:, -1].idxmax()]
print("\nHighest attendance student between 10-20 rows:")
print(highest_attendance_10_to_20)

# Section 4: Find the student with the highest attendance overall
# This time we'll check the entire DataFrame to find the highest attendance in the last column
highest_attendance_overall = df.loc[df.iloc[:, -1].idxmax()]
print("\nStudent with highest attendance overall:")
print(highest_attendance_overall)
