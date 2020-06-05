from flask import Flask,render_template,jsonify,make_response
from flask_cors import CORS
from flask import request as req
import requests
import json
from parse_question import parsing

app = Flask(__name__)
CORS(app=app)
@app.route('/')
@app.route('/index')
def index():
    return render_template('/index.html')

@app.route('/map')
def map():
    return render_template('/Untitled-1.html')

@app.route('/api_google/')
def grandpy():
    user_raw_text = req.args.get('user_raw_text')
    list_question = parsing(user_raw_text)
    adress = "+".join(list_question)
    return_data = requests.get("https://maps.googleapis.com/maps/api/geocode/json?address="+ adress +",&key=AIzaSyAKfLjoRy19P25S1KUOorpwBJ-psQ5oRg4")
    return_data = return_data.json()
    for geometry in return_data["results"]:
        if geometry.get("geometry",False):
            # print(geometry["geometry"])
            dict_lat_lng={}
            dict_lat_lng=geometry["geometry"]
            latitude = dict_lat_lng['location']["lat"]
            longitude = dict_lat_lng['location']["lng"]
            dict_return={}
            dict_return["latitude"] = latitude
            dict_return["longitude"] = longitude
            print(dict_return)
            
    response = app.response_class(
        response=json.dumps(dict_return, ensure_ascii=False), status=200, mimetype="application/json"
    )
    return response

if __name__ == "__main__":
    app.run(debug=False)