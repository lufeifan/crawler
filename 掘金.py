#
import requests,json
from bs4 import BeautifulSoup
headers={
    'Host': 'web-api.juejin.im',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:74.0) Gecko/20100101 Firefox/74.0',
    'X-Agent': 'Juejin/Web',
    'Origin': 'https://juejin.im',
    'Referer': 'https://juejin.im/welcome/ai/%E6%95%B0%E6%8D%AE%E5%88%86%E6%9E%90'
}
params = {"operationName":"","query":"","variables":{"tags":["58e753128d6d810061760e56"],"category":"57be7c18128fe1005fa902de","first":20,"after":"","order":"POPULAR"},"extensions":{"query":{"id":"653b587c5c7c8a00ddf67fc66f989d42"}}}
r=requests.post('https://web-api.juejin.im/query',json=params,headers=headers,)
datas = r.json()['data']['articleFeed']['items']['edges']
mas = {}
url,title =[],[]
for data in datas:
    url.append(data['node']['originalUrl'])
    title.append(data['node']['title'])
    # mas['url'] =data['node']['originalUrl']
    # mas['title'] =data['node']['title']
mas['url'] = url
mas['title'] = title
a= json.dumps(mas,ensure_ascii=False)
print(a)