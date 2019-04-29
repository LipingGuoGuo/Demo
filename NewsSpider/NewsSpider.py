# -*- coding: utf-8 -*-
import os
import sys
import urllib.request
import requests
import re
from lxml import etree

def StringListSave(save_path, filename, slist):
    # os.path.exists(path) 路径存在则返回True，路径损坏返回False
    if not os.path.exists(save_path):
        # os.makedirs()方法用于递归创建目录，mkdir()创建的所有的intermediate-level文件夹需要包含子目录
        os.makedirs(save_path)
    path = save_path + "/" + filename +".txt"
    with open(path, "w+") as fp:
        for s in slist:
            fp.write("%s\t\t%s\n" % (s[0].encode("utf8"), s[1].encode("utf8")))

def Page_Info(myPage):
    mypage_Info = re.findall(r'<div class="titleBar" id=".*?"><h2>(.*?)</h2><div class="more"><a href="(.*?)">.*?</a></div></div>', myPage, re.S)
    return mypage_Info

def New_Page_Info(new_page):
    dom = etree.HTML(new_page)
    new_items = dom.xpath('//tr/td/a/text()')
    new_urls = dom.xpath('//tr/td/a/@href')
    assert(len(new_items)) ==  len(new_urls)
    return zip(new_items,new_urls)

def Spider(url):
    i = 0
    print("下载：", url)
    myPage = requests.get(url).content.decode("gbk")
    # urllib.request 请求模块
    # urllib.request.urlopen(url,data=None,{timeout,}*,cafile=None,capath=NOne,cadefault=False,content=None}

    myPage = urllib.request.urlopen(url).read().decode("gbk")
    myPageResults = Page_Info(myPage)
    save_path = u"网易新闻抓取"
    filename = str(i)+"_"+u"新闻排行版"
    StringListSave(save_path,filename,myPageResults)
    i += 1
    for item,url in myPageResults:
        print("下载：", url)
        new_page = requests.get(url).content.decode("gbk")
        newPageResults = New_Page_Info(new_page)
        filename = str(i)+"_"+item
        StringListSave(save_path, filename, newPageResults)
        i += 1

if __name__ == '__main__':
    print("start")
    start_url = "http://news.163.com/rank/"
    Spider(start_url)
    print("end")