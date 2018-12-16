import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties

# mac支持中文
font = FontProperties(fname='/Library/Fonts/Songti.ttc')
#
Conference = {'AAAI': 18, 'ACL': 4, 'CIKM': 12, 'CogSci': 1, 'ICLR': 4, 'ICML': 6, 'IJCAI': 17, 'KDD': 31, 'NIPS': 3, 'SDM': 2, 'TKDE': 1, 'WSDM': 7, 'WWW': 6}
# 数据
x = []
y = []
for key, value in Conference.items():
    x.append(key)
    y.append(value)

# 设置图片的大小格式
plt.figure(figsize=(8, 5))

plt.bar(x, y, tick_label=x)

plt.xlabel("会议", fontproperties=font)  # X轴标签
plt.ylabel("数量", fontproperties=font)  # Y轴标签

plt.show()
