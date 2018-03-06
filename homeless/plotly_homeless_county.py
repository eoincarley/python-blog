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
number = [x[1] for x in data]

colors = cm.GnBu(np.linspace(1, 0, len(number)) )
colors = [colors_fun.rgb2hex(color) for color in colors]	

trace = go.Pie(labels=county, values=number,
               hoverinfo='label+percent', textinfo='value', 
               textfont=dict(size=20),
               marker=dict(colors=colors, 
                           line=dict(color='#000000', width=0.5)))

py.iplot([trace], filename='Homeless-by-county')