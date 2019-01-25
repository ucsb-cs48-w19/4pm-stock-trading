import os
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def hello():
    return render_template("hello.html", title = 'HelloWorld')

if __name__ == "__main__":
	port = int(os.environ.get('PORT', 33507))
	app.run()