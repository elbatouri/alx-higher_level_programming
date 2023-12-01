#!/usr/bin/python3
"""
Python script that takes in a URL, sends a request to the URL, and displays
the body of the response (decoded in utf-8). It manages urllib.error.HTTPError
exceptions and prints the error code in case of an HTTP error.
"""

import urllib.request
import urllib.error
import sys

if __name__ == "__main__":
    try:
        with urllib.request.urlopen(sys.argv[1]) as response:
            body = response.read()
            print(body.decode('utf-8'))
    except urllib.error.HTTPError as err:
        print('Error code: {}'.format(err.code))
