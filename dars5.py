import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-100, 100, 200)
# y = x ** 2 - 6 * x + 8
# y1 = 0.4 * x + 5.9
# y2 = 1.4 * x
# y3 = -2 * x + 20
y = np.exp(x)
y1 = np.log(x)
plt.plot(x, y)
plt.plot(x, y1, label= "0.4 * x - 15")
# plt.plot(x, y2, label= "1.4 * x")
# plt.plot(x, y3, label= "-2 *x + 20")

plt.title("Funksiya grafigi")
plt.xlabel("x oqi")
plt.ylabel("y oqi")
# plt.legend()
# plt.xlim(0, 5)
# plt.ylim(0, 100)

plt.grid()
plt.show()
# vazifa 5 ta masala kesishgan nuqtani topish