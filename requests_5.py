# 爬取KFC在某地区的餐厅

import requests
import json

url = "http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx"

# 搜索时对应的参数
data = {
    'keyword': '温州',
    'cname': '',
    'pageIndex': '1',
    'pageSize': '10',
    'pid': ''
}
params = {
    'op': 'keyword'
}
# UA伪装
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.18363'
}

response = requests.post(url=url, data=data, params=params, headers=headers)
print(response.text)
file_name = 'data/KFC.txt'
fout = open(file_name, 'w', encoding='utf-8')
fout.write(response.text)
fout.close()
