from cgitb import html
from email.header import Header
from gettext import gettext
from http import server
from nturl2path import url2pathname
from turtle import title
import requests
from bs4 import BeautifulSoup
import smtplib

URL = """product url"""

headers = {
    """user agent"""
}

def price_check(URL, max_price):

    page = requests.get( URL, headers = headers)  

    soup = BeautifulSoup(page.content, 'html.parser')

    title = soup.find(id = "productTitle").getText().strip()

    price = soup.find(id = "priceblock_ourprice").getText().strip()

    new_price = float(price[1: -1].replace(",","."))


    if(new_price <= new_price):
        send_email("mail_address@yahoo.com", URL)


def send_email(toMail, url):
    server= smtplib.SMTP("smtp.yahoo.com",587)
    
    server.ehlo()
    
    server.starttls
    
    server.ehlo
    
    server.login("test")
    
    
    subject = "Down Price"
    
    body = "Connection Link" + url
    
    msg = f'Subject: {subject}\n\n{body}'
    
    server.sendmail(
        "mail_address@yahoo.com", 
        msg
    )
    
    print("Done")
    
    server.quit()
    
    price_check(url,300)