from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "UCSB-CS48 STOCK-TRADING-4PM"
