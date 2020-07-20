import pygal
from die import Die

# 创建两个色子
die_1 = Die(8)
die_2 = Die(8)

# 两个色子和的结果列表
number = int(input("Pleace entru roll number: "))
results = [die_1.roll() + die_2.roll() for roll_num in range(number)]

# 统计各个值的个数
max_result = die_1.num_sides + die_2.num_sides
frequencies = [results.count(value) for value in range(2,max_result+1)]

# 绘图
hist = pygal.Bar()

hist.title = "两颗D8丢" + str(number) + "次"
hist.x_labels = [str(x) for x in range(2,max_result+1)]
hist.x_title = "结果"
hist.y_title = "结果的频率"

hist.add("D8 + D8",frequencies)
hist.render_to_file("two_D8.pvg")
