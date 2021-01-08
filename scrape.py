import requests
from bs4 import BeautifulSoup

def scrape(url):
    url = "url"
    page = requests.get(url)

    soup = BeautifulSoup(page.content, 'html.parser')


