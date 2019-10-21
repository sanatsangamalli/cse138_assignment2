from flask import Flask, request, render_template, jsonify
import os
import sys

class mainKeyVal:

	def _init__():
		self.dictionary = {}

	def get(self, request, key_name):
		if key_name in self.dictionary:
			return jsonify({"doesExist":true, "message":"Retrieved successfully", "value":self.dictionary[key_name]}), 200
		else:
			return jsonify({"doesExist":false, "error:":"Key does not exist", "message":"Error in GET"}), 404
		
	def put(self, request, key_name):
		if len(key_name) > 50:
			return jsonify({"error:":"Key is too long", "message":"Error in PUT"}), 400
		req_data = request.get_json()
		if 'value' in req_data:
			data = req_data['value']
			replaced = key_name in self.dictionary
			self.dictionary[key_name] = data	
			return jsonify({"message":"Added successfully", "replaced":replaced}), 201
			
		else:
			return jsonify({"error:":"Value is missing", "message":"Error in PUT"}), 400
			
	def delete(self, request, key_name):
		if key_name in self.dictionary:
			del self.dictionary[key_name]
			return jsonify({"doesExist":true, "message":"Deleted successfully"}), 200
		else:
			return jsonify({"doesExist":false, "error:":"Key does not exist", "message":"Error in DELETE"}), 404