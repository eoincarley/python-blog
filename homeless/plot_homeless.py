import csv
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdate
import time
import matplotlib.colors as colors_fun
import pdb

file = open('homeless_numbers.csv', 'rt')
reader = csv.reader(file)
data = [x for x in reader]
data = np.array(data)
data = numpy.delete(data, (0), axis=0)
times = [row[0] for row in data]
time_utc = [ mdate.epoch2num(time.mktime(time.strptime(times[i], "%Y-%m-%d"))) for i in np.arange(len(times))]
total = [row[1] for row in data]

male = [row[2] for row in data]
female = [row[3] for row in data]

age0 = [row[4] for row in data]
age1 = [row[4] for row in data]
age2 = [row[4] for row in data]
age3 = [row[4] for row in data]


colors = cm.rainbow(np.linspace(0, 1, 3))
colors = [colors_fun.rgb2hex(color) for color in colors]
plt.plot_date(time_utc, total, linestyle='-', linewidth=0.5, alpha=0.7, color=colors[0])
#plt.plot_date(time_utc, male, linestyle='-', linewidth=0.5, alpha=0.7, color=colors[1])
#plt.plot_date(time_utc, female, linestyle='-', linewidth=0.5, alpha=0.7, color=colors[2])



plt.ylabel('Total number of homeless')
plt.xlabel('Time (UT)')
plt.legend()
grid(b=True, which='major', color='#d3d3d3', linestyle='-')
plt.show()