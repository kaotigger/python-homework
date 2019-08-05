
import requests
import time
from bs4 import BeautifulSoup
import os
import re
import urllib.request
import json
def analysis(soup):
    for link in soup.find_all('dd',class_=True,id=True):
        if(link.find_all('a')):
            for i in link.find_all('a'):
                i.decompose()
        if(link.find_all('ol')):
            for i in link.find_all('ol'):
                i.decompose()
        #print(link.prettify())
        #print(link.get_text())
        words=str(link)
    a=re.sub(re.compile("<dd.*?>"),"",words)
    a=re.sub(re.compile("</dd>"),"",a)
    a=re.sub(re.compile("更多更詳盡歌詞 在"),"",a)
    #print(a)
    m=re.split("<br/>",a)
    #print("\n".join(m))
    #while '' in m:
    #    m.remove('')
    #print(m)
    print("\n".join(m))
    return m

def get_web_page(url):
    time.sleep(0.5)  # 每次爬取前暫停 0.5 秒以免被 PTT 網站判定為大量惡意爬取
    resp = requests.get(
        url=url,
        #cookies={'over18': '1'}
    )
    if resp.status_code != 200:
        print('Invalid url:', resp.url)
        return None
    else:
        return resp.text
    
if __name__=="__main__":
    ids=["twy100188x35x1","twy106207x3x2"]
    urls=[]
    for i in ids:
        urls.append("https://mojim.com/"+i+".htm")
    #url="https://mojim.com/twy106207x2x5.htm"
    for url in urls:
        origian_web_code=get_web_page(url)
        soup1 = BeautifulSoup(origian_web_code, 'html.parser')
        analysis(soup1)
        print("\n===========================================================\n")
    #print(soup1.prettify())