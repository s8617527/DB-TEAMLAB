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
def momo_get(momourl, ps):
    sp = BeautifulSoup(ps, "lxml")
    root = 'https://www.momoshop.com.tw'
    moitn = []
    moitp = []
    moiturl = []
    try:
        name = sp.findAll("p", {'class':'prdName'})
        price = sp.findAll("span", {'class':'price'})
        t1 = sp.findAll("a", {'class':'goodsUrl'})
        for itnn in name:
            moitn.append(itnn.text)
        for itpp in price:
            moitp.append(itpp.text)
        for iturl in t1:
            t2 = root + iturl.get('href')
            moiturl.append(t2)
    except:
        moitn.append("NULL")
        moitp.append("NULL")
        moiturl.append("NULL")
    c = open("momo.csv","w", newline='', encoding='utf-8')      
    writer = csv.writer(c, delimiter=',')       
    writer.writerow(['item','price','url'])
    for item in range(0, len(moitn)):
        temp = [moitn[item], moitp[item], moiturl[item]]
        writer.writerow(temp)   
    c.close()
