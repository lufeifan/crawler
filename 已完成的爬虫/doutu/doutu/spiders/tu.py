# -*- coding: utf-8 -*-
import scrapy
from doutu.items import DoutuItem

class TuSpider(scrapy.Spider):
    name = 'tu'
    allowed_domains = ['www.doutula.com']
    start_urls = ['http://www.doutula.com/photo/list/']

    def parse(self, response):
        imglist =response.xpath("//ul[@class='list-group']")
        for img in imglist:
            imgitem=DoutuItem()
            imgurl=img.xpath(".//a/img/@data-original").extract()

            urls=list(map(lambda url:response.urljoin(url),imgurl))
            item=DoutuItem(image_urls=urls)
            yield item
        
        # 获取下一页内容
        i=0
        next_link = response.xpath('//*[@id="pic-detail"]/div/div[2]/div[3]/ul/li[15]/a/@href').extract()
        # self.log(next_link)
        next_link = response.urljoin(next_link)
        if next_link is not None:
            for url in next_link:  
                url = "http://www.doutula.com" + url  
                yield scrapy.Request(url, callback=self.parse)  
                i=i+1
                print(i)
                print("*"*20)
        else:
            print("---"*15)
            # next_link = next_link[0]
            # yield scrapy.Request("http://www.doutula.com"+next_link,callback=self.parse)