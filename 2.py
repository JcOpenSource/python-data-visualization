import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties

# mac支持中文
font = FontProperties(fname='/Library/Fonts/Songti.ttc')

x = range(1, 11)
yD = [0.514820119, 0.540265696, 0.514820119, 0.514820119, 0.552988485, 0.514820119, 0.496779618, 0.514820119, 0.527542907, 0.514820119]
yE = [0.188128434, 0.188128434, 0.188128434, 0.188128434, 0.188128434, 0.188128434, 0.188128434, 0.188128434, 0.188128434, 0.188128434]
yL = [0.726365738, 0.682187617, 0.683241911, 0.685723948, 0.688467763, 0.689401198, 0.690968143, 0.691350712, 0.694016418, 0.694324856]
yR = [0.734460903, 0.696623025, 0.696934759, 0.697733559, 0.697891845, 0.697293132, 0.697519995, 0.695791853, 0.69578938, 0.695674162]
yX = [0.809058993, 0.717387038, 0.717405582, 0.717170923, 0.716692194, 0.715951522, 0.716337443, 0.718476258, 0.718576645, 0.718658172]

# 生成图片格式
fig = plt.figure()

ax1 = fig.add_subplot(121)
ax1.spines['right'].set_color('none')     # 去掉右边的边框线
ax1.spines['top'].set_color('none')       # 去掉上边的边框线
ax1.plot(x, yD, label='算法1')
ax1.plot(x, yE, label='算法2')

# 对x轴和y轴的刻度进行限制
plt.xticks(
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    [r'0', r'1', r'2', r'3', r'4', r'5', r'6', r'7', r'8', r'9', r'10']
)
plt.yticks(
    [0, 0.1, 0.2, 0.4, 0.5, 0.6, 0.7, 0.8],
    [r'0', r'0.1', r'0.2', r'0.3', r'0.4', r'0.5', r'0.6', r'0.7', r'0.78']
)


plt.legend(loc='up right', prop=font)  # 让图例生效
plt.xlabel(r'实验次数', fontproperties=font)  # X轴标签
plt.ylabel(r'准确度', fontproperties=font)  # Y轴标签

ax2 = fig.add_subplot(122)
ax2.spines['right'].set_color('none')     # 去掉右边的边框线
ax2.spines['top'].set_color('none')       # 去掉上边的边框线
ax2.plot(x, yL, label='算法3')
ax2.plot(x, yR, label='算法4')
ax2.plot(x, yX, label='算法5')

plt.xticks(
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    [r'0', r'1', r'2', r'3', r'4', r'5', r'6', r'7', r'8', r'9', r'10']
)
plt.legend(loc='up right', prop=font)  # 让图例生效
plt.xlabel(r'实验次数', fontproperties=font)  # X轴标签
# plt.xlabel("实验次数", fontproperties=font)  # X轴标签
plt.ylabel(r'准确度', fontproperties=font)  # Y轴标签
fig.suptitle(r'算法准确度对比', fontproperties=font, fontsize=15)


# 增加子图间的间隔
fig.subplots_adjust(hspace=0.4)
plt.show()
