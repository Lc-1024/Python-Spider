# 使用线程池进行多线程操作

import time
from multiprocessing.dummy import Pool
from lxml import etree
import requests
import re
start_time = time.time()


url = "https://www.pearvideo.com/category_8"
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36'
}
page_text = requests.get(url, headers=headers).text
tree = etree.HTML(page_text)

video_paths = tree.xpath('//*[@id="listvideoListUl"]/li/div/a/@href')
video_names = tree.xpath('//*[@id="listvideoListUl"]/li//div[@class="vervideo-title"]/text()')

video_urls = []
for path, name in zip(video_paths, video_names):
    video_page_url = "https://www.pearvideo.com/" + path
    video_page_text = requests.get(video_page_url, headers=headers).text
    ex = 'srcUrl="(.*?\.mp4)"'
    video_url = re.findall(ex, video_page_text)[0]
    video_urls.append(video_url)

def get_video(t):
    url = t[0]
    name = t[1]
    print(url, 'downloading...')
    data = requests.get(url, headers=headers).content
    fout = open('data/'+name+'.mp4', 'wb')
    fout.write(data)
    fout.close()
    print(name, 'Finished.')

pool = Pool(2)
pool.map(get_video, zip(video_urls, video_names))
pool.close()
pool.join()

end_time = time.time()
cost_time = end_time - start_time
print(cost_time, 's')


