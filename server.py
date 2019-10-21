# CSE 138 Assignment 1
# Author: Adit Bhagat (adbhagat@ucsc.edu)

from flask import Flask, request
import os
import requests

app = Flask(__name__)

@app.route('/check', methods=["GET", "POST"])
def check():
    if request.method == "POST":
        msg = request.args.get('msg')
        if msg is not None:
            return 'POST message received: %s' % msg
        else:
            return 'This method is unsupported.', 405
    else:
        if 'FORWARDING_ADDRESS' in os.environ:
            try:
                response = requests.get('http://'+ os.environ['FORWARDING_ADDRESS'] + '/check', timeout=20)
            except requests.Timeout:
                return 'Timed out!'
            else:
                return 'ASDF Request made: %s' % response.content
        else:
            return 'GET message received'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=13800)