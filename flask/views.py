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
    
    wiki_place = requests.get("https://fr.wikipedia.org/w/api.php?action=query&list=geosearch&gscoord=" + str(latitude) + "%7C" + str(longitude) + "&gsradius=10000&gslimit=10&format=json")
    wiki_place = wiki_place.json()
    geosearch = {}
    geosearch = wiki_place["query"]
    place={}
    title={}
    i=0
    for info_place in geosearch["geosearch"]:
        i+=1
        if info_place.get("title",False):
            place[i] = info_place
            title[place[i]["title"]]=info_place
    right_place = place[1]["title"]
    pageid = place[1]["pageid"] 
    print(right_place)
    wiki_information = requests.get("https://fr.wikipedia.org/w/api.php?action=query&origin=*&prop=extracts&explaintext&format=json&titles=" + right_place +"")
    wiki_information = wiki_information.json()
    query = wiki_information["query"]
    pages = query["pages"]
    page_id = pages[str(pageid)]
    extract = page_id["extract"]
    dict_return["extract"] = extract
    
    response = app.response_class(
        response=json.dumps(dict_return, ensure_ascii=False), status=200, mimetype="application/json"
    )
    return response

if __name__ == "__main__":
    app.run(debug=False)