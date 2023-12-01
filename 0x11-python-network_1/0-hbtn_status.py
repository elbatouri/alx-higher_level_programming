#!/usr/bin/python3
"""
this script will:
    - fetches https://alx-intranet.hbtn.io/status
    - use the package urllib
    - use a with statement
"""
import urllib.request

if __name__ == '__main__':
    with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as response:
        body_content = response.read()
        print("Body response:")
        print("\t- type: {}".format(type(body_content)))
        print("\t- content: {}".format(body_content))
        print("\t- utf8 content: {}".format(body_content.decode('utf-8')))
