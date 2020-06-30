""" V0.9--cleaning coding"""
import sys
import os
sys.path.append(f"{os.getcwd()}/flask_app/")
from grandpy import req_grandpy

def test_request_google(monkeypatch):
    dico_grandpy = {'latitude': '48.85837009999999', 'longitude': '2.2944813'}

    class MockRequestsGet:
        def __init__(self, url, params=None):
            self.status_code = 200
            self.dict_test = {}
        def json(self):
            self.dict_test = {
                'results' : [{
                    'geometry' : {
                        'location' : {
                            'lat' : '48.85837009999999',
                            'lng' : '2.2944813'
                        }
                    }
                }]
            }
            return self.dict_test
    monkeypatch.setattr('requests.get', MockRequestsGet)

    object_from_import_class = req_grandpy()
    dict_google = object_from_import_class.search_by_google()
    assert dict_google == dico_grandpy
