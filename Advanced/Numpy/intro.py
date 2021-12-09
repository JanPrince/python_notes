import numpy as np



a = np.arange(15).reshape(3, 5)
print(a)

# get all class methods of a
# print(dir(a))
print(help(a))

# shape of array
print(a.shape)

# the number of dimensions ("axes" in numpy)
print(a.ndim)

# size of array
print(a.size)

# dtype - type of elements in the array
print(a.dtype)                          # int32

print(type(a))

print("=======================================================================")

b = np.array([9, 3, 5, 6])
print(b.ndim)                       # 1 dimension/axis
print(b.shape)

print("=======================================================================")
# c = np.array([[4.0, 3.5, 5.0], [0.2, 0.22]], dtype=np.float64)
# print(c.ndim)                       # 2 dimensional array
# print(c.shape)
# print(c.dtype)