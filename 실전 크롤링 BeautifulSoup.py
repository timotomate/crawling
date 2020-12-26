import requests
from bs4 import BeautifulSoup

req = requests.get("https://search.naver.com/search.naver?sm=tab_hty.top&where=news&query=코로나")

soup = BeautifulSoup(req.text, 'html.parser')

"""
for i in soup.select("#main_pack > div > ul > li > dl > dt") :
    print(i.text)
print("\n------------------------------------\n")
"""

for i in soup.select("#main_pack > div.news.mynews.section._prs_nws > ul > li") :
    print(i.find("dt").text)

print("\n------------------------------------\n")    

url_list = []

for j in soup.select("#main_pack > div > div.paging > a") :
    url_list.append("https://search.naver.com/search.naver" + j['href'])
    
for k in range(0,5) :
    print("\n------------------------------------\n")
    
    req2 = requests.get(url_list[k])
    
    soup2 = BeautifulSoup(req2.text)
    
    for i in soup2.select("#main_pack > div.news.mynews.section._prs_nws > ul > li") :
        print(i.find("dt").text)
    
    