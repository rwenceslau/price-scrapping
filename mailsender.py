import logging
import smtplib
import yaml

class MailSender:
    hostname = 'smtp.gmail.com'
    port = 465
    configfile = 'config.yml'

    def send_mail(self, URL, title, price):

        with open(self.configfile, "r") as config:
            cfg = yaml.load(config, Loader=yaml.FullLoader)

        server = smtplib.SMTP(self.hostname, self.port)
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
        logging.info('Mail has been sent successfully.')
        server.quit()