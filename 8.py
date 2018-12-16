import numpy as np
import matplotlib.pyplot as plt
import matplotlib

# 设置图片尺寸 14" x 7"
matplotlib.rc('figure', figsize=(8, 4))
# 设置字体 14
# matplotlib.rc('font', size=20)
# 不显示顶部和右侧的坐标线
matplotlib.rc('axes.spines', top=False, right=False)
# 不显示网格
matplotlib.rc('axes', grid=False)
# 设置背景颜色是白色
matplotlib.rc('axes', facecolor='white')

name = ['类别1', '类别2', '类别3', '类别4', '类别5', '类别6', '类别7', '类别8', '类别9', '类别10']

# 绘图
x = np.arange(10)
data = np.random.rand(10) * 100
plt.barh(x, data, tick_label=name, alpha=0.6)
plt.show()
