from bs4 import BeautifulSoup
import requests
import sys

def extractFromTag(tag, tagName):
    extraction = tag.split(tagName)
    print(extraction)

for arg in sys.argv[1:]:
    response = requests.get(arg)
    soup = BeautifulSoup(response.text, 'html.parser')
    print(soup.title.text)