import requests
import json

def test_OK_google_places():
    """Test if the function returns a dict with the needed values."""
    return_data = requests.get("https://maps.googleapis.com/maps/api/geocode/json?address=tour+eiffel,&key=AIzaSyAKfLjoRy19P25S1KUOorpwBJ-psQ5oRg4")
    return_data = return_data.json()
    for geometry in return_data["results"]:
        if geometry.get("geometry",False):
            # print(geometry["geometry"])
            dico={}
            dico=geometry["geometry"]
            lat = dico['location']["lat"]
            lng = dico['location']["lng"]
            print('lat is ' + str(lat) + 'lng is ' + str(lng))
        # for location in geometry["geometry"]:
        #     if location.get("location",False):
        #         print(location["lat"])

    # print(return_data)
    # print(return_data["results"])

# test_OK_google_places():
def wiki():
    latitude = 48.85837009999999
    longitude = 2.2944813
    wiki_place = requests.get("https://en.wikipedia.org/w/api.php?action=query&list=geosearch&gscoord=" + str(latitude) + "%7C" + str(longitude) + "&gsradius=10000&gslimit=10&format=json")
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
    wiki_information = requests.get("https://en.wikipedia.org/w/api.php?action=query&origin=*&prop=extracts&explaintext&format=json&titles=" + right_place +"")
    wiki_information = wiki_information.json()
    query = wiki_information["query"]
    pages = query["pages"]
    page_id = pages[str(pageid)]
    extract = page_id["extract"]
    # dict_return["extract"] = extract

wiki()
    