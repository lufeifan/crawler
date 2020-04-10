# -*- coding: utf-8 -*-
import scrapy
from copy import deepcopy
from ..items import DoubanItem
class TuSpider(scrapy.Spider):
    name = 'tu'
    # allowed_domains = ['www.douban.com']
    start_urls = ['https://book.douban.com/tag/']
    def parse(self, response):
        book_tags = response.xpath('//*[@class="article"]/div[2]/div')
        for book_tag in book_tags:
            item = DoubanItem()
            book_t = book_tag.xpath("./a/@name").extract_first()
            s = book_tag.xpath(".//table[@class='tagCol']/tbody/tr/td")
            for book_tag_url in s:
                # print(book_tag_url)
                url=book_tag_url.xpath(".//a/@href").extract_first()
                book_t = book_tag_url.xpath(".//a/text()").extract_first()
                # item = DoubanItem()
                item['book_t'] = book_t
                yield scrapy.Request(
                    "https://book.douban.com/"+url,
                    callback=self.lists,
                    meta={"item": deepcopy(item)}
                )

    def lists(self,response):
        item=response.meta['item']
        books = response.xpath("//li[@class='subject-item']")
        for book in books:
            book_detail =book.xpath(".//div[@class='info']/div[@class='pub']/text()").extract_first().split()
            books_name =book.xpath("./div[@class='info']/h2/a/@title").extract_first()
            book_fen =book.xpath(".//div[@class='star clearfix']/span[@class='rating_nums']/text()").get()
            jieshao =book.xpath(".//div[@class='info']/p/text()").get()
            urls =book.xpath(".//div[@class='pic']/a[@class='nbg']/img/@src").extract()
            urls = list(map(lambda url: response.urljoin(url), urls))
            # print("*"*30)
            # print(urls)
            item['books_name']=books_name
            item['book_fen']=book_fen
            item['img_url']=urls
            item['jieshao']=jieshao
            item['image_urls']=urls
            yield(item)

        # next_link=response.xpath('//*[@id="subject_list"]/div[2]/a/@href').extract()[1:]
            # print(url)
        # if next_link is not None:
        #     for url in next_link:
        #         url = "https://book.douban.com/" + url
        #         print(url)
        #         yield scrapy.Request(url, callback=self.lists)
        # yield scrapy.Request(
        #     "https://book.douban.com/"+next_link[0],
        #     callback=self.lists
        # )
