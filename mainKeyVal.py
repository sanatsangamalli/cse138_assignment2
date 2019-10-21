from flask import Flask, request, render_template, jsonify
import os
import sys

class mainKeyVal:

	def _init__():
		self.dict = {}

	def get(self, request):
		return "This method is unsupported.", 405
		
	def put(self, request, key_name):
		#print(key_name)
		#print(request.data)
		if len(key_name) > 50:
			return jsonify({"error:":"Key is too long", "message":"Error in PUT"}), 400
		req_data = request.get_json()
		if 'value' in req_data:
			data = req_data['value']
			#add to dict
		else:
			return jsonify({"error:":"Value is missing", "message":"Error in PUT"}), 400
			
	def delete(self, request):
		return 405