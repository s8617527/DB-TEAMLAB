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

main = input("搜尋關鍵字")
momo1 = 'https://www.momoshop.com.tw/search/searchShop.jsp?keyword='
momourl = momo1 + main
pchome1 = 'https://ecshweb.pchome.com.tw/search/v3.3/?q='
pchomeurl = pchome1 + main
yahoo1 = 'https://tw.search.mall.yahoo.com/search/mall/product?p='
yahoourl = yahoo1 + main
shp1 = 'https://shopee.tw/search/?keyword='
shp2 = '&order=asc&page=0&sortBy=price'
shpurl = shp1 + main + shp2

print("momo: ", momourl)
chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
driver = webdriver.Chrome(options=chrome_options)
driver.get(momourl)

ps = driver.page_source
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
print(len(moitn), " ", len(moitp), " ", len(moiturl))
for item in range(0, len(moiturl)):
    print(moiturl[item])
##pc_get(pchomeurl)
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
for item in range(0, len(spitems)):
    print(spurls[item])
print("yahoo: ", yahoourl)
driver.get(yahoourl)
ps = driver.page_source
sp = BeautifulSoup(ps, "lxml")
yaitn = []
yaitp = []
yaiturl = []
try:
    name = sp.find("div",{'class':'main'}).findAll("span", class_ = re.compile('2HWui'))
    price = sp.findAll(class_ = re.compile('31jkj'))
    url = sp.findAll("a", class_ = re.compile('3LORP'))
    print(len(url))
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
print(len(yaitn), " ", len(yaitp), " ", len(yaiturl))
for item in range(0, len(yaiturl)):
    print(yaiturl[item])