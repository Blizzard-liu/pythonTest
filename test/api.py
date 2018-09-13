"""
@project = pythontest
@file = api
@author = liu_bo
@create_time = 2018/9/11 12:48
"""
import requests
from lxml import etree


def getOnePage(page):
    # url = "http://maoyan.com/board"
    url = 'http://maoyan.com/board/4?offset = {}'.format(page * 10)

    '''
    User-Agent: Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36
    '''
    user_Agent = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36"}
    # r = requests.get(url)
    r = requests.get(url, headers=user_Agent)
    print(r.text)
    return r.text


text = getOnePage(1)


def parse(text):
    html = etree.HTML(text)
    title = html.xpath('//div[@class = "movie-item-info"]/p[@class = "name"]/a/@title')
    time = html.xpath('//p[@class = "releasetime"]/text()')

    for k, v in zip(title, time):
        print(k + " = ", v)


parse(text)
