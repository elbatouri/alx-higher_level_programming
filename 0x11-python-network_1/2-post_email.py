#!/usr/bin/python3
"""
this script will :
- takes in a URL and an email
- sends a POST request to the passed URL
- displays the body of the response (decoded in utf-8)
- use the with statement
 """
import urllib.request
import urllib.parse
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    data = urllib.parse.urlencode({'email': email}).encode('utf-8')
    with urllib.request.urlopen(url, data=data) as response:
        body = response.read().decode('utf-8')
        print(body)
