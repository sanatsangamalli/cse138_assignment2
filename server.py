from flask import Flask, request, render_template, jsonify
import os
import sys
from mainKeyVal import mainKeyVal
from followerKeyVal import followerKeyVal

app = Flask(__name__)

@app.route("/")
def begin():
    return "welcome to the home page"

@app.route("/kv-store/<string:key_name>", methods = ["GET","PUT", "DELETE"])
def keyValStore(key_name):
    if request.method == "PUT":
        return server.put(request, key_name)
    elif request.method == "GET":
        return server.get(request, key_name)
    elif request.method == "DELETE":
        return server.delete(request, key_name)






if __name__ == "__main__":
    if 'FORWARDING_ADDRESS' not in os.environ:
        server = mainKeyVal()
    else:
        server = followerKeyVal()
    app.run(debug=True, host = '0.0.0.0', port = 13800)