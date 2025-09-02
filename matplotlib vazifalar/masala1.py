import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-5, 5, 100)
y1 = 2 * x + 1
y2 = -x + 4

plt.plot(x, y1, label='y = 2x + 1', color='blue')
plt.plot(x, y2, label='y = -x + 4', color='green')

plt.plot(1, 3, 'ro')
plt.text(2, 3,'Kesishish nuqtasi (1, 3)', color='red')

plt.title("y = 2x + 1 va y = -x + 4")
plt.xlabel("x oqi")
plt.ylabel("y oqi")
plt.grid()
plt.legend()
plt.show()
