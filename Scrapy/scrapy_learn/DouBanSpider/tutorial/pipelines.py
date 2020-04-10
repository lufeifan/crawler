# -*- coding: utf-8 -*-
import codecs,os,json
import pymysql
class TutorialPipeline(object):
    
    def __init__(self):
        # 打开文件,做写入前的准备
        # self.conn = pymysql.connect(host='3306',user='root',passwd='root',db='scrapy')  #连接数据库
        self.file = codecs.open('sohu.json','w+',encoding='utf-8')
        # 先写入[
        self.file.write('[')
 
    # 处理item的函数
    def process_item(self, item, spider):
        # self.conn.query(
        # "insert scrapy(serial_number,movie_name,introduce,star,evaluate,describemas)"  #需要插入的字段
        # "values('{}','{}','{}','{}','{}','{}')".format(
        # item['serial_number'],item['movie_name'],item['introduce'],item['star'],item['evaluate'],item['describemas']  #爬取项目中定义的字段
        # ))
        # self.conn.commit()#执行添加
        # 1.把item转换字典类型
        item = dict(item)
        json_str = json.dumps(item,ensure_ascii=False)
        self.file.write(json_str)
        # 写入,逗号 把每个字典分开
        self.file.write(',\n')
        # 返回一个item 交给下一个pipeline处理
        return item
 
    # 爬虫关闭时,将文件填写完整,关闭文件
    def close_spider(self,spider):
        self.file.seek(-2,os.SEEK_END)
        self.file.truncate()
        self.file.write(']')
        # self.conn.close()  #关闭连接
        self.file.close()
 
    