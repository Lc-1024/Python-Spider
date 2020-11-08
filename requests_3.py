# 破解百度翻译


import requests
import json

word = input('word: ')

url = 'https://fanyi.baidu.com/sug'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.18363'
}
data = {
    'kw': word
}
response = requests.post(url, data, headers=headers)
# 如果确定返回的是json数据，可以调用json()获得obj
obj = response.json()

file_name = 'data/' + word + '.json'
fout = open(file_name, 'w', encoding='utf-8')
json.dump(obj, fout, ensure_ascii=False)
fout.close()
