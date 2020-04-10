# -*- coding: utf-8 -*-
import codecs,os,json
import pymysql

class DoutuPipeline(object):
    def __init__(self):
        self.conn = pymysql.connect(host='3306', user='root', passwd='root', db='scrapy')  # 连接数据库

    def process_item(self, item, spider):
        self.conn.query(
            "insert doutu(imgurl)"  # 需要插入的字段
            "values('{}')".format(
                item['imgurl']
            ))
        self.conn.commit()  # 执行添加
        return item

    # 爬虫关闭时,将文件填写完整,关闭文件
    def close_spider(self, spider):
        self.conn.close()  # 关闭连接
