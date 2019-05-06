import requests
from bs4 import BeautifulSoup
# import os
#
# path = os.chdir("./douban_photo")
# path1 = os.getcwd()
url = "https://movie.douban.com/top250"

'''
https://movie.douban.com/top250?start=25&filter=
https://movie.douban.com/top250?start=50&filter=
'''
i = 0
urls = ["https://movie.douban.com/top250?start" + str(n) + "&filter=" for n in range(0,250,25)]
for url in urls:
    wb_data = requests.get(url)
    soup = BeautifulSoup(wb_data.text,"lxml")
    # print(soup)
    title = soup.select("div.hd > a") # .类  > 子级标签
    # print(title)
    rates = soup.select("span.rating_num")
    imgs = soup.select("img[width='100']")
    for title,rate,img in zip(title, rates, imgs):
        data={
            "title":list(title.stripped_strings),
            "rate":rate.get_text(),
            "img":img.get("src")
        }
        i += 1
        fileName = str(i)+ "." + data["title"][0]+ " "+ data["rate"]+"分.jpg"
        pic = requests.get(data["img"])
        with open("./douban_photo/" + fileName, "wb") as photo:
            photo.write(pic.content)
        print(data)