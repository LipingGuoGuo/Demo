""""
网络图片的爬取
网络图片链接的格式：
http://www.example.con/picture.jpg
国家地理：
http://www.nationalgeographic.com.cn/
选择一个图片web页面：
http://www.nationalgeographic.com.cn/photography/photo_of_the_day/3921.html
"""
import requests
import os
url = "http://image.nationalgeographic.com.cn/2017/0211/20170211061910157.jpg"
root = "F://pics//"
# root = r"F:\pics\\"也可
path = root + url.split("/")[-1]
try:
    if not os.path.exists(root):
        ''' 
        os.mkdir()创建一个新目录
        '''
        os.mkdir(root)
    if not os.path.exists(path):
        '''
        os.path.exists(path)路径存在返回True,路径不存在返回False
        '''
        r = requests.get(url)
        with open(path, "wb") as f:
            '''
            r.content 返回二进制形式内容
            wb 二进制写入
            '''
            f.write(r.content)
            f.close()
            print("文件保存成功")
    else:
        print("文件已存在")
except:
    print("爬取失败")

