import matplotlib.pyplot as plt

plt.rc("font", family="SimHei", size="12")  # 用于解决中文显示不了的问题

x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y1 = [0.73, 0.69, 0.73, 0.75, 0.73, 0.70, 0.73, 0.72, 0.74, 0.73]
y2 = [0.70, 0.65, 0.70, 0.74, 0.70, 0.68, 0.70, 0.71, 0.69, 0.70]
y3 = [0.69, 0.70, 0.69, 0.66, 0.69, 0.71, 0.69, 0.68, 0.72, 0.69]
y4 = [0.45, 0.47, 0.45, 0.5, 0.45, 0.43, 0.45, 0.47, 0.44, 0.45]

plt.plot(x, y1, marker='.', label='算法1')
plt.plot(x, y2, marker='*', label='算法2')
plt.plot(x, y3, marker=6, label='算法3')
plt.plot(x, y4, marker='H', label='算法4')

plt.legend()  # 让图例生效

plt.xticks([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [r'1', r'2', r'3', r'4', r'5', r'6', r'7', r'8', r'9', r'10'])
plt.yticks([0.3,  0.5,  0.7, 0.9], [r'0.3', r'0.5', r'0.7', r'0.9'])

plt.xlim(0, 11)
plt.ylim(0.2, 1.0)

plt.xlabel("实验次数")  # X轴标签
plt.ylabel("准确率")  # Y轴标签
plt.title("XXXXX实验结果")  # 标题

plt.show()
