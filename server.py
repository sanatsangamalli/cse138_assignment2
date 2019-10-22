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
    # print("helloss")
    if request.method == "PUT":
        return server.put(request, key_name)
    elif request.method == "GET":
        return server.get(request, key_name)
    elif request.method == "DELETE":
        return server.delete(request, key_name)






if __name__ == "__main__":
<<<<<<< HEAD
    if 'FORWARDING_ADDRESS' not in os.environ:
        server = mainKeyVal()
    else:
        server = followerKeyVal()
    app.run(debug=True, host = '0.0.0.0', port = 13800)
=======
    # print('server.py main')
    if 'FORWARDING_ADDRESS' not in os.environ:
       server = mainKeyVal()
       # p = 13800
       # print('no FORWARDING_ADDRESS')
       app.run(debug=True, host = '0.0.0.0', port = 13800)
    else:
       server = followerKeyVal()
       # p = 13801
       # print('FORWARDING_ADDRESS')
       app.run(debug=True, host = '0.0.0.0', port = 13801)
    
>>>>>>> 26b2d4e686b2f0d72068a2d7374872c98c636cbf
