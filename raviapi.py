from flask import Flask
from flask import jsonify
from flask import request
from flask_cors import CORS, cross_origin
import json
import pandas as pd
import requests
from gender import gender
app = Flask(__name__)
CORS(app, support_credentials=True)
cross_origin(supports_credentials=True)
@app.route('/get_gender_list', methods=['GET'])
def get_gender_list():
	data = gender()
	return jsonify([data])
if __name__ == '__main__':
    #app.run(port=5000,debug=True)
    app.run(host="localhost",port=5000,debug=True)