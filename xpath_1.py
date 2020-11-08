# 爬取58上海二手房的房源信息

from lxml import etree
import requests

url = "https://sh.58.com/ershoufang/"
headers = {
    'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Mobile Safari/537.36'
}
page_text = requests.get(url, headers=headers).text
fout = open('data/58.html', 'w', encoding='utf-8')
fout.write(page_text)
fout.close()
# 从爬取来的代码中创建etree对象
tree = etree.HTML(page_text)
text_list = tree.xpath('//div[@class="list-container"]//li[@class="list-item-info-title"]/text()')
fout = open('data/58.txt', 'w', encoding='utf-8')
fout.write('\n'.join(text_list))
print('\n'.join(text_list))
fout.close()