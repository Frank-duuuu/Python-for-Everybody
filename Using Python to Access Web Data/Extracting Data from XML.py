# In this assignment you will write a Python program somewhat similar to http://www.py4e.com/code3/geoxml.py.
# The program will prompt for a URL,
#   read the XML data from that URL using urllib and then parse and extract the comment counts from the XML data,
#   compute the sum of the numbers in the file.

import urllib.request, urllib.parse, urllib.error
import ssl
import xml.etree.ElementTree as ET

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
if len(url) < 1:
    url = 'http://py4e-data.dr-chuck.net/comments_722229.xml'
xml = urllib.request.urlopen(url, context=ctx).read().decode()
# print(xml)
counts = list()
tree = ET.fromstring(xml)
comments = tree.findall('comments/comment')

for item in comments:
    count = item.find('count').text
    counts.append(int(count))
print(sum(counts))
