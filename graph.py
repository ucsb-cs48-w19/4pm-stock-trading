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
import stocks


def moving_average(interval, window_size):
	window = np.ones(int(window_size))/float(window_size)
	return np.convolve(interval, window, 'same')

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
		<link rel="stylesheet"  type="text/css" href="{{url_for('static', filename='styles.css')}}">
		<link href="https://fonts.googleapis.com/css?family=Julius+Sans+One" rel="stylesheet">
		<link href="https://fonts.googleapis.com/css?family=Raleway" rel="stylesheet">
		<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.1/css/bootstrap.min.css">
		<style>body{ margin:0 100; background:whitesmoke; }</style>
	</head>
	<style>
		.topnav {
			font-family: 'Raleway', sans-serif;
			background-color: #333;
			overflow: hidden;
			
		}

	/* Style the links inside the navigation bar */
		.topnav a {

			float: left;
			color: #f2f2f2;
			text-align: center;
			padding: 14px 16px;
			text-decoration: none;
			font-size: 13px;
		}

	/* Change the color of links on hover */
		.topnav a:hover {
			transition: .3s ease-out;
			background-color: #ddd;
			color: black;
		}

	/* Add a color to the active/current link */
		.topnav a.active {
			background-color: #4CAF50;
			color: white;
		}
		html,
		body{
			margin: 0;
			height:100%;
			background: #fcfcfc;
			background-size: cover;
		}
		section{
			margin: 50px;
			font-family: 'Raleway', sans-serif;
			margin-top: 0px;
		}
		.header{
			margin-top: 30px;
			color: white;
			text-align: center;
			font-family: 'Raleway', sans-serif;
		}
	</style>
	<body>
		<div class="topnav">
	  		<a class="active" href="/">Home</a>
	  		<a href="/recommended">Recommended Stocks</a>
	  		<a href="/mystocks">My Stocks</a>
	  		<a href="/about">About</a>
		</div>
	<h3 class = "header">4PM STOCK TRADING</h3>
	<section>
	<a href =''' + '/upvoted?abbrev=' + stock_abbrev + '''><button>upvote</button></a>
	</section>
	<section>
	<p>'''+'This stock has ' + upvotes + ' upvotes' + '''</p>
	</section>
	<section class = "graph">
		<h1>''' + stock_name + ' (' +stock_abbrev + ''') stock in the past year</h1>
		<iframe width="1000" height="550" frameborder="0" seamless="seamless" scrolling="no" \
src="''' + plot_url + '''.embed?width=800&height=550"></iframe>
	</section>
	<section>
		<p>''' + 'Information for ' + stock_abbrev + '''</p>
		<p>''' + 'Current Price: $' + price + '''</p>
		<p>''' + 'Open: $' + op + '''</p>
		<p>''' + 'Close: $' + close + '''</p>
		<p>''' + 'PE ratio: ' + pe + '''<p>
		<p>''' + 'Latest Volume: ' + volume + '''</p>
		<p>''' + '52 Week High: $' + w52high + '''</p>
		<p>''' + '52 Week Low: $' + w52low + '''</p>
		<p>''' + 'Market Cap: $' + cap + '''</p>
	</section>
	</body>
</html>'''
	file = './templates/graph.html'
	f = open(file,'w')
	f.write(html_string)
	f.close()

if __name__ == "__main__":
	makeGraph("Apple", "AAPL", {"2017-01-01": 11, "2017-01-02": 6, "2017-01-03": 7.5}) #default graph