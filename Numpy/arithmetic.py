import numpy as np
# Element-wise arithmetic operations on 1-D arrays

# We create two rank 1 ndarrays
x = np.array([1, 2, 3, 4])
y = np.array([5.5, 6.5,7.5,8.5])
print('add(x,y) = ', np.add(x, y))
print('subtract(x,y) = ', np.subtract(x, y))
print('multiply(x,y) = ', np.multiply(x, y))
print('divide(x,y) = ', np.divide(x, y))

print("\n")

# Element-wise arithmetic operations on a 2-D array (Same shape)
X = np.array([1, 2, 3, 4]).reshape(2, 2)
Y = np.array([5.5, 6.5,7.5,8.5]).reshape(2,2)
print('add(x,y) = ', np.add(x, y))
print('subtract(x,y) = ', np.subtract(x, y))
print('multiply(x,y) = ', np.multiply(x, y))
print('divide(x,y) = ', np.divide(x, y))

print("\n")

# Statistical functions
X = np.array([[1, 2], [3,4]])
print(X)
print('Average of all elements in the columns of X:', X.mean(axis=0))
print('Average of all elements in the rows of X:', X.mean(axis=1))

print('Sum of all elements in the columns of X:', X.sum(axis=0))
print('Sum of all elements in the rows of X:', X.sum(axis=1))

print('Median of all elements in the columns of X:', np.median(X, axis=0))
print('Median of all elements in the rows of X:', np.median(X, axis=1))

print("\n")

# Change value of all elements of an array
X = np.array([[1,2], [3,4]])
print(X * 4)
print("\n")

# Arithmetic operations on 2-D arrays (Compatible shape)
# We create a rank 1 ndarray
x = np.array([1, 2,3])
# We create a 3 x 3 ndarray
Y = np.array([[1, 2,3],[4,5,6],[7,8,9]])
# We create a 3 x 1 ndarray
Z = np.array(x).reshape(3,1)

print(x)
print(Y)
print(Z)
print()
print('x + Y = \n', x + Y)
print('Z + Y = \n', Z + Y)