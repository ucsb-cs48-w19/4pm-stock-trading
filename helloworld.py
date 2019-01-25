from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def hello():
    return render_template("hello.html", title = 'HelloWorld')

if __name__ == "__main__":
	#app.listen(process.env.PORT || 3000)
	app.run()