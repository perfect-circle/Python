from die import Die
import pygal

# 创建一个色子
die_1 = Die()
die_2 = Die()

# 丢几次色子，并将其记录在列表中
results = []
for roll_num in range(1000):
    die_1_num = die_1.roll()
    die_2_num = die_2.roll()
    die_num = die_1_num + die_2_num
    results.append(die_num)

# 分析结果
frequencies = []
max_result = die_1.num_sides + die_2.num_sides
for value in range(2,max_result+1):
    frequency = results.count(value)
    frequencies.append(frequency)

# 对数据进行可视化
hist = pygal.Bar()

hist.title = "Results of rolling two D6 1000 times."
hist.x_labels = ['2','3','4','5','6','7','8','9','10','11','12']
hist.x_title = "Result"
hist.y_title = "Frequency of Result"

hist.add('Two D6',frequencies)
hist.render_to_file('die_visual.svg')
