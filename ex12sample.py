import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

url = input('Enter - ')
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, "html.parser")
tags = soup('span')
numlist = list()
for tag in tags:
    content = tag.contents[0]
    content = int(content)
    numlist.append(content)
print(sum(numlist))
