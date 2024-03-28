#!/usr/bin/python3
"""
Fetches the value of the X-Request-Id header variable from a URL response.
"""
import sys
from urllib.request import urlopen

if __name__ == "__main__":
    url = sys.argv[1]

    with urlopen(url) as response:
        print(response.headers.get('X-Request-Id'))
