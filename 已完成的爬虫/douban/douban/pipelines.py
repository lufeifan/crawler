# -*- coding: utf-8 -*-
import pymysql
import scrapy

from douban.items import DoubanItem


class DoubanPipeline(object):
    def __init__(self):
        self.conn = pymysql.connect(host='3306', user='root', passwd='root', db='scrapy')  # 连接数据库

    def process_item(self, item, spider):
        self.conn.query(
            "insert douban(books_name,book_fen,img_url,book_t)"
            "values('{}','{}','{}','{}')".format(
                item['books_name'],item['book_fen'],item['img_url'],item['book_t']
            )
        )
        self.conn.commit()  # 执行添加
        return item

    def close_spider(self, spider):
        self.conn.close()  # 关闭连接

from scrapy.pipelines.images import ImagesPipeline

class MypipeimageslinePipeline(ImagesPipeline):
    #继承类
    def get_media_requests(self, item, info):
        for images_url in item['my_images_urls']:
            yield scrapy.Request(images_url)
            # 返回图片链接所指向的response
    def item_completed(self, results, item, info):
        images_path = [x['path'] for ok,x in results if ok]
        # results是之前get_media_requests返回的，具体看下面
        if not images_path:
            # pass
            raise DoubanItem("item contains no images")
        item['image_path'] = images_path
        # 将图片的链接存储在item里面
        return item
        # return item 必不可少，用来返回item以便其它管道调用item进行处理
