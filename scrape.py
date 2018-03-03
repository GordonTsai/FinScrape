import xlwings as xw
from bs4 import BeautifulSoup
import requests


def process():
    url = "https://www.gurufocus.com/financials/AMZN.html"
    page = requests.get(url)
    # add if page.status_code ==200 it works or jsut starts with 2
    # codes that begin with 2 generally indicate success and 4 or 5 doesn't
    soup=BeautifulSoup(page.text, 'html.parser')
    output=soup.prettify()


    wb = xw.Book.caller('scrape.xlsm')
    wb.sheets[0].range("A1").value = output
    wb.sheets[0].range("eps").value = 5

process()
