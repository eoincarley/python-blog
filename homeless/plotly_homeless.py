import csv
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdate
import time
import matplotlib.colors as colors_fun
import matplotlib.cm as cm
import plotly.plotly as py
import plotly.graph_objs as go
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


colors = cm.rainbow(np.linspace(0, 1, 4))
colors = [colors_fun.rgb2hex(color) for color in colors]	

traces = [go.Scatter(x=times, y=total, line = {'width':2}, marker={'color': colors[0], 'symbol': 100, 'size': "10"}, 
		mode="markers+lines", text=['Total'], name='Total')]

trace_male = go.Scatter(x=times, y=male, line = {'width':2}, marker={'color': colors[1], 'symbol': 100, 'size': "10"}, 
		mode="markers+lines", text=['Male'], name='Male')
traces.append(trace_male)

trace_female = go.Scatter(x=times, y=female, line = {'width':2}, marker={'color': colors[2], 'symbol': 100, 'size': "10"}, 
		mode="markers+lines", text=['Female'], name='Female')
traces.append(trace_female)


layout = {'xaxis': {'title': 'Time'},
  		  'yaxis': {'title': 'Number of homeless adults'}}

data = go.Data(traces)
plot = py.iplot(go.Figure(data=data, layout=layout), filename='Total-Homeless-Ireland')