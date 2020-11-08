# 获得糗事百科热图中所有图片

import requests
import re
import os

if not os.path.exists('data/qiutu'):
    os.mkdir('data/qiutu')

headers = {
    'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Mobile Safari/537.36'
}
url = "https://www.qiushibaike.com/imgrank/page/{}"
img_src_list = []
for i in range(1, 5):
    # print(url.format(i))
    page = requests.get(url=url, headers=headers).text
    ex = '<img src="(.*?)"'
    img_src_list += re.findall(ex, page, re.S)[1:]

for src in img_src_list:
    img_url = 'https:' + src
    # print(img_url)
    img_data = requests.get(img_url).content
    img_name = re.findall('.*/(.*)', src)[0]
    file_name = 'data/qiutu/' + img_name
    fout = open(file_name, 'wb')
    fout.write(img_data)
    fout.close()

