# coding: utf-8
from selenium import webdriver
from mylog import MyLog as mylog
import json
import os
import urllib.request
import time


class GetJianDan(object):
    """the all data from jandan.net
    所有数据来自煎蛋网
    """
    def __init__(self):
        self.startUrl = 'http://jandan.net/ooxx'
        self.log = mylog()
        self.browser = self.getBrowser()
        self.getPageNext(self.browser)

    def getBrowser(self):
        try:
            # 方法一: 指定PhantomJS的路径
            #browser = webdriver.PhantomJS(executable_path=r"D:\phantomjs-2.1.1-windows\bin\phantomjs.exe")
            # 方法二: 复制PhantomJS.exe到C:\Python35目录下(Python安装目录下)
            browser = webdriver.PhantomJS()
            browser.get(self.startUrl)   # 打开目标网站
            browser.implicitly_wait(20)  # 等待js代码加载完毕
        except Exception as e:
            self.log.error('open the %s failed:%s' % (self.startUrl, e))
        else:
            return browser

    def saveImg(self, browser):
        # 找到所有图片的标签,返回一个list
        elements = browser.find_elements_by_xpath('//ol[@class="commentlist"]//div[@class="row"]\
        //div[@class="text"]')
        for element in elements:
            # print(type(element))
            src = element.find_element_by_xpath("./p//img").get_attribute('src')    # img 下载地址
            imgName = element.find_element_by_xpath("./span/a").text    # img 名字
            suffix_name = os.path.splitext(src)[1]  # img后缀名
            # 判断图片后缀是否为.gif,如果是则获取org_src属性
            if suffix_name == '.gif':
                # 重新赋值给src,这样爬取的才是动态的gif图片
                src = element.find_element_by_xpath("./p//img").get_attribute('org_src')
            full_name_img = imgName + suffix_name  # img完整名字
            try:
                # 下载图片,需要传入(图片下载地址,img完整名字带后缀名)
                urllib.request.urlretrieve(src, full_name_img)
                time.sleep(1)  # 设置下载延迟，防止被封
            except Exception as e:
                self.log.error('%s download failed, %s' % (full_name_img, e))
            else:
                self.log.info('%s download success' % full_name_img)

    def createDir(self, dirName):
        """创建目录"""
        if os.path.exists(dirName):
            self.log.error('create directory %s failed, have a sane name file or directory' % dirName)
        else:
            try:
                os.makedirs(dirName)
            except Exception as e:
                self.log.error('create directory %s failed : %s' % (dirName, e))
            else:
                self.log.info('create directory %s success' % dirName)

    def getPageNext(self, browser):
        # 获取总页数
        sumPage = json.loads(browser.find_element_by_xpath("//div[@class='comments']/\
        div[@class='cp-pagenavi']/span[last()]").text)
        cartoonTitle = browser.title  # 获取目录名
        self.createDir(cartoonTitle)  # 创建存储图片目录
        os.chdir(cartoonTitle)  # 进入创建的目录
        i = 1
        while i <= sumPage[0]:
            self.saveImg(self.browser)
            i += 1
            self.log.info('开始爬取第%d页' % i)
            # 利用selenium点击下一页,获取下一页的内容
            NextTag = browser.find_element_by_partial_link_text("下一页").click()
            browser.implicitly_wait(30)  # 等待加载js代码
            time.sleep(3)
        self.log.info('save img success')
        browser.quit()


if __name__ == '__main__':
    st = GetJianDan()