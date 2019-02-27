#! /usr/bin/python3

import os
from flask import Flask, render_template, request, url_for
import stocks
import graph
import stocklist
from glob import glob

app = Flask(__name__)

@app.route('/')
def home():
	for file in glob("./templates/*-graph.html"):
		os.remove(file)
	names = []
	tickers = []
	stocklist.save_stock_tickers(names, tickers)
	return render_template("home.html", title = 'home', stocknames = names, stocktickers = tickers)

@app.route('/recommended')
def render_recommended():
	return render_template("recommended.html", title = 'recommended')

@app.route('/mystocks')
def render_my_stocks():
	return render_template("mystocks.html", title = 'mystocks')

@app.route('/about')
def render_about():
    return render_template("about.html", title = 'about')

@app.route('/stocks') #test function that shows microsoft data, currently not used
def dynamic_page():
	data = stocks.getChart("MSFT") 
	graph.makeGraph("Microsoft", "MSFT", data)
	return render_template("graph.html", title = 'stockinfo')

@app.route('/stockinfo', methods = ['GET']) #example http query: (home url)/stockinfo?name=Microsoft&abbrev=MSFT
def showInfo():
	for file in glob("./templates/*-graph.html"): #get rid of all previous graph htmls <- temp fix
		os.remove(file)
	stockname = request.args.get('name')
	stockabbrev = request.args.get('abbrev')
	data = stocks.getChart(stockabbrev)
	graph.makeGraph(stockname, stockabbrev, data)
	sheet = stockname+"-graph.html"
	return render_template(sheet, title = 'stockinfo')

if __name__ == "__main__":
	port = int(os.environ.get('PORT', 33507))
	app.run()