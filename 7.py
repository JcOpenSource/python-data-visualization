import matplotlib.pyplot as plt
import numpy as np
import matplotlib

# 设置图片尺寸 8 x 4
matplotlib.rc('figure', figsize=(8, 4))
# 不显示顶部和右侧的坐标线
matplotlib.rc('axes.spines', top=False, right=False)
# 不显示网格
matplotlib.rc('axes', grid=True)

# 0.数据
x_data = np.random.rand(100) * 100
y_data = np.random.rand(100) * 100

# 1.画图
plt.scatter(x_data, y_data, s=10, color='k')
plt.title("title")
plt.xlabel("x_label")
plt.ylabel("y_label")
plt.show()
