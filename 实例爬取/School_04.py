"""
中国最好大学定向爬虫
程序的结构设计：
1.从网络上获取大学排名网页内容
grtHTMLText()
2.提取网页内容中信息到合适的数据结构
fillUnivList()
3.利用数据结构展示并输出结果

关于对齐
中文对其问题的解决
采用中文字符的空格填充 chr(12288)
printUnivList()
"""
import requests
from bs4 import BeautifulSoup
import bs4
def getHTMLText(url):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ""

def fillUnivList(ulist, html):
    soup = BeautifulSoup(html, 'lxml')
    for tr in soup.find('tbody').children:
        """
        过滤标签类型
        """
        if isinstance(tr, bs4.element.Tag):
            tds = tr('td')
            '''
            .string 取标签的字符串，tr('td') 也就是tr.find_all('td')
            '''
            ulist.append([tds[0].string, tds[1].string, tds[3].string])

def printUnivList(ulist, num):
    """
    10表示字符串的宽度
    宽度不够时，采用中文空格填充，中文空格的编码为chr(12288)
    """
    tplt = "{0:{3}^10}\t{1:{3}^10}\t{2:^10}"
    print(tplt.format("排名", "学校名称", "总分", chr(12288)))
    for i in range(num):
        u = ulist[i]
        print(tplt.format(u[0], u[1],u[2], chr(12288)))
    # print("Suc" + str(num))

# def main():
#     uinfo = []
#     url = "http://www.zuihaodaxue.com/zuihaodaxuepaiming2019.html"
#     html = getHTMLText(url)
#     fillUnivList(html, url)
#     printUnivList(uinfo, 20)  # 20所学校信息
# main()
if __name__ == "__main__":
    uinfo = []
    url = "http://www.zuihaodaxue.com/zuihaodaxuepaiming2019.html"
    html = getHTMLText(url)
    # print(getHTMLText(url))
    fillUnivList(uinfo, html)
    printUnivList(uinfo, 3)
