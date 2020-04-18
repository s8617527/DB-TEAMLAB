"""
def pc_get(pchomeurl):
    print("pchome: ", pchomeurl)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.113 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest',
        'accept' : 'pplication/json, text/javascript, */*; q=0.01'
    }
    r = requests.get(pchomeurl,headers=headers,allow_redirects=True)
    sp = BeautifulSoup(r.text, "lxml")
    print(sp.findAll("div", class_ = 'Cm_C'))
    pcitems = []
    pcprices = []
    pcurls = []
    try:
        name = sp.find("div",{'class':'Cm_C'}).findAll("h5", {'class':'prod_name'})
        print(name)
        price = sp.find("div",{'class':'Cm_C'}).findAll("span", {'class':'value'})
        for itnn in name:
            pcitems.append(itnn.text)
        for itpp in price:
            pcprices.append(itpp.text)
        for iturl in name:
            t2 = iturl.get('href')
            pcurls.append(t2)
    except:
        pcitems.append("NULL")
        pcprices.append("NULL")
        pcurls.append("NULL")
    print(len(pcitems), " ", len(pcprices), " ", len(pcurls))      
    for item in range(0, len(pcurls)):
        print(pcurls[item])
    c = open("pchome.csv","w", newline='', encoding='utf-8')      
    writer = csv.writer(c, delimiter=',')       
    writer.writerow(['item','price','url'])
    for item in range(0, len(moitn)):
        temp = [pcitems[item], pcprices[item], pcurls[item]]
        writer.writerow(temp)
    c.close()
"""