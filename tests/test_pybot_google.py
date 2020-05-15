import pytest
import requests
import json

def test_OK_google_places():
    """Test if the function returns a dict with the needed values."""
    def json():
        """Return a fake json result from request."""
        location = {"lat": 20, "lng": 30}
        geometry = {"location": location}
        candidates = [{"formatted_address": "champ de Mars",
                       "geometry": geometry,
                       "name": "Tour Eiffel"}]
        response = {"candidates": candidates, "status": "OK"}
        return response

    