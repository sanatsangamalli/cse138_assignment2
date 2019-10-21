from flask import Flask, request, render_template, jsonify
import os
import sys

class mainKeyVal:

	def __init__(self):
		self.dictionary = {}

	def get(self, request, key_name):
		if key_name in self.dictionary:
			return jsonify({"doesExist":True, "message":"Retrieved successfully", "value":self.dictionary[key_name]}), 200
		else:
			return jsonify({"doesExist":False, "error:":"Key does not exist", "message":"Error in GET"}), 404
		
	def put(self, request, key_name):
		if len(key_name) > 50:
			return jsonify({"error:":"Key is too long", "message":"Error in PUT"}), 400
		req_data = request.get_json()
		if 'value' in req_data:
			data = req_data['value']
			replaced = key_name in self.dictionary
			self.dictionary[key_name] = data	
			
			if replaced:
				message = "Updated successfully"
				code = 200
			else:
				message = "Added successfully"
				code = 201
				
			return jsonify({"message":message, "replaced":replaced}), code
			
		else:
			return jsonify({"error:":"Value is missing", "message":"Error in PUT"}), 400
			
	def delete(self, request, key_name):
		if key_name in self.dictionary:
			del self.dictionary[key_name]
			return jsonify({"doesExist":True, "message":"Deleted successfully"}), 200
		else:
			return jsonify({"doesExist":False, "error:":"Key does not exist", "message":"Error in DELETE"}), 404