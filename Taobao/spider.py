#  coding: utf-8
#数据采集

import re
import time
import pandas as pd
import requests


start = time.clock() #计时开始
#为1-100页的url编号
plist = []
for i in range(1,101):
    plist.append((i-1)*44)

datamsp = pd.DataFrame(columns=[])

while True:
    def network_programming(num):
        url='https://s.taobao.com/search?q=%E9%9B%A8%E4%BC%9E&imgfile=&js=1&stats_click=search_radio_all%3A1&initiative_id=staobaoz_20180913&ie=utf8&fs=1&filter_tianmao=tmall&filter=reserve_price%5B%2C70%5D&bcoffset=0&p4ppushleft=%2C44&s='+str(num)
        web = requests.get(url,headers = headers)
        web.encoding = 'utf-8'
        #print(web.text)
        return web

    #构造heasers
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3534.4 Safari/537.36'}

    for i in plist:
        webi = network_programming(i)
        #print(webi.text)
        #event.append(webi)
        regex = re.compile('"auctions":(.*?),"recommendAuctions"')
        json = regex.findall(webi.text)
        if(len(json)):
            table = pd.read_json(json[0], encoding='utf-8')
            datamsp = pd.concat([datamsp, table], axis=0, ignore_index=True)
    break
datamsp.to_excel('datamap.xls',index = False)
datamsp.t
end = time.clock()
print(end-start)




