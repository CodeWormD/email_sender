import logging
import os
import smtplib
from email.mime.text import MIMEText

from dotenv import load_dotenv

from exceptions import LoginException, MessageSendingException
from message import msg


load_dotenv()

SENDER_EMAIL = os.getenv('MAIL_NAME')
SENDER_PASS = os.getenv('MAIL_PASS')
EMAIL_FOR = ['danich.hz@yandex.ru', 'dan.dad@bk.ru']


def email_sender():
    # логинимся под почтой отправителя
    try:
        mail = smtplib.SMTP_SSL('smtp.mail.ru')
        mail.login(SENDER_EMAIL, SENDER_PASS)
    except Exception as ex:
        logging.error(f'{ex} - check login and pass')
        raise LoginException(f'{ex} - check login and pass')

    # отправляем сообщение
    try:
        message = MIMEText(msg)
        mail.sendmail(SENDER_EMAIL, EMAIL_FOR, message.as_string())
        mail.quit()
    except Exception as ex:
        logging.error(f'{ex} - check sendmail')
        raise MessageSendingException(f'{ex} - check login and pass')


def main():
    email_sender()


if __name__ == "__main__":
    logging.basicConfig(
        filename="logs/main.log",
        filemode='a',
        format='%(levelname)s - %(asctime)s - %(message)s',
        encoding='utf-8',
        level=logging.DEBUG)
    logging.info('Started sending emails')
    main()
    logging.info('Messages were sent seccussfully!')
