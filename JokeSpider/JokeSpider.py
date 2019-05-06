import urllib.request
from bs4 import BeautifulSoup
import xlwt
import xlrd
import time
wb = xlwt.Workbook()
ws = wb.add_sheet('test')
def getHTML(url):
    headers = {
        'User-Agent': 'User-Agent:Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.108 Safari/537.36 '}
    req = urllib.request.Request(url, headers=headers)
    return urllib.request.urlopen(req).read()

def creatSoup(url):
    html_text = getHTML(url)
    soup_0 = BeautifulSoup(html_text, 'html.parser')
    return soup_0

def creatExcelAndSheet(sheetName):
    file = xlwt.Workbook(encoding = 'utf-8', style_compression = 0)
    sheet = file.add_sheet(sheetName)
    return sheet, file

def writeToSheet(a, b, c):
    ws.write(a, b, c)

def summaryAllContent(a,b,url):
    print("提示：抓取结束，无更多内容")
    print("-------------summary----------")
    print("您抓取的网址为%s" % url)
    print("共抓取%d页 共%d个内容" % (a-1, b-1))
    print("------------------------------")

def getEachContent(eachContent):
    sss = ""
    for s in eachContent.strings:
        sss += s
    return sss

# sheet,file = creatExcelAndSheet("data")
i = 1
k = 1
while i < 5:
    url = "https://www.qiushibaike.com/textnew/page/"+str(i)+"/"
    soup = creatSoup(url)
    a_soup = soup.select("div[class=content] span") # 根据关键字取得按list存放的内容
    contentLen = len(a_soup)
    print("Info:第%d页有%d个笑话" % (i, contentLen))
    print(a_soup)
    for eachContent in a_soup:
        sss = getEachContent(eachContent)
        print(sss)
        writeToSheet(k, 0, k)
        writeToSheet(k, 1, sss)
        print("正在获取第%d个内容...Done" %k)
        time.sleep(0.05)
        k += 1

    print("提示：正在获取下一页内容...")
    i += 1
    time.sleep(3)
summaryAllContent(i, k, url)


wb.save("C:/Users/dell/Desktop/test.xls")