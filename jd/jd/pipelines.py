# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import codecs,os,json
import pymysql

class JdPipeline(object):
    def __init__(self):
        # 打开文件,做写入前的准备
        self.conn = pymysql.connect(host='3306',user='root',passwd='root',db='scrapy')  #连接数据库
        # self.file = codecs.open('jd.json','w+',encoding='utf-8')
        # 先写入[
        # self.file.write('[')
 
    # 处理item的函数
    def process_item(self, item, spider):
        # self.conn.query(
        # "insert jd(book_sort_url,em_list,em_list_url,chuban_name)"  #需要插入的字段
        # "values('{}','{}','{}','{}')".format(
        # item['book_sort_url'],item['em_list'],item['em_list_url'],item['chuban_name']  #爬取项目中定义的字段
        # ))
        # self.conn.query(
        # "insert jd(book_sort,book_sort_url,em_list,em_list_url,chuban_name,book_img,book_people,book_money)"  #需要插入的字段
        # "values('{}','{}','{}','{}','{}','{}','{}','{}')".format(
        # item['book_sort'],item['book_sort_url'],item['em_list'],item['em_list_url'],item['chuban_name'],item['book_img'],item['book_people'],item['book_money']  #爬取项目中定义的字段
        # ))
        self.conn.query(
        "insert jd(book_sort,book_url,book_sort_url,em_list,em_list_url,chuban_name,book_name,book_img,book_people,book_money)"  #需要插入的字段
        "values('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(
        item['book_sort'],item['book_url'],item['book_sort_url'],item['em_list'],item['em_list_url'],item['chuban_name']," ".join(item['book_name']).strip(),item['book_img'],item['book_people'],item['book_money']  #爬取项目中定义的字段
        ))
        self.conn.commit()#执行添加
        # print(item['book_name'][0])
        # 1.把item转换字典类型
        # item = dict(item)
        # json_str = json.dumps(item,ensure_ascii=False)
        # self.file.write(json_str)
        # # 写入,逗号 把每个字典分开
        # self.file.write(',\n')
        # # 返回一个item 交给下一个pipeline处理
        return item
 
    # 爬虫关闭时,将文件填写完整,关闭文件
    def close_spider(self,spider):
        # self.file.seek(-2,os.SEEK_END)
        # self.file.truncate()
        # self.file.write(']')
        self.conn.close()  #关闭连接
        # self.file.close()
