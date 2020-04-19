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
def shp_get(shpurl):
    print("蝦皮: ", shpurl)
    headers = {
        'User-Agent': 'Googlebot'
    }
    r = requests.get(shpurl,headers=headers,allow_redirects=True)
    sp = BeautifulSoup(r.text, "lxml")
    root = 'https://shopee.tw'
    try:
        name = sp.find_all("div", class_="_1NoI8_ _16BAGk")
        p1 = sp.find_all("div", class_="_2lBkmX")
        links = sp.findAll("a", {'data-sqe':'link'})
        spitems = []
        spprices = []
        spurls = []
        for itnn in name:
            spitems.append(itnn.text)
            ##print(itnn.text)
        for itpp in p1:
            p2 = itpp.find(class_ = '_341bF0')
            spprices.append(p2.text)
        for iturl in links:
            t1 = root + iturl.get('href')
            spurls.append(t1)
    except:
        spitems.append("NULL")
        spprices.append("NULL")
        spurls.append("NULL")
    c = open("shopee.csv","w", newline='', encoding='utf-8')      
    writer = csv.writer(c, delimiter=',')       
    writer.writerow(['item','price','url'])
    for item in range(0, len(spitems)):
        temp = [spitems[item], spprices[item], spurls[item]]
        writer.writerow(temp)
    c.close()
