# -*- coding: utf-8 -*-
import scrapy


class ZhiSpider(scrapy.Spider):
    name = 'zhi'
    allowed_domains = ['zhihu.com']
    start_urls = ['https://www.zhihu.com/people/cliff-92-84']

    def parse(self, response):
        username = response.xpath('//*[@id="ProfileHeader"]/div/div[2]/div/div[2]/div[1]/h1/span[1]/text()').get()
        onther_user =response.xpath('//*[@id="root"]/div/main/div/div[2]/div[2]/div[2]/div/a[1]/@href').get()
        yield scrapy.Request(
            "https://www.zhihu.com"+onther_user,
            callback=self.guanzhu
        )
        print(username)

    def guanzhu(self,response):
        # print(response.url)
        onther_people=response.xpath('//*[@class="UserLink"]/div[@class="Popover"]/div/a')
        print(onther_people)
        for i in onther_people:
            people = i.xpath('text()').get()
            print(people)