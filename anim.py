import matplotlib.pyplot as plt
import numpy as np
fig = plt.figure()
x = np.linspace(0, 2 * np.pi, 50)
y_sin = np.sin(x)
y_cos = np.cos(x)
plt.title('sin(x) & cos(x)')
plt.xlabel('X axis')
plt.ylabel('Y axis')
plt.plot(x, y_sin, color = "red", linewidth = 1.5, linestyle = "-.", label = "y_sin")
plt.plot(x, y_cos, marker = '+', linestyle = '-', label = 'y_cos')
plt.legend(loc = "upper left")
plt.show()