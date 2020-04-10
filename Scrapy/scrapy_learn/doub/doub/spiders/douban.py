# -*- coding: utf-8 -*-
import scrapy
from doub.items import DoubItem
import logging
logger = logging.getLogger(__name__) #实例化

class DoubanSpider(scrapy.Spider):
    name = 'douban'
    # allowed_domains = ['read.douban.com/']
    # start_urls = ['https://read.douban.com/']
    start_urls = ['https://movie.douban.com/top250']

    # handle_httpstatus_list = [302]
    # start_urls = ['https://read.douban.com/category?kind=508']   
    # url = "https://read.douban.com/kind/508"
    # def start_requests(self):                               # 构建Start_Request
    # #     
    # #     meta = {'dont_redirect': True},
    #     yield scrapy.Request(url, meta={
    #             'dont_redirect': True,
    #             'handle_httpstatus_list': [302]
    #         },callback=self.parse)
    

    def parse(self, response):
        info_list = response.xpath("//div[@class='info']/div[@class='hd']/a/span[@class='title'][1]")
        # print(response.request.url)
        # print()
        # print(response.request.headers)
        # print(response.meta)
        # print(response.headers)
        # print(info_list)
        for i in info_list:
            book_item =DoubItem()
            book_item['title']=i.xpath('text()').extract()[0].split()
            logger.info(book_item)
            # print(book_item)
            yield book_item


