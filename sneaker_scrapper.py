import requests
from bs4 import BeautifulSoup

def price_scrapper():
    URL = 'https://www.vans.com.br/sapatos/tenis/tenis-old-skool/p/1002001070011U'
    headers = {"User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36'}

    page = requests.get(URL, headers = headers)
    soup = BeautifulSoup(page.content, 'html.parser')

    title = soup.find(class_='product-title lighter').get_text()
    price = soup.find(class_='product-cash-price').get_text()
    #size = soup.find(id_='variant-size-41').get('value').get_text()

    regular_price = 329.0
    converted_price = float(price[2:5])

    if (converted_price < regular_price):
        print(title, '\n', 'R$', converted_price)
    else:
        print("Price is still at: " + price)


price_scrapper()
