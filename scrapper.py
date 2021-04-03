import requests
from bs4 import BeautifulSoup

class PriceScrapper:
    url = ''
    headers = {"User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36'}

    def __init__(self, url):
        self.url = url
    
    def load_page(self):
        page = requests.get(self.url, self.headers)
        return (BeautifulSoup(page.content, 'html.parser'))
        