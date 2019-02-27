import os
from flask import Flask, render_template, request, url_for
import stocks

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("home.html", title = 'home')

@app.route('/recommended')
def render_recommended():
    return render_template("recommended.html", title = 'recommended')

@app.route('/mystocks')
def render_my_stocks():
    return render_template("mystocks.html", title = 'mystocks')

@app.route('/about')
def render_about():
    return render_template("about.html", title = 'about')

@app.route('/stocks')
def dynamic_page():
    return stocks.getChart("MSFT")
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 33507))
    app.run()
