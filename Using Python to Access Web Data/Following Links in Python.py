# In this assignment you will write a Python program that expands on http://www.py4e.com/code3/urllinks.py.
# The program will use urllib to read the HTML from the data files below,
#   extract the href= vaues from the anchor tags,
#   scan for a tag that is in a particular position relative to the first name in the list,
#   follow that link and repeat the process a number of times and report the last name you find.

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
position = int(input('Enter position:')) - 1
count = int(input('Enter count:'))
if len(url) < 1:
    url = 'http://py4e-data.dr-chuck.net/known_by_Sukhmani.html'


def scrap(position, count):
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')

    lines = list()
    tags = soup('a')
    for tag in tags:
        lines.append(tag.get('href', None))

    for i in range(count - 1):
        html = urllib.request.urlopen(lines[position], context=ctx).read()
        soup = BeautifulSoup(html, 'html.parser')
        lines = list()
        tags = soup('a')
        for tag in tags:
            lines.append(tag.get('href', None))
    print(lines[position])


scrap(position, count)
