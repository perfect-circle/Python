import matplotlib.pyplot as plt
from random_walk import RandomWalk

# 只要程序处于活动状态，就不断地模拟随机漫步
while True:
    # 创建一个RandomWalk实例，并将其包含的点都绘制出来
    rw = RandomWalk(5000)
    rw.fill_walk()

    # 设置窗口尺寸
    plt.figure(figsize=(13,10))
    point_numbers = list(range(rw.num_points))
    plt.plot(rw.x_values, rw.y_values, linewidth=1)

    plt.scatter(0,0,c='green', edgecolors='none',s=30)
    plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red',edgecolors='none',s=30)

    plt.show()

    keep_running = input("Make another walk?(y/n):")
    if keep_running == 'n':
        break
