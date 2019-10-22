from flask import Flask, request
import os
import requests

class followerKeyVal:

    def get(self, request, key_name):
        # print('before try')
        try:
            # print('in try')
            response = requests.get('http://'+ os.environ['FORWARDING_ADDRESS'] + '/kv-store/' + key_name, data=request.form, headers=dict(request.headers), timeout=20)
            # print('test text ')
            # print(response)
        except requests.Timeout:
            return 'Timed out!'
        else:
            return response.content, response.status_code

    def put(self, request, key_name):
        try:
            response = requests.put('http://'+ os.environ['FORWARDING_ADDRESS'] + '/kv-store/' + key_name, data=request.form, headers=dict(request.headers), timeout=20)
        except requests.Timeout:
            return 'Timed out!'
        else:
            return response.content, response.status_code
    def delete(self, request, key_name):
        try:
            response = requests.delete('http://'+ os.environ['FORWARDING_ADDRESS'] + '/kv-store/' + key_name, data=request.form, headers=dict(request.headers), timeout=20)
        except requests.Timeout:
            return 'Timed out!'
        else:
            return response.content, response.status_code