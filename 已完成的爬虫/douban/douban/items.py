# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class DoubanItem(scrapy.Item):
    # define the fields for your item here like:
    book_t = scrapy.Field()
    books_name = scrapy.Field()
    book_fen = scrapy.Field()
    book_detail = scrapy.Field()
    img_url=scrapy.Field()
    jieshao = scrapy.Field()
    image_urls = scrapy.Field()
    images = scrapy.Field()


