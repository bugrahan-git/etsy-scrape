# scrape functions

import requests
from bs4 import BeautifulSoup

def scrape_url(url):
    r = requests.get(url)
    if r.status_code == requests.codes.ok:
        s = BeautifulSoup(r.text, 'html.parser')
        return None
    
    return None