# 爬取论语中的全部内容

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

soup = BeautifulSoup(first_page, 'lxml')

fout = open("data/lunyu.txt", 'w', encoding='utf-8')
for detail in soup.select(".book-mulu a"):
    fout.write(detail.text+'\n\n\n')
    text_url = 'https://www.shicimingju.com' + detail['href']
    text_page = requests.get(text_url, headers=headers).text
    text_soup = BeautifulSoup(text_page, 'lxml')
    for sen in text_soup.select('.chapter_content p'):
        fout.write(sen.text)
    fout.write('\n\n\n')
fout.close()
