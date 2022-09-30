#!/usr/bin/env python3
""" Send request to alta3research-flask01.py for zodiac data """

# imports
import requests
import json
from pprint import pprint
import yaml

# URL link to zodiac api
URL = "http://127.0.0.1:2224/"

def main():

    # request to api
    resp = requests.get(URL + "/alldata")

    # convert JSON to pythonic data
    data = resp.json()

    #loop over data
    for item in data.get("zodiac_animals"):
        pprint(item)
    
if __name__ == "__main__":
    main()
