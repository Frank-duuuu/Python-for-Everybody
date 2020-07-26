# In this assignment you will write a Python program somewhat similar to http://www.py4e.com/code3/json2.py.
# The program will prompt for a URL, read the JSON data from that URL using urllib and then parse and extract the comment counts from the JSON data,
# compute the sum of the numbers in the file and enter the sum below:

import urllib.request, urllib.parse, urllib.error
import ssl
import json

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter location: ')
if len(url) < 1:
    url = 'http://py4e-data.dr-chuck.net/comments_42.json'
print('Retrieving:', url)
js = urllib.request.urlopen(url, context=ctx).read().decode()
print('Retrieved', len(js), 'characters')

info = json.loads(js)
# print(info)
counts = list()
comments = info['comments']
for item in comments:
    # print(item)
    counts.append(int(item['count']))
print('Count:', len(counts))
print('Sum:', sum(counts))
