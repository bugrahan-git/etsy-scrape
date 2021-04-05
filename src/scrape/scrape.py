# scrape functions

import requests
from bs4 import BeautifulSoup
import re

def scrape_url(url):
    r = requests.get(url)
    if r.status_code == requests.codes.ok:
        s = BeautifulSoup(r.text, 'html.parser')
        name = s.find('h1', attrs={"data-buy-box-listing-title": ""}).text.strip()
        price = s.find('div', attrs={"data-buy-box-region": "price"}).find('p').text.strip()
        price = re.findall('\d+\.\d+', price)[0]
        image = s.find('div', attrs={"class": "image-carousel-container"}).find('img')['src'].strip()
        return {'url': url, 'name': name, 'price': price, 'image': image}
    
    return None