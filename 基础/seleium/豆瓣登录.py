from selenium import webdriver
import time
driver =webdriver.Chrome()
driver.get("https://www.douban.com/")
iframe =driver.find_element_by_tag_name("iframe")
driver.switch_to_frame(iframe)
driver.find_element_by_class_name('account-tab-account').click()
time.sleep(1)
driver.find_element_by_id('username').send_keys('18376098023')
driver.find_element_by_id('password').send_keys('1020aA..')
driver.find_element_by_class_name('btn-account').click()

time.sleep(5)
cookies={i["name"]:i["value"] for i in driver.get_cookies()}
print(cookies)
driver.quit()