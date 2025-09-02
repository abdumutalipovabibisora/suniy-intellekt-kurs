# a = [1, 2, 3]
# b = a[0]
# a[0] = a[2]
# a[2] = b
# print(a)

# qol = ["kok", "qora", "qora", "qizil"]

# qizil = qol[0]
# qol[0] = qol[2]
# qol[2] = qizil

# qol[0], qol[1], qol[2], qol[3] = qol[2], qol[1], qol[0], qol[3]

# print(qol)

# qol[0], qol[-1] = qol[-1], qol[0]
# print(qol)

            
# b = qol[0]
# qol[0] = qol[1]
# qol[1] = qol[2]
# qol[2] = qol[3]
# qol[3] = qol[4]
# qol[4] = qol[5]
# qol[5] = qol[6]
# qol[6] = b
# if qol[0] == "qizil":
#     print(qol)

qol = ["kok", "qora", "qora","qora", "qora","qora", "qora", "qizil"]
while qol[0] != "qizil":
    rang = qol.pop(0)
    qol.append(rang)
print(qol)


