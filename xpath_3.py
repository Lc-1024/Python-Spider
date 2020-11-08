# 爬取全国城市名称

from lxml import etree
import requests

url = "https://www.aqistudy.cn/historydata/"
headers = {
    'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Mobile Safari/537.36'
}
page_text = requests.get(url, headers=headers).text
fout = open('data/chengshi.html', 'w', encoding='utf-8')
fout.write(page_text)
fout.close()
# 从爬取来的代码中创建etree对象
tree = etree.HTML(page_text)
# 利用两个编码的共同性写xpath
name = tree.xpath('//div[@class="bottom"]//a/text()')
# 或者用 | 同时识别两条路径
# name = tree.xpath('//div[@class="bottom"]/ul/li/a/text() | //div[@class="bottom"]/ul/div[2]/li/a/text()')
fout = open('data/chengshi.txt', 'w', encoding='utf-8')
fout.write("\n".join(name))
print(len(name))
fout.close()
