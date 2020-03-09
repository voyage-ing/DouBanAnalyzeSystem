import re
import os
import urllib
import random
import requests,json
import urllib.parse
import urllib.request
from lxml import etree

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

        print("chicking proxy ......")


        try:
            # p = requests.get('http://icanhazip.com', headers=head, proxies=proxy)
            p = requests.get('http://pv.sohu.com/cityjson', headers=head, proxies=proxy,timeout=3)
        except:
            continue

        if ip in p.text:
            print(p.text)
            print(proxy_json + "  √")
            break
        else:
            pass

    return proxy_json

subFilmURL = 'https://www.douban.com/search?cat=1002&q='
subBookURL = 'https://www.douban.com/search?cat=1001&q='
subMusicURL = 'https://www.douban.com/search?cat=1003&q='

class Douban_id():
    '''
    get a Douban id according to the film name,music name,or book name that you provid
    '''
    def __init__(self,name,sort='movie'):
        '''
        :param name: film name,music name,or book name
        :param sort: sort attr is optional just from ['movie','book','music']
        '''
        self.name = name
        self.sort = sort
        self.url_1 = subFilmURL
        self.url_2 = subBookURL
        self.url_3 = subMusicURL

    def getID(self):

        if self.sort == 'book':
            url = self.url_2 + urllib.parse.quote(self.name)
        elif self.sort == 'movie':
            url = self.url_1 + urllib.parse.quote(self.name)
        elif self.sort == 'music':
            url = self.url_3 + urllib.parse.quote(self.name)
        else:
            print("error: wrong option about catagory's name.the right one is from 'movie'or'music'or'book'")
            os._exit()


        headers = [{"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:60.0) Gecko/20100101 Firefox/60.0"},
                   {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36"},
                   {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/17.17134"},]
        header = random.choice(headers)

        # request = urllib.request.Request(url,headers=header)
        # response = urllib.request.urlopen(request)
        proxy = ''      #str(getProxy())

        proxies = {
            'http': 'http://' + proxy,
            'https': 'https://' + proxy,
        }

        response = requests.get(url,headers=header)
        # html = response.read().decode('utf-8')
        html = response.text

        selector = etree.HTML(html)
        a_tag =  selector.xpath('//*[@id="content"]/div/div[1]/div[3]/div[2]/div[1]/div[2]/div/h3/a/@onclick')[0]

        #print(a_tag)
        partten = re.compile(r'sid: (\d+)',re.S)

        filmID = partten.findall(a_tag)[0]

        return filmID




