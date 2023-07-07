import numpy as np

# Create and print a 4x2 matrix with values ranging from 2 to 10
matrix = np.arange(2, 10).reshape(4, 2)
print(matrix)
print()

# Create and print a 8x8 matrix and fill it with a checkerboard pattern
checkerboard = np.array([[0, 1], [1, 0]])
checkerboard = np.tile(checkerboard, (4, 4))
print(checkerboard)
print()

# Get the unique values of a list
# List = [10, 20, 10, 30, 20, 40, 20, 20, 10, 30, 0, 50, 10]
list = [10, 20, 10, 30, 20, 40, 20, 20, 10, 30, 0, 50, 10]
unique_values = np.unique(list)
print(unique_values)
print()

# Get the values greater than 37 in the list
# List = [6, 75, 9, 82, 36, 42, 59, 3, 52, 1, 32, 68, 93, 4, 27, 85, 0, -3, 57]
list = [6, 75, 9, 82, 36, 42, 59, 3, 52, 1, 32, 68, 93, 4, 27, 85, 0, -3, 57]
greater_than_37 = np.where(np.array(list) > 37)
print(np.array(list)[greater_than_37])
print()

# Convert the values of a list of values in Centigrade into Fahrenheit degrees
# List = [0, 12, 45.21 ,34, 99.91]
centigrade = [0, 12, 45.21 ,34, 99.91]
fahrenheit = (np.array(centigrade) * 9 / 5) + 32
print(fahrenheit)
print()
