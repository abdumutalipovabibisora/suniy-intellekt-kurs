import numpy as np

# x = np.array([2, 4, 8, 9])
# y = np.array([3, 1, -2, 4])

# k = np.sum(x + y)
# print(k)

# javob = np.sqrt(np.prod(x + y) * 2)
# print(javob)

# x = np.int32((np.random.random((2, 2)) + 1) * 3)
# y = ((np.random.random((2, 2)) + 1) * 3).astype(np.int32)

# print(x,"\n", y)

# k = x * y
# n = x @ y
# print(k)
# print(n)

x = np.array([1, 2, 3, 4])
y = np.array([4, 3, 2, 1])
x = np.reshape(x, (2, 2))
y = np.reshape(y, (2, 2))
print(x @ y)