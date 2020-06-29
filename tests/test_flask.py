import sys
import os
sys.path.append(f"{os.getcwd()}/flask_app/")
from grandpy import req_grandpy

object_for_test = req_grandpy()

def test_request_google(monkeypatch):
    dico_grandpy = {'latitude': '48.85837009999999', 'longitude': '2.2944813'}

    class MockRequestsGet:
        def __init__(self, url, params=None):
            self.status_code = 200
        def json(self):
            test_list = ["latitude","longitude"]
            test_dict = {}
            test_dict["latitude"]= '48.85837009999999'
            test_dict["longitude"]= '2.2944813'


            return test_dict
            # {
            #     {'latitude': '48.85837009999999', 'longitude': '2.2944813'}
            #     }

    monkeypatch.setattr('requests.get', MockRequestsGet)
    
    assert object_for_test.search_by_google() == dico_grandpy

# def test_request_wiki(monkeypatch):