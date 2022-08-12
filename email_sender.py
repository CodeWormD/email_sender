import os
import smtplib
from dotenv import load_dotenv
from email.mime.text import MIMEText
from message import msg

load_dotenv()

SENDER_EMAIL = os.getenv('MAIL_NAME')
SENDER_PASS = os.getenv('MAIL_PASS')
EMAIL_FOR = ['danich.hz@yandex.ru', 'dan.dad@bk.ru']


def email_sender():
    try:
        mail = smtplib.SMTP_SSL('smtp.mail.ru')
        mail.login(SENDER_EMAIL, SENDER_PASS)
        
        message = MIMEText(msg)
        mail.sendmail(SENDER_EMAIL, EMAIL_FOR, message.as_string())
        
        print('Messages were sent seccussfully!')
        mail.quit()
        
    except Exception as ex:
        return f'{ex} - check login and pass'



def main():
    email_sender()

if __name__ == "__main__":
    main()
