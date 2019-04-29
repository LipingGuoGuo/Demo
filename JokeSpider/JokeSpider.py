import urllib.request
from bs4 import BeautifulSoup
import xlwt
import xlrd
import time

def getHTML(url):
    headers = {
        'User-Agent': 'User-Agent:Mozilla/35.0 Chrome/ 74.0.3729.108 '}
    req = urllib.request.Request(url, headers=headers)
    return urllib.request.urlopen(req).read()

def creatSoup(url):
    html_text = getHTML(url)
    soup_0 = BeautifulSoup(html_text, 'html5lib')
    return soup_0

def creatExcelAndSheet(SheetName):
    file = xlwt.Workbook(encoding = 'utf-8', style_compression = 0)
    sheet = file.add_sheet(SheetName)
    return sheet,file

def writeToSheet(a,b,c):
    sheet.write(a,b,c)

def summaryAllContent(a,b,url):
    print("提示：抓取结束，无更多内容")
    print("-------------summary----------")
    print("您抓取的网址为%s"%url)
    print("共抓取%d页 共%d个内容"%(a-1,b-1))
    print("------------------------------")

def getEachContent(eachContent):
    a = eachContent.select("div")[0]
    b = a.select("span")[0]
    sss = " "
    for s in b.strings:
        sss += s
    return sss

sheet,file = creatExcelAndSheet("data")

i = 1
k = 1
while i < 24:
    url = "https://www.qiushibaike.com/8hr/page/" + str(i) + "/?s=4991834"
    soup = creatSoup(url)
    a_soup = soup.select("a[class=contentHerf]")
    contentLen = len(a_soup)
    print("Info:第%d页有%d个笑话" % (i, contentLen))

    for eachContent in a_soup:
        sss = getEachContent(eachContent)
        writeToSheet(k, 0, k)
        writeToSheet(k, 1, sss)
        print("正在获取第%d个内容...Done" % k)
        time.sleep(0.05)
        k += 1

summaryAllContent(i, k, url)
file.save("C:/Users/Administrator/Desktop/笑话爬虫.xls")