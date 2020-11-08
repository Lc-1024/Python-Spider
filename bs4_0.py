# bs4 的基本操作

import requests
from bs4 import BeautifulSoup

url = "https://www.shicimingju.com/book/lunyu.html"
headers = {
    'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Mobile Safari/537.36'
}
first_page = requests.get(url, headers=headers).text
fout = open("data/lunyu.txt", 'w', encoding='utf-8')
fout.write(first_page)
fout.close()
# 从文件中获取数据
fin = open("data/lunyu.txt", 'r', encoding='utf-8')
soup = BeautifulSoup(fin, 'lxml')

# 也可以将文本传入后获得soup对象
soup = BeautifulSoup(first_page, 'lxml')


# soup.tagName 返回第一个tagName(div, ul, li, a...)下的数据
print(soup.a)
# soup.find('tagName') == soup.tagName
print(soup.find('a'))
# soup.find('tagName', class_/id/attr='song') 
# 找到某个特定的tagName，参数固定且相等的第一个数据
print(soup.find('a', href="javascript:void(0)"))
# soup.select('.book-mulu')
# 找到参数==book-mulu的所有数据，返回一个list
print(soup.select(".book-mulu"))
# 层级选择器，一个>表示一级，找到该级下的所有数据，返回list
print(soup.select('div > ul > li > a'))
print(soup.select(".book-mulu > ul > li > a"))
# 中间用' '隔开表示多级
print(soup.select(".book-mulu a"))

# 获取对应路径下的数据
# .text / .get_text()  获取同一路径下的所有数据
# .string 获取该路径直接对应的数据
print(soup.select(".book-mulu a")[0].string)
print(soup.select(".book-mulu ul")[0].text)
print(soup.select(".book-mulu a")[0].get_text())
# 获得路径中的属性值，用字典的方法获取
print(soup.select(".book-mulu a")[0]['href'])
