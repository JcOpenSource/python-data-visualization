import matplotlib.pyplot as plt
import numpy as np

# x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
x_name = range(1, 11)
y1 = np.random.rand(10) * 100
y2 = np.random.rand(10) * 100
y3 = np.random.rand(10) * 100
y4 = np.random.rand(10) * 100

x = list(range(0, 10))

total_width, n = 0.8, 4
width = total_width / n


plt.bar(x, y1, width=width, label='Algorithm1')

for i in range(len(x)):
    x[i] = x[i] + width
plt.bar(x, y2, width=width, label='Algorithm2', tick_label=x_name)

for i in range(len(x)):
    x[i] = x[i] + width
plt.bar(x, y3, width=width, label='Algorithm3')

for i in range(len(x)):
    x[i] = x[i] + width
plt.bar(x, y4, width=width, label='Algorithm4')

plt.legend()
plt.show()
