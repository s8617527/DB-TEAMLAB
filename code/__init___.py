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
from momo_get import *
from yahoo_get import *
from shopee_get import *

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
momo_get(momourl, ps)
driver.get(yahoourl)
ps = driver.page_source
yahoo_get(yahoourl, ps)
shp_get(shpurl)
