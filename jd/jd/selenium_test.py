
# from selenium import webdriver
# import time
# browser = webdriver.Chrome()
# browser.get(url='https://www.baidu.com')
# time.sleep(2)
# input = browser.find_element_by_css_selector('#kw')
# input.send_keys('韩国女团')
# time.sleep(2)
# input.clear()
# input.send_keys('后背摇')
# button = browser.find_element_by_css_selector('#su')
# button.click()
# time.sleep(10)
# browser.close()

# from selenium import webdriver
# from selenium.webdriver import ActionChains

# browser = webdriver.Chrome()

# url = "http://www.runoob.com/try/try.php?filename=jqueryui-api-droppable"
# browser.get(url)
# browser.switch_to.frame('iframeResult')
# source = browser.find_element_by_css_selector('#draggable')
# target = browser.find_element_by_css_selector('#droppable')
# actions = ActionChains(browser)
# actions.drag_and_drop(source, target)
# actions.perform()

# from selenium import webdriver
# browser = webdriver.Chrome()
# browser.get("http://www.zhihu.com/explore")
# browser.execute_script('window.scrollTo(0,document.body.scrollHeight)')
# browser.execute_script('alert("To Bottom")')