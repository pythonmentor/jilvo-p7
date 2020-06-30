""" V0.9--cleaning coding"""
import requests
import json
from flask import Flask, render_template, jsonify, make_response
from flask_cors import CORS
from flask import request as req
from parse_question import parsing
from grandpy import req_grandpy

app = Flask(__name__)
CORS(app=app)
@app.route('/')
@app.route('/index')
def index():
    return render_template('/index.html')

@app.route('/api_google/')
def req_for_api():
    objet = req_grandpy()
    objet.parse(req.args.get('user_raw_text'))
    objet.search_by_google()
    dict_return = objet.search_by_wiki()

    response = app.response_class(
                response=json.dumps(dict_return, ensure_ascii=False),
                status=200, mimetype="application/json")
    return response

if __name__ == "__main__":
    app.run(debug=False)