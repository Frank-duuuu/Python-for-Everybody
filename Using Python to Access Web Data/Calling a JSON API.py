# In this assignment you will write a Python program somewhat similar to http://www.py4e.com/code3/geojson.py.
# The program will prompt for a location, contact a web service and retrieve JSON for the web service and parse that data,
# and retrieve the first place_id from the JSON.
# A place ID is a textual identifier that uniquely identifies a place as within Google Maps.

import urllib.request, urllib.parse, urllib.error
import json
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
serviceurl = 'http://py4e-data.dr-chuck.net/json?'

while True:
    address = input('Enter location: ')
    if len(address) < 1: break
    parms = dict()
    parms['address'] = address
    parms['key'] = 42
    url = serviceurl+urllib.parse.urlencode(parms)
    print('Retrieving', url)
    js = urllib.request.urlopen(url).read().decode()
    print('Retrieved', len(js), 'characters')
    # print(js)
    info = json.loads(js)
    # print(info)
    results = (info['results'][0]['place_id'])
    print(results)
