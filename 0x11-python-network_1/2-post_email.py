#!/usr/bin/python3
""" this script will :
    - takes in a URL and an email
    - sends a POST request to the passed URL
    - displays the body of the response (decoded in utf-8)
    - use the with statement
    
    """

from urllib import request, parse
import sys

if __name__ == "__main__":
    link = sys.argv[1]
    val = {'email': sys.argv[2]}
    data = parse.urlencode(val)
    Req = request.Request(link, data)
    with request.urlopen(Req) as response:
        print(response.read().decode('utf-8'))
