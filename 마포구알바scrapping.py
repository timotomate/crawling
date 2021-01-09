import os
import csv
import requests
from bs4 import BeautifulSoup

os.system("cls")
#os.system("clear")


alba_url = "http://www.alba.co.kr"
"""
mon_url = "https://www.alba2.co.kr"
req2 = requests.get(alba_url)
soup2 = BeautifulSoup(req.text, 'html.parser')
main2 = soup.find("div", {"id":"MainSuperBrand"})
brands = main.fnid_all("li"

for brand in brands:
    link = 


"""

req = requests.get(alba_url)
soup = BeautifulSoup(req.text, 'html.parser')
main = soup.find("div", {"id" : "MainSuperBrand"})
brands = main.find_all("li")#MainSuperBrand의 자손태그임

for brand in brands:
    link = brand.find("a", class_="goodsBox-info")
    name = brand.find("span", class_="company")
    if link and name is not None:
        link = link["href"]
        name = name.text
        company = {'name' : name, 'jobs' : []}
        jobs_request = requests.get(link)
        jobs_soup = BeautifulSoup(jobs_request.text, "html.parser") 
        tbody = jobs_soup.find("div", {"id" : "NormalInfo"}).find("tbody") #일반채용정보 표 전체
        rows = tbody.find_all("tr", {"class":""})
        for row in rows:
            local = row.find("td", class_="local")
            
            if local:
                local = local.text.replace(u'\xa0', ' ')
                
            title = row.find("td", class_="title")
            
            if title:
                title = title.find("a").find("span", {
                    "class": "company"
                }).text.strip()
                title = title.replace(u'\xa0', ' ')
            
            time = row.find("td", class_="data")
            
            if time:
                time = time.text.replace(u'\xa0', ' ')
            
            pay = row.find("td",class_="pay")
            
            if pay:
                pay = pay.text.replace(u'\xa0', ' ')
            
            date = row.find("td", class_="regDate")
            
            if date:
                date = date.text.replace(u'\xa0', ' ')
            
            job = {
                "위치" : local,
                "title" : title,
                "근무시간" : time,
                "시간" : pay,
                "등록시간" : date
            }
            company['jobs'].append(job)
        print(company)