# encoding: utf-8
"""
@project = pythontest
@file = love
@author = liu_bo
@create_time = 2018/9/13 11:07
@describe = 
"""
import requests
from lxml import etree
from bs4 import BeautifulSoup as BS
from selenium import webdriver
import time
import random
import os
import itchat
import datetime

love_word_path = 'love_word.txt'
pic_path = '示爱图片'


def crawl_Love_words():
    """
    抓取情话
    :return:
    """
    browser = webdriver.Chrome()
    print("正在抓取情话...")
    url = "http://www.binzz.com/yulu2/3588.html"
    browser.get(url)
    html = browser.page_source
    Selector = etree.HTML(html)
    love_words_xpath_str = "//div[@id='content']/p/text()"
    love_words = Selector.xpath(love_words_xpath_str)
    for i in love_words:
        word = i.strip("\n\t\u3000\u3000").strip()
        with open(love_word_path, "a") as file:
            file.write(word + "\n")
    print("情话抓取完成")


def getimage():
    """
    抓取我爱你的图片
    :return:
    """
    browser = webdriver.Chrome()
    url = 'http://image.so.com/i?q=%E6%88%91%E7%88%B1%E4%BD%A0%E7%94%B5%E5%BD%B1%E5%8F%B0%E8%AF%8D&src=srp'
    browser.get(url)
    count = 1
    for i in range(2):
        js = "var q=document.documentElement.scrollTop=100000"
        browser.execute_script(js)
        time.sleep(1)
    time.sleep(2)
    response = browser.page_source
    html = BS(response, 'lxml')
    imgurls = html.select('img')
    isexist(pic_path)
    for imgurl in imgurls:
        response = requests.get(imgurl['src'])
        image_path = str(count) + '.jpg'
        count += 1
        with open(image_path, 'wb') as f:
            f.write(response.content)
            print(str(count) + ' success')


def isexist(path):
    """
    判断文件是否存在
    :param path:
    :return:
    """
    if not os.path.exists(path):
        os.makedirs(path)
        os.chdir(path)
    else:
        os.chdir(path)


def send_news():
    """
    给你心爱的ta发送消息和图片
    :return:
    """
    # 计算相恋天数
    inLoveDate = datetime.datetime(2016, 5, 1)  # 相恋的时间
    todayDate = datetime.datetime.today()
    inLoveDays = (todayDate - inLoveDate).days
    Wordsnumber = random.randint(1, 120)  # 随机挑选出情话

    # 获取情话
    file_path = love_word_path
    with open(file_path) as file:
        love_word = file.readlines()[Wordsnumber].split('：')[1]
        print(love_word)

    # SINCERE_WISH = u'祝%s新年快乐！'
    # 向所有的好友发送不同的祝福消息
    # friendList = itchat.get_friends(update=True)[1:]
    # for friend in friendList:
    #     # 如果是发送目的，把下面的方法改为itchat.send即可
    #     print(SINCERE_WISH % (friend['DisplayName'] or friend['NickName']), friend['UserName'])
    #     time.sleep(.5)
    itchat.auto_login(hotReload=True)  # 热启动，不需要多次扫码登录
    print(itchat.get_chatrooms())
    # friend_name = u'如花'
    # my_friend = itchat.search_friends(name=friend_name)
    friend_name = '继续一起聊bug'
    my_friend = itchat.search_chatrooms(name=friend_name)
    if my_friend is None:
        print(u'没有找到my_friend:' + friend_name)
    else:
        girlfriend = my_friend[0]["UserName"]
        print(girlfriend)
        message = """
        亲爱的{}:
        中午好，今天是你和 bobo 相恋的第 {} 天~
        今天他想对你说的话是：
        {}
        最后也是最重要的！
        """.format("如花", str(inLoveDays), love_word)
        itchat.send(message, toUserName=girlfriend)

        files = os.listdir(pic_path)
        print(files)
        file = files[Wordsnumber]
        print(file)
        love_image_file = "./"+pic_path+"/" + file
        try:
            itchat.send_image(love_image_file, toUserName=girlfriend)
        except Exception as e:
            print(e)


def main():
    if os.path.exists(love_word_path):
        print('话已存在')
    else:
        crawl_Love_words()

    if os.path.exists(pic_path):
        print('图片已存在')
    else:
        getimage()
    send_news()


if __name__ == '__main__':
    while True:
        curr_time = time.strftime("%Y-%m-%d %H:%M", time.localtime())
        love_time = curr_time.split(" ")[1]
        if love_time != "13:14":
            main()
            time.sleep(60)
        else:
            print("还没到时间哟，现在时间：" + love_time)
