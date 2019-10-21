from flask import Flask, request, render_template, jsonify
import os
import sys
from mainKeyVal import mainKeyVal

app = Flask(__name__)

@app.route("/")
def begin():
	return "welcome to the home page"

@app.route("/kv-store/<string:key_name>", methods = ["GET","PUT", "DELETE"])
def keyValStore(key_name):
	if request.method == "PUT":
		#print("__")
		#print(request)
		#print("__")
		return server.put(request, key_name)
	elif request.method == "GET": 
		return "This method is unsupported.", 405
	elif request.method == "DELETE":
		return ""






if __name__ == "__main__":
	server = mainKeyVal()
	app.run(debug=True, host = '0.0.0.0', port = 13800)