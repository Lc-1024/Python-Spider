# 最简单的爬虫程序

import requests

url = "https://www.baidu.com/"

response = requests.get(url)
print(response.text)
fout = open("data/baidu.html", 'w', encoding='utf-8')
fout.write(response.text)
fout.close()