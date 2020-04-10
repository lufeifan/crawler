# -*- coding: utf-8 -*-
import scrapy,json,urllib
from copy import deepcopy
from ..items import JdItem
class JSpider(scrapy.Spider):
    name = 'j'
    allowed_domains = ['jd.com']
    start_urls = ['https://book.jd.com/booksort.html']

    def parse(self, response):
        dl_list = response.xpath("//div[@class='mc']/dl/dt")
        for dl in dl_list:
            item = JdItem()
            item['book_sort'] = dl.xpath("./a/text()").extract_first()
            item['book_sort_url'] ='https:'+dl.xpath("./a/@href").extract_first()
            # item['book_sort_url'] = 'https:'+item['book_sort_url']
            em_list = dl.xpath("./following-sibling::dd/em")
            for em in em_list:
                item['em_list']=em.xpath('a/text()').extract_first()
                item['em_list_url'] = 'https:' +em.xpath('a/@href').extract_first()
                # print(item)
                yield scrapy.Request(
                    item['em_list_url'],
                    callback=self.parse_cate_url,
                    meta={"item":deepcopy(item)}
                )

    def parse_cate_url(self,response):
        item=response.meta['item']
        book_list =response.xpath('//*[@id="plist"]/ul/li')
        for book_item in book_list:
            item['chuban_name']=book_item.xpath('.//span[@class="p-bi-store"]/a/@title').extract_first()
            item['book_name']=book_item.xpath('..//div[@class="p-name"]/a/em/text()').extract_first().split()
            item['book_url']='https:'+book_item.xpath('.//div[@class="p-img"]/a/@href').extract_first()
            item['book_img']=book_item.xpath('.//div[@class="p-img"]/a/img/@src').extract_first()
            if item['book_img'] is None:
                item['book_img']=book_item.xpath('.//div[@class="p-img"]/a/img/@data-lazy-img').extract_first()
            item['book_img']='https:'+ item['book_img']
            
            item['book_sku'] = book_item.xpath("./div/@data-sku").extract_first()
            item['book_people']=book_item.xpath('.//span[@class="author_type_1"]/a/text()').extract_first()
            new_url='https://p.3.cn/prices/mgets?skuIds=J_{}'.format(item['book_sku'])
            # print(item)
            # yield(item)
            yield scrapy.Request(
                new_url,
                callback=self.parse_money,
                meta={"item": deepcopy(item)},
                dont_filter=True   #过滤域名
            )

    def parse_money(self,response):
        # print(response.text)
        item=response.meta['item']
        item['book_money'] =json.loads(response.body.decode())[0]["op"]
        # print(item)
        yield(item)

    # def money_url(self,response):
    #     print("ok")
    #     print(response.url)
    #     item=response.meta['item']
    #     item['book_money'] =json.loads(response.body.decode())[0]["op"]
    #     # print(item)
    #     yield(item)


        
