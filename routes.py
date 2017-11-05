from setup import app
from flask import request,jsonify
from pymongo import MongoClient
import json
from bson.objectid import ObjectId

Client = MongoClient(app.config['MONGO_URI'])
DB = Client[app.config['MONGO_DBNAME']]

@app.route("/static/rule",methods=['GET'])
def getStaticsRule():
	collection = DB['static']
	rule = collection.find_one({'page':'rule page'})
	rule['_id']=str(rule['_id'])
	return jsonify(rule)
	
@app.route("/static/upload",methods=['GET'])
def getStaticsUpload():
	collection = DB['static']
	rule = collection.find_one({'page':'upload log'})
	rule['_id']=str(rule['_id'])
	return jsonify(rule)
	
@app.route("/static/cdet",methods=['GET'])
def getStaticsCdet():
	collection = DB['static']
	rule = collection.find_one({'page':'user cdet'})
	rule['_id']=str(rule['_id'])
	return jsonify(rule)

@app.route("/rules/<rule_id>",methods=['GET'])
def route_rule(rule_id):
	collection = DB['rule']
	rule = collection.find_one({'_id':ObjectId(rule_id)})
	rule['_id']=str(rule['_id'])
	return jsonify(rule)
	
	
@app.route("/rules/add",methods=['POST'])
def add_rule():
	data = request.get_json()
	collection = DB['rule']
	collection.insert(data)
	data['_id']=str(data['_id'])
	return jsonify(data)
	
	
@app.route("/result/testcases",methods=['POST'])
def getTestCases():
	#apply_ml()
	response = app.response_class(
		response = 'working',
		status = 200
	)
	return response