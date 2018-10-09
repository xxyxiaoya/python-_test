# -*- coding:utf-8 -*-
import re
import requests
from bs4 import BeautifulSoup

#----------------------------------------------登陆-----------------------------------------------------
host = "http://sit1-credit.zhph.lan"  # 系统域名地址
urll = host + "/logon.do"
data = {
    "method":"login",
    "username":"xiaoxiaoya",
    "password":"123456"
    }
r_login = requests.post(url=urll,data=data)
print r_login.text
print r_login.cookies["JSESSIONID"]
# strin = r_login.cookies["JSESSIONID"]
cookies = str(r_login.cookies["JSESSIONID"])
# s = requests.session()  # 保持会话

urll_1 = host + "/queryP2pAccountInfoAction.do"
header = {"Cookie":"cookies"}
data_1 = {
    "mainBody":"HT",
    "perPageCount":"15",
    "pageTurn":"YES",
    "currPage":"1",
    "method":"queryP2pAccountInfo",
    }
file = {"files[]": ("50216.jpg", open("E:\\code\\XD_dh\\50216.jpg", "rb"), "")}
r = requests.post(url=urll_1,headers=header,data=data_1,files=file)
print r.text
urls = re.findall(r'class="items".*?href="(.*?)"', r.text, re.S)  # re.S 把文本信息转换成1行匹配
print urls
print (type(urls))
print "-" * 100

# r = requests.get(url=host)
# html = r.text
# if r.status_code == 200:
#     # print html  #返回文本内容
#     soup = BeautifulSoup(html, "html.parser")
#     # print('soup:')
#     # print soup
#     # print(type(soup))
# else:
#     print "responseCode:"
#     print r.status_code
#
# # a = soup.find_all("form")    #查找所有form标签
# a = soup.select('form[action^="/"]')    #查找在form标签中属性为action，且action值以"/"开头的标签
#
# # b = soup.select("input[class]")    #查找input标签中包含class属性的标签
# # b = soup.find_all("input",class_="s_ipt")    # 查找在input标签中属性class为"s_ipt"的标签
# # b = soup.select('input[id^="k"]')    #查找在input标签中属性为id，且id值以"k"开头的标签
# # b = soup.select('input[id$="w"]')    #查找在input标签中属性为id，且id值以"w"结尾的标签
# # b = soup.find_all("input",attrs={"class":"s_ipt","id":"kw"})    #查找在input标签中多属性匹配的标签
# # print b
# print a    #查找出的a格式为list
# # print(type(a))
# print "x"*100
# #打印出标签所含list个数
# print "标签个数："
# print len(a)
# print("="*100)
# #打印出标签中属性值影藏的url
# # print a[0]['action']
# for i in a:
#     print i["action"]
#     url = host + i["action"]
#     print url
#     q = requests.post(url=url)    #遍历请求
#     print q.text

class Result:
    def __init__(self):
        self.url = ''
        self.result = ''

class Pachong:
    def __init__(self, hosturl):
        self.report = []  # ['url1,jieguo','']
        self.urls = []  # 类变量
        self.hosturl = hosturl

    def a(self, hostUrl):
        new_urls = []
        if 'http://' not in hostUrl and 'https://' not in hostUrl:
            hostUrl = self.hosturl + hostUrl

        # setp1：通过hostUrl请求获取html解析出urls数组
        r = requests.get(url=hostUrl)

        if r.status_code == 200:
            html = r.text
            soup = BeautifulSoup(html, "html.parser")
            s = Result()
            s.url = hostUrl
            s.result = '请求成功'
            self.report.append(s)
        else:
            print "responseCode:"
            print r.status_code
            s = Result()
            s.url = hostUrl
            s.result = '请求失败'
            self.report.append(s)

        a = soup.select('form[action^="/"]')  # 查找在form标签中属性为action，且action值以"/"开头的标签,type为list
        for i in a:
            print i["action"]
            url = self.hosturl + i["action"]
            print url
            # 去重
            if url not in self.urls:
                self.urls.append(url)
                new_urls.append(url)
         # setp2：new_urls，
        for j in new_urls:
            self.a(j)

# p = Pachong("http://sit1-credit.zhph.lan")
# p.a("http://sit1-credit.zhph.lan")
# print('='*100)
# for i in p.report:
#     print i.url,i.result