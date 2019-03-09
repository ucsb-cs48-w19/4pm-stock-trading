import plotly as py
import pandas as pd
import numpy as np

from datetime import datetime
from datetime import time as dt_tm
from datetime import date as dt_date

import plotly.plotly as py
import plotly.tools as plotly_tools
import plotly.graph_objs as go
plotly_tools.set_credentials_file(username='franklee26', api_key='NUbcE4xBFBPFP6tezOBR')

import os
import tempfile
os.environ['MPLCONFIGDIR'] = tempfile.mkdtemp()
import matplotlib.pyplot as plt

from IPython.display import HTML
import stocks

# moving average backend 
def moving_average(interval, window_size):
	window = np.ones(int(window_size))/float(window_size)
	return np.convolve(interval, window, 'same')

# returns a plotly url (will append url below in html)
def makeGraph(stock_name, stock_abbrev, quotes, quote, upvotes):
	x = []
	y = []
	values = []
	ma = []
	print(stock_name)
	print(stock_abbrev)

	price = str(quote['latestPrice'])
	op = str(quote['open'])
	close = str(quote['close'])	
	pe = str(quote['peRatio'])
	cap = str(quote['marketCap'])
	volume = str(quote['latestVolume'])
	w52high = str(quote['week52High'])
	w52low = str(quote['week52Low'])

	if len(quotes) == 0:
		print ("quotes empty")
	else:
		for k in quotes.keys():
			x.append(k);
		for i in range(len(quotes)):
			values.append(quotes[x[i]])
		y = list(map(float,values))
		ma = moving_average(y, 10)

	xy_data = go.Scatter( x=x, y=y, mode='markers', marker=dict(size=4), name=stock_abbrev)
	mov_avg = go.Scatter( x=x[5:-4], y=ma[5:-4], \
					  line=dict(width=2,color='red'), name='Moving average' )
	# data = [xy_data, mov_avg]
	# trying to add annotation to graph
	# Sets the text at x,y and so I off set it proportional to the 40% of the max range. Works surpisingly well!
	# ISSUE: Can't add $ symbol to string! The html is doing something weird with it
	annotations = []
	annotations.append(dict(xref='paper', x=1.01, y=max(y) - 0.4 * (max(y) - min(y)), 
                                  xanchor='left', yanchor='middle',
                                  text='<b>Information on ' + stock_abbrev + "\nPrice: " + price + "\nOpen: " + op + "\nClose: " + close + "\nPE: " + pe +
                                  "\nCAP: " + cap + "\nVolume: " + volume + "\nw52high: " + w52high + "\nw52low: " + w52low + "</b>",
                                  font=dict(family='Arial',
                                            size=15),
                                  showarrow=False))
	data = go.Data([xy_data, mov_avg])
	layout=go.Layout(yaxis={'title':'Price (USD)'})
	layout['annotations'] = annotations
	figure=go.Figure(data=data,layout=layout)
	
	config = {'scrollZoom': False}
	py.iplot(figure, filename=stock_name + ' stock moving average', annotations = annotations, config = config)

	plot_url = py.plot(figure, filename=stock_name + ' stock moving average', auto_open=False, annotations = annotations)
	print (plot_url)
	return (plot_url)

if __name__ == "__main__":
	makeGraph("Apple", "AAPL", {"2017-01-01": 11, "2017-01-02": 6, "2017-01-03": 7.5}) #default graph
