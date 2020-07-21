import csv

from datetime import datetime

from matplotlib import pyplot as plt

filename = 'death_valley_2014.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    highs = []
    dates = []
    lows = []
    for row in reader:
        try:
            date = datetime.strptime(row[0], "%Y-%m-%d")
            low = int(row[3])
            high = int(row[1])
        except ValueError:
            print(date,'missing data')
        else:
            dates.append(date)
            highs.append(high)
            lows.append(low)

# 根据数据绘制图形
fig = plt.figure(dpi=128, figsize=(15,12))
plt.plot(dates, highs, c='red', alpha=0.5)
plt.plot(dates, lows, c='blue', alpha=0.5)
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

# 设置图形的格式
plt.title("Daily high and low temperatures - 2014\nDeath Valley,CA", fontsize=24)
plt.xlabel('',fontsize=14)
fig.autofmt_xdate()     # x轴标签斜体
plt.ylabel('Temperatures', fontsize=16)

plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()
