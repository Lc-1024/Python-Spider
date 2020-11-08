# 获取国家药监总局化妆品公司的许可证

import requests
import json

url = "http://scxk.nmpa.gov.cn:81/xk/itownet/portalAction.do"
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.18363'}
params = {'method': 'getXkzsList'}
data = {
    'on': 'true',
    'page': '1',
    'pageSize': '15',
    'productName': '',
    'conditionType': '1',
    'applyname': '',
    'applysn': ''
}
ids = []
# 获取前十页所有公司的ID
for page in range(1, 11):
    data['page'] = str(page)
    # 获取网站中关于所有公司的链接信息
    json_datas = requests.post(url, data=data, params=params, headers=headers).json()
    # 从链接信息中获得各个公司对应的ID，作为获取证书的data
    for d in json_datas['list']:
        ids.append(d['ID'])

# 利用id获得证书
params = {'method': 'getXkzsById'}
data = {}
all_data = []
for id in ids:
    data['id'] = id
    detail_json = requests.post(url, data=data, params=params, headers=headers).json()
    all_data.append(detail_json)

file_name = 'data/company.json'
fout = open(file_name, 'w', encoding='utf-8')
json.dump(all_data, fout, ensure_ascii=False)
fout.close()

print(len(all_data))
