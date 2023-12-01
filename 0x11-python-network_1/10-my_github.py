#!/usr/bin/python3
"""
Python script that sends a search request to the
github API, searching people
"""
import requests
import sys
from request.auth import HTTPBasicAuth

if __name__ == "__main__":
    auth = HTTPBasicAuth(sys.argv[1], sys.argv[2])
    reques = requests.get("https://api.github.com/user", auth=auth)
    print(reques.json().get("id"))
