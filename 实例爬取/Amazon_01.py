import requests
url = "https://www.amazon.cn/dp/B078FFX8B6/ref=cngwdyfloorv2_recs_0/459-1268658-8279449?pf_rd_m=A1AJ19PSB66TGU&pf_rd_s=desktop-2&pf_rd_r=W7DJ7VBD5SGDE79BJBKX&pf_rd_r=W7DJ7VBD5SGDE79BJBKX&pf_rd_t=36701&pf_rd_p=d2aa3428-dc2b-4cfe-bca6-5e3a33f2342e&pf_rd_p=d2aa3428-dc2b-4cfe-bca6-5e3a33f2342e&pf_rd_i=desktop"
try:
    kv = {"user-urgent": "Chrome/74.0"}  # requests库，更改头部信息，重新定义
    r = requests.get(url, headers=kv)
    r.raise_for_status()
    # r.encoding = r.apparent.encoding
    print(r.text[:1000])
except:
    print("爬取失败")