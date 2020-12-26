from selenium import webdriver
from bs4 import BeautifulSoup

driver = webdriver.Chrome('C:/Users/realadmin3/Desktop/chromedriver/chromedriver.exe')
# 3초 쉬고
driver.implicitly_wait(3)
# url에 접근
driver.get('http://www.todayhumor.co.kr/')
# HTML형태로 받아와서 soup에 넣어놓음
soup = BeautifulSoup(driver.page_source, 'html.parser')

#print(soup)

for i in soup.find_all("td", class_="subject") :
    print(i.text)

driver.find_element_by_id("span_topmenu_bestofbest").click()

print("구분선 -------------------------------------------------")

soup = BeautifulSoup(driver.page_source, 'html.parser')

for i in soup.find_all("td", class_="subject") :
    print(i.text)
    
# 자유게시판 제목 크롤링
print("구분선2 -------------------------------------------------")
driver.find_element_by_id("span_topmenu_freeboard").click()

for i in soup.find_all("td", class_="subject") :
    print(i.text)
    
print("구분선 -----------------------------------------")

#driver.close()