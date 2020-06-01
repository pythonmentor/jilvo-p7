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
            print('lat is' + str(lat) + 'lng is' + str(lng))
        # for location in geometry["geometry"]:
        #     if location.get("location",False):
        #         print(location["lat"])

    # print(return_data)
    # print(return_data["results"])

test_OK_google_places()
    