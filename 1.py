import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties

#mac支持中文
font = FontProperties(fname='/Library/Fonts/Songti.ttc')

# 数据准备
x = range(1, 11)
y1 = [0.514820119, 0.540265696, 0.514820119, 0.514820119, 0.552988485, 0.514820119, 0.496779618, 0.514820119, 0.527542907, 0.514820119]
y2 = [0.188128434, 0.188128434, 0.188128434, 0.188128434, 0.188128434, 0.188128434, 0.188128434, 0.188128434, 0.188128434, 0.188128434]
y3 = [0.726365738, 0.682187617, 0.683241911, 0.685723948, 0.688467763, 0.689401198, 0.690968143, 0.691350712, 0.694016418, 0.694324856]
y4 = [0.734460903, 0.696623025, 0.696934759, 0.697733559, 0.697891845, 0.697293132, 0.697519995, 0.695791853, 0.69578938, 0.695674162]
y5 = [0.809058993, 0.717387038, 0.717405582, 0.717170923, 0.716692194, 0.715951522, 0.716337443, 0.718476258, 0.718576645, 0.718658172]

plt.plot(x, y1, label='算法1')
plt.plot(x, y2, label='算法2')
plt.plot(x, y3, label='算法3')
plt.plot(x, y4, label='算法4')
plt.plot(x, y5, label='算法5')

plt.legend(loc='lower right', prop=font)  # 让图例生效
plt.xlabel("实验次数", fontproperties=font)  # X轴标签
plt.ylabel("实验准确度", fontproperties=font)  # Y轴标签
plt.title("Comparison of algorithm accuracy")  # 标题

plt.show()
