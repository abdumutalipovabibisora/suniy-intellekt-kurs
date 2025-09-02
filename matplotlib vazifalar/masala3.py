import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-5, 5, 100)
y1 = np.sin(x)
y2 = 0.5

plt.plot(x, y1, label='y = sin(x)', color='blue')
plt.plot(x, y2, label='y = 0.5', color='green')

plt.plot(-2, 0, 'ro')
plt.text(-1.5, -1, 'Kesishish nuqtasi (-2, 0)', color='red')
plt.plot(3, 5, 'ro')
plt.text(3.3, 4, 'Kesishish nuqtasi (3, 5)', color='red')

plt.title("funksiya garfigi")
plt.xlabel("x oqi")
plt.ylabel("y oqi")
plt.grid()
plt.legend()
plt.show()