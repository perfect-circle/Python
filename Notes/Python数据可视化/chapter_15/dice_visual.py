import pygal
from die import Die

# 创建两个色子
die_1 = Die()
die_2 = Die()

# 把两个色子的结果加起来，放在列表中
results = [die_1.roll() + die_2.roll() for roll in range(1000)]

# 统计点总数
max_result = die_1.num_sides + die_2.num_sides
frequencies = [results.count(value) for value in range(2,max_result+1)]

#创建视图
hist = pygal.Bar()

hist.title = "Results of rolling two D6 dice 1000 times."
hist.x_labels = [str(x) for x in range(2,max_result+1)]
hist.x_title = '结果'
hist.y_title = "频率的总数"

hist.add("D6 + D6",frequencies)
hist.render_to_file("dice_visual.svg")
