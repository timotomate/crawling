# 1
import requests
from bs4 import BeautifulSoup 

req = requests.get('https://pann.nate.com/talk/c20002?page=1')
soup = BeautifulSoup(req.text, 'html.parser')

print(soup.select("#searchDiv > div.posting_wrap > table > tbody > tr"))

for i in soup.select("#searchDiv > div.posting_wrap > table > tbody > tr"):
    print(i.text)
	
for i in soup.select("#searchDiv > div.posting_wrap > table > tbody > tr"):
    print(i.find("a").text)
	
	

# 2
import requests
from bs4 import BeautifulSoup


for i in range(1,11):
    req = requests.get("https://pann.nate.com/talk/c20002?page="+str(i))
    soup = BeautifulSoup(req.text, 'html.parser')
    
    for i in soup.select("#searchDiv > div.posting_wrap > table > tbody > tr"):
        print((i.find("a").text).lstrip())