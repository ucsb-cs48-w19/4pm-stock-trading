import os

from flask import Flask, render_template, request

app = Flask(__name__)

    # a simple page that says hello
@app.route('/')
def hello():
    return render_template("index.html", title = 'HelloWorld')

if __name__ == "__main__":
    app.run()
