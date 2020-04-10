#!/usr/bin/python3
# -*- coding: utf-8 -*-
import requests

session=requests.Session()
headers={'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit'}
#添加请求头
r=session.get('https://www.baidu.com/',headers=headers)
# 将cookiejar类型的转成字典形式的方法
dic_cookies = requests.utils.dict_from_cookiejar(session.cookies)
print(dic_cookies)
print('*'*30)
print(session.cookies)

