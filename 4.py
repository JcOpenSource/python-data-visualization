import matplotlib.pyplot as plt
import seaborn as sns
from pandas import DataFrame

plt.rc("font", family="SimHei", size="12")  # 用于解决中文显示不了的问题

# 数据
Conference = {'AAAI': 18, 'ACL': 4, 'CIKM': 12, 'CogSci': 1, 'ICLR': 4, 'ICML': 6, 'IJCAI': 17, 'KDD': 31, 'NIPS': 3, 'SDM': 2, 'TKDE': 1, 'WSDM': 7, 'WWW': 6}
x_Conference = []
y_Conference = []
for (key, value) in Conference.items():
    x_Conference.append(key)
    y_Conference.append(value)
dictionary = {'会议': x_Conference, '数量': y_Conference}
frame = DataFrame(dictionary)

# 设置图片的大小格式
plt.figure(figsize=(8, 5))

sns.barplot(x='会议', y='数量', data=frame)

plt.show()
