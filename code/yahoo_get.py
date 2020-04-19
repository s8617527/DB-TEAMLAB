from urllib import request
from bs4 import BeautifulSoup
from urllib.parse import urlparse
from urllib.request import urlopen
import re
import sqlite3
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import json
import requests
from fake_useragent import UserAgent
from lxml import html
import csv
def yahoo_get(yahoourl, ps):
    print("yahoo: ", yahoourl)
    sp = BeautifulSoup(ps, "lxml")
    yaitn = []
    yaitp = []
    yaiturl = []
    try:
        name = sp.find("div",{'class':'main'}).findAll("span", class_ = re.compile('2HWui'))
        price = sp.findAll(class_ = re.compile('31jkj'))
        url = sp.findAll("a", class_ = re.compile('3LORP'))
        for itnn in name:
            yaitn.append(itnn.text)
        for itpp in price:
            yaitp.append(itpp.text)
        for iturl in url:
            t1 = iturl.get('href')
            yaiturl.append(t1)
    except:
        yaitn.append("NULL")
        yaitp.append("NULL")
        yaiturl.append("NULL")
    c = open("yahoo.csv","w", newline='', encoding='utf-8')      
    writer = csv.writer(c, delimiter=',')       
    writer.writerow(['item','price','url'])
    for item in range(0, len(yaitn)):
        temp = [yaitn[item], yaitp[item], yaiturl[item]]
        writer.writerow(temp)
    c.close()