# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class TutorialItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # title=scrapy.Field()
    # info=scrapy.Field()
    serial_number=scrapy.Field()
    movie_name=scrapy.Field()
    introduce=scrapy.Field()
    star=scrapy.Field()
    evaluate=scrapy.Field()
    describemas=scrapy.Field()
    
