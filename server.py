from flask import Flask, request, render_template, jsonify
import os
import socket
import sys

app = Flask(__name__)

@app.route("/")
def begin():
    return "welcome to the home page"

@app.route("/kv-store/<string:key_name>", methods = ["GET","PUT", "DELETE"])
def keyValStore(key_name):
    if request.method == "PUT": 
        try:
            req_data = request.get_json()
            data = req_data['data']
			if len(key_name) > 50:
				return jsonify({"error:":"Key is too long", "message":"Error in PUT"}), 400
		except Exception as e:
			return jsonify({"error:":"Value is missing", "message":"Error in PUT"}), 400
    elif request.method == "GET": 
        return "This method is unsupported.", 405
    elif request.method == "DELETE":






















if __name__ == "__main__":
    app.run(debug=True, host = '0.0.0.0', port = 13800)