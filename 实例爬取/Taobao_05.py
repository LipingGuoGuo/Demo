"""
淘宝
功能描述：
目标：获取淘宝搜索页面的信息，提取其中的商品名称和价格
理解：获取淘宝的搜索接口
翻页的处理
技术路线：requests-re

书包：
https://s.taobao.com/search?q=%E4%B9%A6%E5%8C%85&imgfile=&commend=all&ssid=s5-e&search_type=item&sourceId=tb.index&spm=a21bo.2017.201856-taobao-item.1&ie=utf8&initiative_id=tbindexz_20170306

程序的结构设计：
1.提交商品搜索请求，循环获取页面
2.对于每个页面，提取商品名称和价格信息
3.将信息输出到屏幕上
"""
import requests
import re
def getHTMLText(url):
    try:
        r = requests.get(url)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ""

def parsePage(ilt,html):
    try:
        '''
        正则表达式的含义是 匹配双引号内遗传由若干数字和小数点组成的字符
        列表类型
        '''
        plt = re.findall(r'\"view_price\"\:\"{\d\.}*\"', html)
        """
        *?最小匹配
        正则表达式的含义是 非贪婪匹配raw_string对应的值也就是双引号内任意字符串
        """

        tlt = re.findall(r'\"raw_title\"\:\".*?\"', html)
        for i in range(len(plt)):
            price = eval(plt[i].split(':')[1])
            title = eval(tlt[i].split(':')[1])
            ilt.append([price, title])
    except:
        print("")

def printGoodList(ilt):
    tplt = "{:4}\t{:8}\t{:16}"
    print(tplt.format("序号", "价格", "商品名称"))
    count = 0
    for g in ilt:
        count = count + 1
        print(tplt.format(count, g[0], g[1]))

def main():
    goods = "书包"
    depth = 2
    start_url = "https://s.taobao.com/search?q=" + goods
    infoList = []
    for i in range(depth):
        try:
            url = start_url + "&s=" + str(44*i)
            html = getHTMLText(url)
            parsePage(infoList, html)
        except:
            continue
    printGoodList(infoList)
main()


