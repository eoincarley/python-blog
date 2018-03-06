import csv
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdate
import time
import matplotlib.colors as colors_fun
import matplotlib.cm as cm
import plotly.plotly as py
import plotly.graph_objs as go
from plotly import tools
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
age1 = [row[5] for row in data]
age2 = [row[6] for row in data]
age3 = [row[7] for row in data]


colors = cm.rainbow(np.linspace(0, 1, 3))
colors = [colors_fun.rgb2hex(color) for color in colors]    

#traces = [go.Scatter(x=times, y=total, line = {'width':2}, marker={'color': colors[0], 'symbol': 100, 'size': "10"}, 
 #       mode="markers+lines", text=['Total'], name='Total')]

#data = go.Data(traces)
#plot = py.iplot(go.Figure(data=data, layout=layout), filename='Total-Homeless-Ireland')


trace0 = go.Scatter(x=times, y=male, line = {'width':2}, marker={'color': colors[0], 'symbol': 100, 'size': "10"}, 
       mode="markers+lines", text=['Male'], name='Male')

trace1 = go.Scatter(x=times, y=female, line = {'width':2}, marker={'color': colors[1], 'symbol': 100, 'size': "10"}, 
         mode="markers+lines", text=['Female'], name='Female')


fig = tools.make_subplots(rows=1, cols=2, specs=[[{}, {}]], shared_xaxes=True,
                          shared_yaxes=False, vertical_spacing=0.001)

fig.append_trace(trace0, 1, 1)
fig.append_trace(trace1, 1, 1)


number = [ male[-1], female[-1]]#, age2[-1], age3[-1] ]
percent = [round(100.0*(float(x)/float(total[-1])),1) for x in number]
age_bracket = ['Male',  'Female']

pdb.set_trace()
trace5 = go.Bar(
    x=age_bracket,
    y=percent,
    marker=dict(
        color='rgba(50, 171, 96, 0.6)',
        line=dict(
            color='rgba(50, 171, 96, 1.0)',
            width=1),
    ),
    name='Percent distribution by gender, July 2017',
)


number = [ male[0], female[0]]#, age2[-1], age3[-1] ]
percent = [round(100.0*(float(x)/float(total[-1])),1) for x in number]
age_bracket = ['Male',  'Female']


trace6 = go.Bar(
    x=age_bracket,
    y=percent,
    marker=dict(
        color='rgba(50, 171, 96, 0.6)',
        line=dict(
            color='rgba(50, 171, 96, 1.0)',
            width=1),
    ),
    name='Percent distribution by gender, July 2017',
)

layout = dict(
    title='Total number of homeless adults',
    yaxis1=dict(
        showline=False,
        showticklabels=True,
        domain=[0, 0.85],
        range=[1300, 3000],
        title='Number of homeless aduuts'
    ),
    yaxis2=dict(
        showline=True,
        linecolor='rgba(102, 102, 102, 0.8)',
        linewidth=2,
        domain=[0, 0.85],
        range=[0, 100],
        title='Percent of total, July 2017'
    ),
    xaxis1=dict(
        zeroline=False,
        showticklabels=True,
        showgrid=True,
        domain=[0, 0.65],
    ),
    xaxis2=dict(
        showticklabels=True,
        showgrid=True,
        domain=[0.7, 1],
    ),
    legend=dict(
        x=0.029,
        y=1.038,
        font=dict(
            size=10,
        ),
    ),
    margin=dict(
        l=100,
        r=20,
        t=70,
        b=70,
    ),
    paper_bgcolor='rgb(248, 248, 255)',
    plot_bgcolor='rgb(248, 248, 255)',
)


# Creating two subplots

fig.append_trace(trace5, 1, 2)


fig['layout'].update(layout)
py.iplot(fig, filename='Ireland-Homeless-Plot1')
