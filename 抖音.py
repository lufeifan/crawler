import requests
from bs4 import BeautifulSoup
headers={'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit'}
r=requests.get('https://tophub.today/n/KqndgxeLl9',headers=headers)
soup = BeautifulSoup(r.text)
data=[]
for item in soup.find_all('a')[2:22]:
    s=item.get_text().strip().split('\n')[0]
    data.append(item.get_text().strip().split('\n')[0])
print(data)
