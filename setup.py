from flask import Flask,render_template

app = Flask(__name__)

app.config.from_pyfile('config/local.py')
from views import *
from routes import *
	
#@app.route("/user/<username>")
#def greet_user(username):
#	return "Hello "+username

if __name__ == "__main__":
	app.run(host='0.0.0.0',debug=True)
	