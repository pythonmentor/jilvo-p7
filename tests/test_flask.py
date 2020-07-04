""" V0.9--cleaning coding"""
import sys
import os

from flask_app.grandpy import req_grandpy


def test_request_google(monkeypatch):
    dico_grandpy_google = {
        'latitude': '48.85837009999999',
        'longitude': '2.2944813',
    }

    class MockRequestsGet_Google:
        def __init__(self, url, params=None):
            self.status_code = 200
            self.dict_test = {}

        def json(self):
            self.dict_test = {
                'results': [
                    {
                        'geometry': {
                            'location': {
                                'lat': '48.85837009999999',
                                'lng': '2.2944813',
                            }
                        }
                    }
                ]
            }
            return self.dict_test

    monkeypatch.setattr('requests.get', MockRequestsGet_Google)

    object_from_import_class = req_grandpy()
    dict_google = object_from_import_class.search_by_google()
    assert dict_google == dico_grandpy_google


# def test_request_wiki(monkeypatch):
#     dico_grandpy_wiki = {'pageid' : '1359783', 'title' : 'Tour Eiffel'}

#     class MockRequestsGet_Wiki:
#         def __init__(self, url, params=None):
#             self.status_code = 200
#             self.dict_test_wiki = {}
#         def json(self):
#             self.dict_test_wiki = {
#                 'query' : {
#                     'geometry' : [{
#                             'pageid' : '1359783',
#                             'title' : 'Tour Eiffel',
#                             'lat' : '48.8583',
#                             'lon' : '2.2944813'

#                     }]
#                 }
#             }
#             return self.dict_test_wiki
#     monkeypatch.setattr('requests.get', MockRequestsGet_Wiki)

#     object_from_import_class = req_grandpy()
#     dict_wiki = object_from_import_class.search_by_wiki()
#     assert dict_wiki == dico_grandpy_wiki


def test_request_wiki_bio(monkeypatch):
    dico_grandpy_wiki_bio = {"pageid": 9232, "extract": "Paris is a city"}

    class MockRequestsGet_Wiki_Bio:
        def __init__(self, url, params=None):
            self.status_code = 200
            self.dict_test_wiki_bio = {}

        def json(self):
            self.dict_test_wiki_bio = {
                "query": {
                    "pages": {
                        "9232": {"pageid": 9232, "extract": "Paris is a city"}
                    }
                }
            }
            return self.dict_test_wiki_bio

    monkeypatch.setattr('requests.get', MockRequestsGet_Wiki_Bio)

    object_from_import_class = req_grandpy()
    dict_wiki_bio = object_from_import_class.search_by_wiki_bio()
    assert dict_wiki_bio == dico_grandpy_wiki_bio

