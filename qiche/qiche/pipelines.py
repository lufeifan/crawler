# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import codecs,os,json
import pymysql
from urllib import request

from scrapy.pipelines.images import ImagesPipeline


class QichePipeline(object):
    def __init__(self):

        # self.path=os.path.join(os.path.dirname(os.path.dirname(__file__)),'images')
        # if not os.path.exists(self.path):
        #     os.mkdir(self.path)

        self.conn = pymysql.connect(host='3306',user='root',passwd='root',db='scrapy')  #连接数据库


    # 处理item的函数
    def process_item(self, item, spider):

        # urlss=item['imgurl']
        # img_name=urlss.split('_')[-1]
        # request.urlretrieve(urlss,os.path.join(self.path,img_name))

        self.conn.query(
        "insert doutu(imgurl)"  #需要插入的字段
        "values('{}')".format(
        item['image_urls']
        ))
        self.conn.commit()#执行添加
        return item

    # 爬虫关闭时,将文件填写完整,关闭文件
    def close_spider(self, spider):
        self.conn.close()  #关闭连接


class QicheImagesPipeline(ImagesPipeline):
    def file_path(self, request, response=None, info=None):

        pass