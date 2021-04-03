import logging
from mailsender import MailSender
from scrapper import PriceScrapper

def price_scrapper():

    URL = 'https://www.vans.com.br/sapatos/tenis/tenis-old-skool/p/1002001070011U'
    price_scrapper = PriceScrapper(URL)
    soup = price_scrapper.load_page()

    title = soup.find(class_='product-title lighter').get_text()
    price = soup.find(class_='product-cash-price').get_text()
    #size = soup.find(id_='variant-size-41').get('value').get_text()

    regular_price = 339.0
    converted_price = float(price[2:5])

    if (converted_price < regular_price):
        logging.info(title, '\n', 'R$', converted_price)
        MailSender.send_mail(MailSender, URL, title, price)
    else:
        print("Price is still at: " + price)


price_scrapper()
