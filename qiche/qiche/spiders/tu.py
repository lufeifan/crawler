# -*- coding: utf-8 -*-
import scrapy,json

from qiche.items import QicheItem


class TuSpider(scrapy.Spider):
    name = 'tu'
    allowed_domains = ['car.autohome.com']
    start_urls = ['https://car.autohome.com.cn/pic/series/66.html']

    def parse(self, response):
        urllist=response.xpath("//div[@class='uibox']")[1:]
        for urli in urllist:
            imgs=urli.xpath(".//ul/li/a/img/@src").getall()
            urls=list(map(lambda url:response.urljoin(url),imgs))
            item=QicheItem(image_urls=urls)
            yield item
