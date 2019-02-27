import plotly as py
import pandas as pd
import numpy as np

from datetime import datetime
from datetime import time as dt_tm
from datetime import date as dt_date

import plotly.plotly as py
import plotly.tools as plotly_tools
import plotly.graph_objs as go
plotly_tools.set_credentials_file(username='shirlyn', api_key='6xWgJbxX7mvqlJf5M3gx')

import os
import tempfile
os.environ['MPLCONFIGDIR'] = tempfile.mkdtemp()
import matplotlib.pyplot as plt

from IPython.display import HTML


def moving_average(interval, window_size):
	window = np.ones(int(window_size))/float(window_size)
	return np.convolve(interval, window, 'same')

def makeGraph(stock_name, stock_abbrev, quotes):
	x = []
	y = []
	values = []
	ma = []

	if len(quotes) == 0:
		print ("quotes empty")
	else:
		for k in quotes.keys():
			x.append(k);
		for i in range(len(quotes)):
			values.append(quotes[x[i]])
		y = list(map(float,values))
		ma = moving_average(y, 10)

	xy_data = go.Scatter( x=x, y=y, mode='markers', marker=dict(size=4), name=stock_abbrev )
	mov_avg = go.Scatter( x=x[5:-4], y=ma[5:-4], \
					  line=dict(width=2,color='red'), name='Moving average' )
	data = [xy_data, mov_avg]

	py.iplot(data, filename=stock_name + ' stock moving average')

	plot_url = py.plot(data, filename=stock_name + ' stock moving average', auto_open=False,)
	print (plot_url)

	html_string = '''
<html>
	<head>
		<meta http-equiv="Cache-Control" content="no-cache, no-store, must-revalidate" />
		<meta http-equiv="Pragma" content="no-cache" />
		<meta http-equiv="Expires" content="0" />
		<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.1/css/bootstrap.min.css">
		<style>body{ margin:0 100; background:whitesmoke; }</style>
	</head>
	<body>
		<h1>''' + stock_name + ' (' +stock_abbrev + ''') stock in the past year</h1>
		<iframe width="1000" height="550" frameborder="0" seamless="seamless" scrolling="no" \
src="''' + plot_url + '''.embed?width=800&height=550"></iframe>
	</body>
</html>'''
	file = './templates/'+stock_name+'-graph.html'
	f = open(file,'w')
	f.write(html_string)
	f.close()

if __name__ == "__main__":
	makeGraph("Apple", "AAPL", {"2017-01-01": 11, "2017-01-02": 6, "2017-01-03": 7.5})