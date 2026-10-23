import numpy as np
import matplotlib
matplotlib.use("TkAgg")
import matplotlib.pyplot as plt

x = np.linspace(0, 4 * np.pi, 240)

plt.figure("Graph using Matplot")
plt.plot(x, np.sin(x), label="sin(x)")
plt.plot(x, np.log(x), label="log(x)")
plt.plot(x, np.cos(x), label="cos(x)")
plt.title("Trigonometric Functions")
plt.legend()
plt.grid(True)
plt.show()
