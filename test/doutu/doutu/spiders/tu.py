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
            item=DoutuItem()
            imgurl=img.xpath(".//a/img/@data-original").extract()
            # print(imgurl)
            urls=list(map(lambda url:response.urljoin(url),imgurl))
            item=DoutuItem(image_urls=urls)
            # for i in imgurl:
            #     item["image_urls"]="https:"+i
                # print(item["image_urls"])
            yield item

        next_link = response.xpath('//*[@id="pic-detail"]/div/div[2]/div[3]/ul/li[13]/a/@href').extract()
        # self.log(next_link)
        # next_link = response.urljoin(next_link)
        print(next_link)
        if next_link is not None:
            for url in next_link:  
                url = "http://www.doutula.com" + url  
                yield scrapy.Request(url, callback=self.parse)  
            # next_link = next_link[0]
            # yield scrapy.Request("http://www.doutula.com"+next_link,callback=self.parse)