# def add_nums(a, b):
#     return a + b



# def add_num_vec(num, vec):
#     for i in range(len(vec)):
#         vec[i] += num
#     return vec



# def add_vecs(a, b):
#     n = len(a)
#     if n == len(b):
#         for i in range(n):
#             a[i] += b[i]
#         return a

# son = 7
# vec1 = [3,4]
# vec2 = [1,2,3]
# vec3 = [5,6]

# print(add_nums(5, son))

# print(add_num_vec(son, vec2))

# print(add_num_vec(son, vec1))

# print(add_vecs(vec1, vec3))

# print(add_vecs(vec2, vec3))


# import numpy as np

# a = np.array([1, 2, 3])
# b = 5
# vec = [3, 4, 5]
# print(a + b)
# print(a + vec)
# print(a * 5)
# print(a * vec)

# class Num:
#     def __init__(self, num):
#         self.num = num
        
#     def __add__(self, num):
#         if type(num) is list:
#             for i in range(len(num)):
#                 num[i] += self.num
#             return num
#         return self.num + num
    
# a = Num(5)
# print(a + 10)
# print(a + [1, 2, 3])

# a = 16
# print(np.sqrt(a))
# print(np.sqrt([a, 25]))

a = np.array([[1, 2], [3, 4]])
t = a.T
print(a + t)
print(a * t)
print(a @ t)
print(a, t)