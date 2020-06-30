""" V0.9--cleaning coding"""
import requests
import json
from parse_question import parsing
class req_grandpy:
        def __init__(self):
            self.dict_return = {}
            self.adress = ""

        def parse(self,user_raw_text):
            list_question = parsing(user_raw_text)
            self.adress = "+".join(list_question)

        def search_by_google(self):
            return_data = requests.get("https://maps.googleapis.com/maps/api/geocode/json?address="+ self.adress +",&key=AIzaSyAKfLjoRy19P25S1KUOorpwBJ-psQ5oRg4")
            return_data = return_data.json()
            for geometry in return_data["results"]:
                if geometry.get("geometry",False):
                    # print(geometry["geometry"])
                    dict_lat_lng={}
                    dict_lat_lng=geometry["geometry"]
                    latitude = dict_lat_lng['location']["lat"]
                    longitude = dict_lat_lng['location']["lng"]
                    self.dict_return["latitude"] = latitude
                    self.dict_return["longitude"] = longitude
                    return self.dict_return

        def search_by_wiki(self):
            dict_return_wiki = self.dict_return
            wiki_place = requests.get("https://fr.wikipedia.org/w/api.php?action=query&list=geosearch&gscoord=" + str(self.dict_return["latitude"]) + "%7C" + str(self.dict_return["longitude"]) + "&gsradius=10000&gslimit=10&format=json")
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
            print(pageid)
            print(right_place)
            wiki_information = requests.get("https://fr.wikipedia.org/w/api.php?action=query&origin=*&prop=extracts&explaintext&format=json&titles=" + right_place +"")
            wiki_information = wiki_information.json()
            query = wiki_information["query"]
            pages = query["pages"]
            page_id = pages[str(pageid)]
            extract = page_id["extract"]
            dict_return_wiki["extract"] = extract[0:500]
            dict_return_wiki["pageid"] = pageid
            return dict_return_wiki
    