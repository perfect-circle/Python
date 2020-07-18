import matplotlib.pyplot as plt

x_values = list(range(0,5001))
y_values = [x**3 for x in x_values]
plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Reds, edgecolor='none', s=20)

# 设置图表标题并给坐标轴加上标签
plt.title("Cubic Numbers", fontsize=14)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Cubic of Value", fontsize=14)

# 设置刻度范围
plt.axis([0,5100, 0,5100**3])
plt.show()
