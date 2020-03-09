import urllib
import urllib.request
import urllib.parse
import requests,json
import random
import http.cookiejar
import re
import os
import random
import time
from DB_func import addFini
from bs4 import BeautifulSoup as bs
#faker包，生产随机虚拟headers
from faker import Faker
uA = Faker()
#全局变量，页数控制
pageIndex = 0
filename = None

#异常处理，只控制程序进行不实际报错
class EmptyError(Exception):
    pass

def getProxy():
    proxy_pool_url = 'http://127.0.0.1:5010/get'
    while(1):
        response = requests.get(url=proxy_pool_url)
        proxy_json = json.loads(response.text)['proxy']
        print("using : " + proxy_json)
        ip = proxy_json.split(':')[0]

        proxy = {
            'http': 'http://' + str(proxy_json),
            'https': 'https://' + str(proxy_json),
        }

        user_agent_list = [
            'Mozilla/5.0 (Windows NT 6.2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/28.0.1464.0 Safari/537.36',
            'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.16 Safari/537.36',
            'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.3319.102 Safari/537.36',
            'Mozilla/5.0 (X11; CrOS i686 3912.101.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.116 Safari/537.36',
            'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.93 Safari/537.36',
            'Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/32.0.1667.0 Safari/537.36',
            'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:17.0) Gecko/20100101 Firefox/17.0.6',
            'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/28.0.1468.0 Safari/537.36',
            'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2224.3 Safari/537.36',
            'Mozilla/5.0 (X11; CrOS i686 3912.101.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.116 Safari/537.36'
        ]
        UserAgent = random.choice(user_agent_list)

        head = {'User-Agent': UserAgent}
        try:
            # p = requests.get('http://icanhazip.com', headers=head, proxies=proxy)
            p = requests.get('http://pv.sohu.com/cityjson', headers=head, proxies=proxy,timeout=3)
        except:
            continue

        if ip in p.text:
            print(p.text+ "  √")
            #print(proxy_json + "  √")
            break
        else:
            pass

    return proxy_json

#爬取评论主要函数
def getComments(name,id,sort='movie'):
    '''
    :param name: 爬取对象名称
    :param id: 爬取对象豆瓣对应ID
    :param sort: 分类（电影：movie，书籍：book，音乐：music）
    :return: 返回评论保存到本地的文件夹路径
    '''
    while 1:
        global pageIndex
        page = pageIndex*20
        pageIndex += 1
        headers = {'User-Agent': uA.user_agent()}
        #代理IP，西刺代理这个不知道现在还能不能用，当时性能挺好的

        proxy = str(getProxy())
        proxies = {
            'http': 'http://' + proxy,
            'https': 'https://' + proxy,
        }

        #电影应该是豆瓣最开始的业务吧，和其他分类的URL完全不一样
        if sort == 'movie':
            url = 'https://movie.douban.com/subject/' + id + '/comments?start='+ str(page) + '&limit=20&sort=new_score&status=P'
        else:
            url = 'https://book.douban.com/subject/'+ id + '/comments/hot?p=' + str(pageIndex)
            print(url)
        try:
            '''
                此处两种出发异常，①URL访问失败,②评论爬取为空（最后一页以后均为空）
                触发异常以后弃用代理或者更换代理。
            '''
            print("with proxy")
            response = requests.get(url=url,headers=headers,proxies=proxies)
            html = response.text
            #print(html)
            soup = bs(html, 'lxml')
            if sort == "movie":
                comm_tag = soup.find_all('p', attrs={'class': ""})[:-6]
            else:
                comm_tag = soup.find_all('p', attrs ={'class':"comment-content"})
                #print(comm_tag)
            if comm_tag == []:
                #print("sssssss")
                raise EmptyError("response is empty!")
        except:
            time.sleep(3)
            print("without proxy")
            response = requests.get(url=url,headers=headers)
            html = response.text
            soup = bs(html, 'lxml')
            if sort == "movie":
                comm_tag = soup.find_all('p', attrs={'class': ""})[:-6]
            else:
                comm_tag = soup.find_all('p', attrs ={'class':"comment-content"})
            #print(comm_tag)
        finally:
            path = '/Users/hang/PycharmProjects/bishe/Douban_Comments_Spider/comments_infor/'+ sort + "/" +name
            isExists = os.path.exists(path)
            if not isExists:
                os.makedirs(path)
            else:
                if comm_tag == []:
                    print('page %d is empty'%(page))
                    break
                else:
                    for i in comm_tag:
                        substr = i.get_text()
                        strlist = substr.split()
                        comment = ''.join(strlist)
                        print(comment)
                        global filename
                        filename = "/Users/hang/PycharmProjects/bishe/Douban_Comments_Spider/comments_infor/" + sort + '/' + name +"/"+ name + "_comments.txt"
                        #print(filename)
                        try:
                            with open(filename, 'a+') as f:
                                f.write(comment + "\n\n")
                        except:
                            #评    论信息含有emoji表情
                            pass
                        finally:
                            pass
                    if sort == 'movie':
                        print('finished page %d'%(page))
                    else:
                        print('finished page %d'%(pageIndex))

                    time.sleep(random.randint(3,6))

    print("All have written into files!")
    addFini(sort,name)
    return "./comments_infor/"+ sort + '/' + name +"/"+ name + "_comments"

"""
    login()为登陆函数，因为在电影短片的前（page=200）页无登陆限制，以后需要登陆。
    其他分类无登陆限制
    本来想写登陆的，测试的时候账号被永久封了，慎重啊。
"""
# def login():
#     login_url = 'https://www.douban.com/login'
#     captcha_Json_url = 'https://www.douban.com/j/misc/captcha'
#     headers = {'User-Agent': uA.user_agent()}
#
#     captchaInfor = requests.get(captcha_Json_url,headers=headers)
#     imgUrl ='https://' +  captchaInfor.json()['url'][2:]
#     token = captchaInfor.json()['token']
#
#     img = requests.get(imgUrl,headers=headers).content
#     with open('captcha img.png','wb') as f:
#         f.write(img)
#     text = input('输入验证码：')
#
#     data = {
#                "form_email": username,
#                "form_password": password,
#                "captcha-solution": text,
#     }
#
#     session = requests.Session()
#     data = session.post(login_url,data,headers=headers)
#     cookies = requests.utils.dict_from_cookiejar(session.cookies)
#     print(cookies)
#     return cookies

