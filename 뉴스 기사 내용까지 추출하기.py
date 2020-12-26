import requests
from bs4 import BeautifulSoup

req = requests.get("http://www.donga.com/news/List/Enter/?p=1&prod=news&ymd=&m=")
soup = BeautifulSoup(req.text, 'html.parser')

#1. 반복문을 통해서 링크에 접근한다.
for i in soup.find_all("div", class_='rightList') :
    #2. html을 가져온다.
    req_new = requests.get(i.find("a")['href'])
    #3. txt화 한다.
    soup_new = (req_new.text, 'html.parser')
    
    print(soup_new)