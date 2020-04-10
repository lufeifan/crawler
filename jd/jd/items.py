# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class JdItem(scrapy.Item):
    # define the fields for your item here like:
    book_sort = scrapy.Field()
    book_sort_url = scrapy.Field()
    em_list = scrapy.Field()
    em_list_url = scrapy.Field()
    chuban_name = scrapy.Field()
    book_name = scrapy.Field()
    book_img = scrapy.Field()
    book_people = scrapy.Field()
    book_money = scrapy.Field()
    book_sku =scrapy.Field()
    book_url =scrapy.Field()

