#!/usr/bin/python3
"""
Sends a POST request to http://0.0.0.0:5000/search_user with a given letter.
Usage: ./8-json_api.py <letter>
  - The letter is sent as the value of the variable `q`.
  - If no letter is provided, sends `q=""`.
"""
import sys
import requests


if __name__ == "__main__":
    letter = "" if len(sys.argv) == 1 else sys.argv[1]
    payload = {"q": letter}

    url = "http://0.0.0.0:5000/search_user"
    r = requests.post(url, data=payload)

    try:
        response = r.json()
        if response:
            print("[{}] {}".format(response.get("id"), response.get("name")))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
