from selenium import webdriver

driver = webdriver.Chrome('C:/Users/realadmin3/Desktop/chromedriver/chromedriver.exe')

driver.implicty_wait(3)

driver.get('https://nid.naver.com/nidlogin.login?mode=form&url=https%3A%2F%2Fwww.naver.com')

driver.find_element_by_id("id").send_keys("alstjdwo323")
driver.find_element_by_id("pw").send_keys("realbale!")

#driver.find_element_by_class("btn_global").click()
#씨발 위에 코드로 하면 진행 안 됨

#driver.find_element_by_id("log.login").click()