import requests
from bs4 import BeautifulSoup


#1. URL을 Requests로 가져오기
req = requests.get('https://www.naver.com')

#2. html을 TXT로 변경하기
soup = BeautifulSoup(req.text, 'html.parser')

# 3. 필요한 부분을 뽑아내기 - 1(조건지정)

for i in soup.find_all("span", class_="txt_issue"):
	print(i.text)

# 3. 필요한 부분을 뽑아내기 -2(명시적지정)
for i in soup.select("url"):
	print(i.find("a").text)

