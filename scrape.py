from bs4 import BeautifulSoup
import requests
import sys

def parseTextForDomain(url):
    return url.split("/")[2]

for arg in sys.argv[1:]:
    response = requests.get(arg)
    domain = parseTextForDomain(response.url)
    soup = BeautifulSoup(response.text, 'html.parser')
    title = soup.title.text 
    description = soup.find("meta", {"name":"description"})['content']
    
    print(f"Title: {title}\nDescription: {description}\nDomain: {domain}")