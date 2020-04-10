# -*- coding: utf-8 -*-
import scrapy,re
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
# from doub.items import DoubItem
import logging
logger = logging.getLogger(__name__) #实例化

class CfSpider(CrawlSpider):
    name = 'cf'
    # allowed_domains = ['movie.douban.com']
    start_urls = ['http://bxjg.circ.gov.cn/web/site0/tab5240/module14430/page1.htm']
    # start_urls = ['https://movie.douban.com/top250']

    rules = (
        # Rule(LinkExtractor(restrict_xpaths=("//div/dl[@ddt-area='5358']/dd")), callback='parse_item'),
        Rule(LinkExtractor(allow=r'/web/site0/tab5240/info\d+\.htm'), callback='parse_item', follow=True),  #LinkExtractor链接提取器
        # Rule(LinkExtractor(allow=r'/top250?start=\d{2}&filter='), callback='parse_item', follow=True),  #LinkExtractor链接提取器
        # Rule(LinkExtractor(allow=r'/web/site0/tab5240/module14430/page\d+\.htm'),follow=True),  # 下一页,不需要callback处理，但是需要follow不断循环翻页
    )

    def parse_item(self, response):
        item = {}
        # print(response.body.decode())
        # print(response.url)
        #item['domain_id'] = response.xpath('//input[@id="sid"]/@value').get()
        item['title'] = re.findall("<!--TitleStart-->(.*?)<!--TitleEnd-->",response.body.decode())[0].split()
        #item['description'] = response.xpath('//div[@id="description"]').get()
        print("end")
        logger.debug(item)
        yield item
