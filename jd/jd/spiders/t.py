# -*- coding: utf-8 -*-
import scrapy,json


class TSpider(scrapy.Spider):
    name = 't'
    allowed_domains = ['jd.com']
    start_urls = ['https://p.3.cn/prices/mgets?skuIds=J_12750790201']

    def parse(self, response):
        print(json.loads(response.body.decode())[0]["op"])
        pass
