#!/usr/bin/python3
""" a script that will :
    - sends a request to the URL and displays the value of the X-Request-Id
    - use the packages urllib and sys
    - use a with statement

    """
import urllib.request
import sys

if __name__ == "__main__":
    with urllib.request.urlopen(sys.argv[1]) as response:
        content = response.info()
        print(content.get("X-Request-Id"))
