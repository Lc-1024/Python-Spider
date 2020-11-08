# 爬取豆瓣电影排行榜

import requests
import json

url = "https://movie.douban.com/j/chart/top_list"

# 搜索时对应的参数
params = {
    'action': '',
    'interval_id': '100:90', # %3A 问题仍待解决
    'type': '24',
    'start': '0',
    'limit': '20'
}
# UA伪装
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.18363'
}
response = requests.get(url=url, params=params, headers=headers)

file_name = 'data/douban.json'
fout = open(file_name, 'w', encoding='utf-8')
json.dump(response.json(), fout, ensure_ascii=False)
fout.close()
