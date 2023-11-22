# Creating a 1 dimensional array
import numpy as np
x = np.array([1, 2, 3, 4, 5, 6, 7, 8])
print(x)
print("X has elements of type: ", x.dtype)

# return number of dimensions in the array
print(x.ndim)

# 2 dimensional array
y = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
print(y)
print(y.ndim)
print("Y is an object of type: ", type(y))
print("Y elements are of type: ", y.dtype)
print("Y has a total of ", y.size, "elements")
print("Y has", y.shape, "dimensions")

# How would I save a numpy array to a file
np.save('my_array', y) # a file names my_array was just created.

# how do I access the saved array into another variable.
# basically I want to use the information on that array
z = np.load('my_array.npy')
print("\n")
print(z)
print("Z has", z.size,"dimensions")
print("Z is of type", type(z))
print("Elements of Z are of type", z.dtype)