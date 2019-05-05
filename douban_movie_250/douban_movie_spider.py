import requests
from bs4 import BeautifulSoup
url = "https://movie.douban.com/top250"
wb_data = requests.get(url)
soup = BeautifulSoup(wb_data.text,"lxml")
titles = soup.select("div hd > a")
rates = soup.select("span.rating_num")
imgs = soup.select("img[width=100]")
for title,rate,img in zip(titles, rates, imgs):
    data={
        "title":list(title.stripped_string),
        "rate":rate.get_text(),
        "img":img.get("src")
    }