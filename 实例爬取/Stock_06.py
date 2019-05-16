"""
候选数据网站的选择
选取原则：股票信息静态存在于HTML页面中，非JS代码生成，没有robots协议限制
选取方法：浏览器F12，源代码查看等
选取心态：可以多找信息源尝试

程序的结构设计
1.从东方财富网获取股票列表
2.根据股票列表逐个到百度股票获取个股信息
3.将结果存储到文件

"""
import requests
from bs4 import BeautifulSoup
import traceback
import re

def getHTMLText(url, code="utf-8"):
    try:
        r = requests.get(url,timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ""

def getStockList(lst, stockURL):
    html = getHTMLText(stockURL, "GB2312")
    soup = BeautifulSoup(html, "lxml")
    a = soup.find_all("a")
    for i in a:
        try:
            href = i.attrs["href"]
            lst.append(re.findall(r"[s][hz]\d{6}", href)[0])
        except:
            continue

def getStockInfo(lst, stockURl, fpath):
    count = 0

    for stock in lst:
        url =stockURl + stock + ".html"
        html = getHTMLText(url)
        try:
            if html == "":
                continue
            infoDict = {}
            soup = BeautifulSoup(html, "lxml")
            stockInfo = soup.find("div", attrs = {"class": "stock-bets"})
            name = stockInfo.find_all(attrs={"class": "bets-name"})[0]
            infoDict.update({"股票名称": name.text.split()[0]})
            keyList = stockInfo.find_all("dt")
            valueList = stockInfo.find_all("dd")
            for i in range(len(keyList)):
                key = keyList[i].text
                value = valueList[i].text
                infoDict[key] = value

            with open(fpath, "a", encoding="utf-8") as f:
                f.write(str(infoDict) + "\n")
                count = count + 1
                print("\r当前速度:{:2f}%".format(count*100/len(lst)), end="")
        except:
            count = count + 1
            print("\r当前速度:{:2f}%".format(count * 100 / len(lst)), end="")
            traceback.print_exc()
            continue

        return ""

def main():
    stock_list_url = "http://quote.eastmoney.com/stocklist.html"
    stock_info_url = "https://gupiao.baidu.com/stock/"
    output_file = "F://BaiduStockInfo.txt"
    slist = []
    getStockList(slist,stock_info_url)
    getStockInfo(slist,stock_info_url,output_file)
