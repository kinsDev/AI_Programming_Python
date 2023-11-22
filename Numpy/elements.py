import numpy as np
# Accessing, Deleting, and Inserting Elements Into ndarrays

# Modify an element of 1-D array
x = np.array([1, 2, 3, 4, 5])
x[3] = 20
print(x, "\n")

# Access individual elements in 2D
x = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]])
print(x)
print(x[1, 1])#acccess element 6
print(x[2, 1:])#access element 10 to 12
print(x[1:, 1:])#access element 6 to 16
print(x[:, 1:3])#access element in middle
print(np.diag(x))#access only the diagonal elements

print("\n")

# Delete elements
y = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]])
y = np.delete(y, [1, 1])
print(y)

# We append the integer 7 and 8 to x
y = np.append(y, [7, 8])
print(y)

# We insert the integer 50 and 70 between 10 and 11 in y.
y = np.insert(y, 10,[50,70])
print(y)
print("\n")

# We stack a on top of b
a = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]])
b = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]])
s = np.vstack((a, b))
print(a)
print(b, "\n")
print(s, "\n")

# We stack b on top of a
ns = np.vstack((b, a))
print(ns, "\n")

