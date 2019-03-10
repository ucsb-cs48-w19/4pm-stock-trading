#! /usr/bin/python3

import os
from flask import Flask, render_template, request, url_for
import stocks
import graph
import stocklist
from glob import glob
import json

app = Flask(__name__)

# routes to home page
@app.route('/')
def home():
	names = []
	tickers = []
	prices = []
	stocklist.save_stock_tickers(names, tickers)
	return render_template("home.html", title = 'home', stocknames = names, stocktickers = tickers)

# routes to trending page
@app.route('/trending')
def render_recommended():
	file = open('data/stockData.txt', 'r')
	stockDict = json.loads(file.read())
	file.close()
	names = []
	tickers = []
	upvotes = []
	for i in range(5):
		maxticker = list(stockDict.keys())[0]
		maxUpvote = list(stockDict.values())[0]
		for key, value in stockDict.items():
			if(isinstance(value, int) and value > maxUpvote):
				maxticker = key
				maxUpvote = value
		tickers.append(maxticker)
		names.append(stockDict[maxticker + '-name'])
		upvotes.append(str(maxUpvote))
		stockDict.pop(maxticker)
		stockDict.pop(maxticker+'-name')
	return render_template("recommended.html", title = 'Trending',stocknames = names, stocktickers= tickers, upvotes = upvotes)

# routes to stocks page
@app.route('/mystocks')
def render_my_stocks():
	return render_template("mystocks.html", title = 'mystocks')

# routes to about page
@app.route('/about')
def render_about():
    return render_template("about.html", title = 'about')

# routes to upvoted 
@app.route('/upvoted', methods = ['GET','POST'])
def button_pressed():
	stockname = request.args.get('name')
	stockabbrev = request.args.get('abbrev')
	url = request.form.get("url")
	#########
	file = open('data/stockData.txt', 'r')
	stockDict = json.loads(file.read())
	file.close()
	stockDict[stockabbrev] = stockDict[stockabbrev] + 1
	upvotes = stockDict[stockabbrev]
	file = open('data/stockData.txt', 'w')
	file.write(json.dumps(stockDict))
	file.close()
	data = stocks.getChart(stockabbrev)
	quote = stocks.getQuote(stockabbrev)
	return render_template("graph.html", title = 'stockinfo', name = stockname, abbrev = stockabbrev, graph_url = url, vote_count = upvotes)

# routes to info
@app.route('/stockinfo', methods = ['GET']) #example http query: (home url)/stockinfo?name=Microsoft&abbrev=MSFT
def showInfo():
	stockname = request.args.get('name')
	stockabbrev = request.args.get('abbrev')

	file = open('data/stockData.txt', 'r')
	stockDict = json.loads(file.read())
	file.close()
	upvotes = stockDict[stockabbrev]

	data = stocks.getChart(stockabbrev)
	quote = stocks.getQuote(stockabbrev)
	url = graph.makeGraph(stockname, stockabbrev, data, quote)
	return render_template("graph.html", title = 'stockinfo', name = stockname, abbrev = stockabbrev, graph_url = url, vote_count = upvotes)


@app.route('/google973af8c591e84ad7.html')
def render_ver():
	return render_template("google973af8c591e84ad7.html", title = 'verification')
if __name__ == "__main__":
	port = int(os.environ.get('PORT', 33507))
	app.run()
