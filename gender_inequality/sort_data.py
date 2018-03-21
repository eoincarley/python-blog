import csv
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdate
import matplotlib.cm as cm
import matplotlib.colors as colors_fun
import time
import pdb

file = open('gender_inequality.csv', 'rt', encoding='ISO-8859-1')
reader = csv.reader(file)
data = [x for x in reader]
#data = np.array(data)
yyyy = data[0][2:]
ineq_index = [data[i][2:] for i in np.arange(1,len(data)-1)]


#---------------------#
# 	Building colors
'''
colors = cm.rainbow(np.linspace(0, 1, len(neuro_keys)))
colors = [colors_fun.rgb2hex(color) for color in colors]

plt.ylabel('X')
plt.xlabel('Y')
plt.legend()
grid(b=True, which='major', color='#d3d3d3', linestyle='-')
plt.show()
'''