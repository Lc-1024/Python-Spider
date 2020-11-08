# 爬取4k美食的图片

from lxml import etree
import requests
import os


url = "http://pic.netbian.com/4kmeishi/"
headers = {
    'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Mobile Safari/537.36'
}
page_text = requests.get(url, headers=headers).text
page_text = page_text.encode('ISO-8859-1').decode('gbk')
fout = open('data/meishi.html', 'w', encoding='utf-8')
fout.write(page_text)
fout.close()
# 从爬取来的代码中创建etree对象
tree = etree.HTML(page_text)
src = tree.xpath('//*[@id="main"]/div[3]/ul//img/@src')
alt = tree.xpath('//*[@id="main"]/div[3]/ul//img/@alt')

if not os.path.exists('data/meishi'):
    os.mkdir('data/meishi')
for url, name in zip(src, alt):
    url = "http://pic.netbian.com" + url
    img_data = requests.get(url, headers=headers).content
    file_path = 'data/meishi/' + name + '.jpg'
    fout = open(file_path, 'wb')
    fout.write(img_data)
    fout.close()
