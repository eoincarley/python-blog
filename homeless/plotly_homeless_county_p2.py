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

file = open('homeless_by_county.csv', 'rt')
reader = csv.reader(file)
data = [x for x in reader]
county = [x[0] for x in data]
number = [float(x[1]) for x in data]
population = [float(x[2]) for x in data]
number_per_capita = [round(number[index]/(population[index]/1e4), 2) for index in np.arange(len(number))]

county = np.array(county)
county =np.arrange
number_per_capita = np.array(number_per_capita)
index = np.flip(np.argsort(number_per_capita), 0)
number_per_capita = number_per_capita[index]
county = county[index]



data = [go.Bar(
            x=county,
            y=number_per_capita,
            #text=number_per_capita,
            textposition = 'auto',
            marker=dict(
                color='rgb(158,202,225)',
                line=dict(
                    color='rgb(8,48,107)',
                    width=1.5),
            ),
            opacity=0.6
        )]

layout = go.Layout(
    title='Number of homeless per 10,000 of county population',
    yaxis=dict(
        title='Number per 1e4',
        titlefont=dict(
            size=16,
            color='rgb(107, 107, 107)'
        ),
    ),
)


fig = go.Figure(data=data, layout=layout)
py.iplot(fig, filename='Homeless-county-per-capita')