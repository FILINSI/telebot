from ast import While
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
import requests
import time
import datetime

def count():
    while True:
        link = "https://asset.party/get/developer/preview"
        req = Request(link, headers={'User-Agent': 'Mozilla/5.0'})
        webpage = urlopen(req).read()
        with requests.Session() as s:
            soup = BeautifulSoup(webpage, 'html5lib')
        alert = (soup.find('span', attrs={'class':'tag'}).get_text())
        time.sleep(0)
        return alert
print(count())
    