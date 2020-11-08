# 网页采集器

import requests

url = "https://www.baidu.com/s"

search = input("what you want to search: ")
# 搜索时对应的参数
params = {
    'wd': search
}
# UA伪装
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.18363'
}
response = requests.get(url=url, params=params, headers=headers)

file_name = 'data/' + search + '.html'
fout = open(file_name, 'w', encoding='utf-8')
fout.write(response.text)
print(response.text)
fout.close()

