from flask import Flask, request, jsonify
import os
import requests
import json

class followerKeyVal:

    def get(self, request, key_name):
        try:
            reqdata = request.get_json(silent=True)
            if reqdata is not None:
                response = requests.get('http://'+ os.environ['FORWARDING_ADDRESS'] + '/kv-store/' + key_name, data=json.dumps(reqdata), headers=dict(request.headers), timeout=20)
            else:
                response = requests.get('http://'+ os.environ['FORWARDING_ADDRESS'] + '/kv-store/' + key_name, headers=dict(request.headers), timeout=20)
        except (requests.Timeout, requests.exceptions.ConnectionError):
            return jsonify({'error': 'Main instance is down', 'message': 'Error in GET'}), 503
        else:
            return response.content, response.status_code

    def put(self, request, key_name):
        try:
            reqdata = request.get_json(silent=True)
            if reqdata is not None:
                print(reqdata)
                print(type(reqdata))
                response = requests.put('http://'+ os.environ['FORWARDING_ADDRESS'] + '/kv-store/' + key_name, data=json.dumps(reqdata), headers=dict(request.headers), timeout=20)
                print("Reqdata done")
            else:
                response = requests.put('http://'+ os.environ['FORWARDING_ADDRESS'] + '/kv-store/' + key_name, headers=dict(request.headers), timeout=20)
        except:
            return jsonify({'error': 'Main instance is down', 'message': 'Error in PUT'}), 503
        else:
            return response.content, response.status_code

    def delete(self, request, key_name):
        try:
            reqdata = request.get_json(silent=True)
            if reqdata is not None:
                response = requests.delete('http://'+ os.environ['FORWARDING_ADDRESS'] + '/kv-store/' + key_name, data=json.dumps(reqdata), headers=dict(request.headers), timeout=20)
            else:
                response = requests.delete('http://'+ os.environ['FORWARDING_ADDRESS'] + '/kv-store/' + key_name, headers=dict(request.headers), timeout=20)
        except:
            return jsonify({'error': 'Main instance is down', 'message': 'Error in DELETE'}), 503
        else:
            return response.content, response.status_code