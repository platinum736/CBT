from setup import app
from flask import render_template,request

@app.route("/login",methods=['GET'])
def home_page():
	return render_template("login.html")

@app.route("/check_login",methods=['POST'])
def checkLogin():
	userType = request.form.get('utype')
	if(userType == 'cadmin' or userType == 'ncadmin'):
		return render_template("admin_login.html")
	else:
		return render_template("user_login.html")
		
	return render_template("user_login.html")
	
@app.route("/header",methods=['GET'])
def load_header():
	return render_template("header.html")
	
@app.route("/create_rule",methods=['GET'])
def load_createRule():
	return render_template("create_rule.html")
	
@app.route("/admin_login",methods=['GET'])
def load_adminlogin():
	return render_template("admin_login.html")