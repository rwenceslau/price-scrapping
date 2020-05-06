import requests
import smtplib
import yaml
from bs4 import BeautifulSoup

def price_scrapper():
    URL = 'https://store.playstation.com/pt-br/product/UP9000-CUSA17357_00-MLBTHESHOW20STND?smcid=pdc%3Apt-br%3Aexplore-gamefinder%3Aprimary%2520nav%3Amsg-games%3Acomprar-jogos'
    headers = {"User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36'}

    page = requests.get(URL, headers = headers)
    soup = BeautifulSoup(page.content, 'html.parser')

    title = soup.find(class_='pdp__title').get_text()
    price = soup.find(class_='price-display__price').get_text()
    regular_price = 249.0
    converted_price = float(price[2:5])

    if (converted_price < regular_price):
        print(title, '\n',converted_price)
        send_mail(URL, title, price)
    else:
        print("Price is still at: " + price)

def send_mail(URL, title, price):

    with open("config.yml", "r") as config:
        cfg = yaml.load(config, Loader=yaml.FullLoader)

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login(cfg["username"], cfg["password"])

    subject = title + ' price fell'
    body = 'The price of ' + title + ' fell down to ' + price + '\n\n'+ '\n\n Check it out on: ' + URL
    msg = f"Subject: {subject}\n\n{body}"

    server.sendmail(
        cfg["mailfrom"],
        cfg["mailto"],
        msg
    )
    print('Mail has been sent successfully')
    server.quit()

price_scrapper()
