from urllib import request
from urllib import parse
# import requests
from http.cookiejar import CookieJar
# url="https://passport.csdn.net/login"
url="https://www.csdn.net/"
# https://www.csdn.net/
# reqs=requests.get("https://www.csdn.net/")
# request.urlretrieve("https://www.lagou.com/","lagou.html")
# print(reqs.read()
# print(reqs.text)
cooks =CookieJar()
handler =request.HTTPCookieProcessor(cooks)
opener = request.build_opener(handler)

headers={
    "cookie":"uuid_tt_dd=10_18967429480-1546066692684-819876; ADHOC_MEMBERSHIP_CLIENT_ID1.0=cd907735-4a72-d35a-9972-3475ee92a278; smidV2=20190314180351d753612bc456e4d739aac872786cff3400791083439258400; UN=qq_42852199; Hm_ct_6bcd52f51e9b3dce32bec4a3997715ac=6525*1*10_18967429480-1546066692684-819876!1788*1*PC_VC!5744*1*qq_42852199; dc_session_id=10_1556192991599.310188; _ga=GA1.2.843540842.1556673732; __gads=ID=218b0ee3cd9d1419:T=1582511085:S=ALNI_MaH-fKfl8vTsRc4j__N8vmMC3N-rw; firstDie=1; announcement=%257B%2522isLogin%2522%253Atrue%252C%2522announcementUrl%2522%253A%2522https%253A%252F%252Fblog.csdn.net%252Fblogdevteam%252Farticle%252Fdetails%252F103603408%2522%252C%2522announcementCount%2522%253A0%252C%2522announcementExpire%2522%253A3600000%257D; SESSION=6bf07ad7-cc4f-4afe-9ae6-2374285446b4; TY_SESSION_ID=622931f8-1957-45d2-800c-6ee78b836d39; c-toolbar-writeguide=1; c_ref=https%3A//www.baidu.com/link%3Furl%3DK6Hwb4V7yz1uxBimTrM5drW1OyxqeaZfO_kHlvvUqRRI4kgo6jGvTIkF-FXv7bdMIo_jDru7lTNNpr2SjB3OR3h_k2O-1l3x5dlPgwsn2R7%26wd%3D%26eqid%3Db910503d0001398f000000065e7d66cf; Hm_lvt_6bcd52f51e9b3dce32bec4a3997715ac=1585274953,1585275230,1585276200,1585276630; UserName=qq_42852199; UserInfo=1a127c512a7544458fe4a25dec7dd1e9; UserToken=1a127c512a7544458fe4a25dec7dd1e9; UserNick=lufeifana; AU=2BA; BT=1585277101610; p_uid=U000000; Hm_lpvt_6bcd52f51e9b3dce32bec4a3997715ac=1585277109; dc_tos=q7tzn8",
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36",
}
data={
    # "username":'18376098023',
    # "password":"18376098023aA.."
    'all':'18376098023',
    'pwd':'18376098023aA..'
}
# req=request.Request(url=url,data=parse.urlencode(data).encode('utf-8'),headers=headers)
req=request.Request(url=url,headers=headers)

# opener.open(req)

req = request.urlopen(req)
# print(req.read().decode('utf-8'))

with open('1.html',"w",encoding='utf-8') as f:
    f.write(req.read().decode('utf-8'))

# user_url="https://www.zhihu.com/question/382731837"
# req=request.Request(url=user_url,headers=headers)
# resp=opener.open(req)
# with open('1.html',"w",encoding='utf-8') as f:
#     f.write(resp.read().decode('utf-8'))