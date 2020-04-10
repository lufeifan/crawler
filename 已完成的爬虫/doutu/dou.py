import requests
from lxml import etree
headers={
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:74.0) Gecko/20100101 Firefox/74.0',
}
url ='https://www.doutula.com/search?keyword=%E5%A4%A9%E7%9C%9F'
r=requests.get(url,headers=headers)
html=etree.HTML(r.text)

reponse = html.xpath('//*[@id="search-result-page"]/div/div/div[2]/div/div[1]/div/div/a/@href')

print(reponse)