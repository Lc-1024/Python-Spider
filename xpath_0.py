# xpath 基础操作

from lxml import etree
import requests

url = "https://www.shicimingju.com/book/lunyu.html"
headers = {
    'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Mobile Safari/537.36'
}
page_text = requests.get(url, headers=headers).text
# 从爬取来的代码中创建etree对象
tree = etree.HTML(page_text)
fout = open('data/lunyu.html', 'w', encoding='utf-8')
fout.write(page_text)
fout.close()
# 打开已有的html文件
parser = etree.HTMLParser(encoding='utf-8')
tree = etree.parse('data/lunyu.html', parser=parser)

# 获得某个路径下的对象
# 会获取匹配的所有的对象组成的list
print(tree.xpath('/html/head/meta'))
# 用//可以省略中间部分，获取前面的路径下所有的符合条件的路径
print(tree.xpath('/html/body//li'))

# 可以用属性值指定路径
print(tree.xpath('//div[@class="book-mulu"]'))
# 也可以用索引定位某一条路径，索引从1开始
print(tree.xpath('//div[@class="book-mulu"]/ul/li[3]/a'))

# 获取文本内容
# 用'/text()'获取该标签内直接的文本，返回为list
# 用'//text()'获取该标签内的所有文本，返回为list
print(tree.xpath('//div[@class="book-mulu"]/ul/li/a/text()'))
print(tree.xpath('//div[@class="book-mulu"]/ul/li//text()'))

# 获取属性值，用'/@xxx'获得符合条件的所有xxx的值，返回为list
print(tree.xpath('//div[@class="book-mulu"]/ul/li/a/@href'))