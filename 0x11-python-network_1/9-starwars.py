#!/usr/bin/python3
"""
Python script that sends a search request to the
github API, searching people
"""
import requests
import sys

if __name__ == "__main__":
    search_term = sys.argv[1] if len(sys.argv) > 1 else ""
    search_url = 'https://swapi.co/api/people/?search={}'.format(search_term)
    
    response = requests.get(search_url)
    json_data = response.json()

    print("Number of results: {}".format(json_data.get('count')))
    for character in json_data.get('results'):
        print(character.get('name'))
