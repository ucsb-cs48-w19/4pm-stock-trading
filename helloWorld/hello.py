import os
from flask import Flask, render_template, request
import stocks

app = Flask(__name__)

@app.route('/')
def hello():
    return render_template("hello.html", title = 'HelloWorld')

@app.route('/printStock')
def render_test():
    return stocks.helper()

@app.route('/liveStocks')
def dynamic_page():
    return stocks.getChart("MSFT")

if __name__ == "__main__":
	port = int(os.environ.get('PORT', 33507))
	app.run()


