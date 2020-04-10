# -*- coding: utf-8 -*-
import codecs,os,json
import pymysql
import request

class DoutuPipeline(object):
    def __init__(self):
        self.path=os.path.join(os.path.dirname(os.path.dirname(__file__)),'images')
        if not os.path.exists(self.path):
            os.mkdir(self.path)
        # self.conn = pymysql.connect(host='3306', user='root', passwd='root', db='scrapy')  # 连接数据库

    def process_item(self, item, spider):
        # urlss=item['image_urls']
        # for url in urlss:
        #     # img_name=urlss.split('/')[-1]
        #     request.urlretrieve(urlss,os.path.join(self.path))
        # self.conn.query(
        #     "insert doutu(imgurl)"  # 需要插入的字段
        #     "values('{}')".format(
        #         item['image_urls']
        #     ))
        # self.conn.commit()  # 执行添加
        return item

    # 爬虫关闭时,将文件填写完整,关闭文件
    def close_spider(self, spider):
        # self.conn.close()  # 关闭连接
        pass
