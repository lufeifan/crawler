# -*- coding: utf-8 -*-
import scrapy
import urllib.parse
import re

class DouyinSpider(scrapy.Spider):
    name = 'douyin'
    # allowed_domains = ['music.163.com']
    start_urls = ['http://music.163.com/discover/toplist']

    def parse(self, response):
        with open('wangyi.txt','w',encoding='utf-8') as f:
            f.write(response.text)
        pattern = re.compile(r'^<ul class="f-hide">$')
        s=pattern.findall(response.text)
        print(s)
        pass

