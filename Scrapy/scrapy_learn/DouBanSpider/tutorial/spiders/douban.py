# -*- coding: utf-8 -*-
import scrapy
from tutorial.items import TutorialItem

class DoubanSpiderSpider(scrapy.Spider):
    name = 'douban'
    # allowed_domains = ['movie.douban.com']
    # start_urls = ['https://read.douban.com/category?page=1&kind=100']
    # start_urls = ['http://movie.douban.com/top250']


    def parse(self, response):
        
        book_list=response.xpath("//div[@class='extra-info']/div[@class='sticky-info']/div[@class='rating']/a[@class='amount']") 
        for i in book_list:
            book_item=TutorialItem()
            book_item['title']=i.xpath("text()").extract()
        
            yield book_item

        # 获取下一页内容
        # next_link = response.xpath("//div[@class='paginator-full']/ul/li/a/@href").extract()
        # self.log(next_link)
        # if next_link is not None:
        #     for url in next_link:  
        #         url = "https://read.douban.com/" + url  
        #         yield scrapy.Request(url, callback=self.parse)  
            # next_link = next_link[0]
            # yield scrapy.Request("https://movie.douban.com/top250"+next_link,callback=self.parse)
