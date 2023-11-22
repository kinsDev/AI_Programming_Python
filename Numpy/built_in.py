# Using Built-in Functions to Create ndarrays
import numpy as np

# Create a Numpy array of zeros with a desired shape
x = np.zeros((3, 4))
print(x, "\n")

# Create a Numpy array of ones
x = np.ones((3, 4))
print(x, "\n")

# Create a numpy array of constant numbers
x = np.full((7, 7), 7)
print(x, "\n")

# Create a Numpy array of an Identity matrix
x = np.eye(5)
print(x, "\n")

# Create a Numpy array of constants diagonal instead of the one with a defauly value
x = np.diag([10, 20, 30, 40, 50, 60, 70, 80, 90, 100])
print(x, "\n")

# Create a Numpy array of evenly spaced values in a given range, using
x = np.arange(10)
print(x, "\n")

# Create a Numpy array using start and stop value
x = np.arange(1, 11)
print(x, "\n")

# Create a Numpy array using start, stop value, and size between the numbers
x = np.arange(0, 22, 3)
print(x, "\n")

# Create a Numpy array using linspace. Linspace allows us o create a specific number of elements evenly on a given range
# I want to create 20 elements on a range of 0 to 60
x = np.linspace(0, 60, 20)
print(x, "\n")
# with endpoint excluded
x = np.linspace(0, 60, 30, endpoint = False)
print(x, "\n")

# Create a Numpy array by feeding the output of arange() function as an argument to the reshape() function.
y = np.linspace(0, 60, 30, endpoint=False)
y = np.reshape(y, (3, 10))
print(y, "\n")

# Create a numpy array and reshape it
y = np.arange(21).reshape(3,7)
print(y, "\n")

# Create a Numpy array using the numpy.random.random() function.
x = np.random.random((4, 5))
print(x, "\n")

# Create a Numpy array using the numpy.random.randint() function.
x = np.random.randint((5, 6))
print(x, "\n")
y = np.random.randint(0, 51, size=(5, 10))
print(y, "\n")

# We create a 1000 x 1000 ndarray of random floats drawn from normal (Gaussian) distribution
# with a mean of zero and a standard deviation of 0.1.
X = np.random.normal(0, 0.1, size=(1000, 1000))
print(X, "\n")