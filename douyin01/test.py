#!/usr/bin/python3
# -*- coding: utf-8 -*-
import re
from selenium import webdriver
browser = webdriver.PhantomJS()
browser.get("https://music.163.com")
browser.implicitly_wait(20)  # 等待js代码加载完毕
 # browser.save_screenshot('1.png') 

iframe_elemnt = browser.find_element_by_id("g_iframe")
browser.switch_to.frame(iframe_elemnt)

elements = browser.find_elements_by_xpath('//div[@id="top-flag"]//dl[1]//dd//ol//li')
for element in elements:
    # print(type(element))
    title = element.find_element_by_xpath('./a').get_attribute("href")
    # title=re.findall(r'id=\d+',title)
    title=title.split('?')[1]
        # author = element.find_element_by_css_selector('.nm.nm-icn.f-thide.s-fc3').text
    print(title)
# https://music.163.com/song?id=1436910205


browser.quit()
