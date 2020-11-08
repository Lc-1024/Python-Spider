# selenium实现简单的浏览器操作

from selenium import webdriver
from lxml import etree

# 实例化一个浏览器对象
bro = webdriver.Chrome(executable_path="chromedriver")

# 发起一个url请求
url = "http://scxk.nmpa.gov.cn:81/xk/"
bro.get(url)

# 获取源码数据
page_text = bro.page_source

fout = open('data/huazhuangpin.html', 'w', encoding='utf-8')
fout.write(page_text)
fout.close()

tree = etree.HTML(page_text)
name = tree.xpath('//ul[@id="gzlist"]/li/dl/@title')
print(name)

bro.quit()