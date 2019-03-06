#! /usr/bin/python3

import os
from flask import Flask, render_template, request, url_for
import stocks
import graph
import stocklist
from glob import glob
import json

app = Flask(__name__)

@app.route('/')
def home():
	for file in glob("./templates/*-graph.html"):
		os.remove(file)
	names = []
	tickers = []
	prices = []
	stocklist.save_stock_tickers(names, tickers, prices)
	return render_template("home.html", title = 'home', stocknames = names, stocktickers = tickers, prices = prices)

@app.route('/recommended')
def render_recommended():
	return render_template("recommended.html", title = 'recommended')

@app.route('/mystocks')
def render_my_stocks():
	return render_template("mystocks.html", title = 'mystocks')

@app.route('/about')
def render_about():
    return render_template("about.html", title = 'about')

@app.route('/upvoted', methods = ['GET'])
def button_pressed():
	stockabbrev = request.args.get('abbrev')
	file = open('Data/stockData.txt', 'r')
	stockDict = json.loads(file.read())
	file.close()
	stockDict[stockabbrev] = stockDict[stockabbrev] + 1
	file = open('Data/stockData.txt', 'w')
	file.write(json.dumps(stockDict))
	file.close()
	return render_template("graph.html", title = 'stockinfo', display = 'Upvoted')

@app.route('/stockinfo', methods = ['GET']) #example http query: (home url)/stockinfo?name=Microsoft&abbrev=MSFT
def showInfo():
	for file in glob("./templates/*-graph.html"): #get rid of all previous graph htmls <- temp fix
		os.remove(file)
	stockname = request.args.get('name')
	stockabbrev = request.args.get('abbrev')

	file = open('Data/stockData.txt', 'r')
	stockDict = json.loads(file.read())
	file.close()
	upvotes = stockDict[stockabbrev]

	data = stocks.getChart(stockabbrev)
	quote = stocks.getQuote(stockabbrev)
	graph.makeGraph(stockname, stockabbrev, data, quote, upvotes)
	sheet = "graph.html"
	return render_template(sheet, title = 'stockinfo', display = 'Upvote')

if __name__ == "__main__":
	port = int(os.environ.get('PORT', 33507))
	app.run()