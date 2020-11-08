# 爬取图片

import requests
url = "https://qiubai-video.qiushibaike.com/HKI3TEPSQBEYYXRY_hd.jpg"
# content 返回数据的二进制码
image_data = requests.get(url).content
# wb, rb 都是以二进制的方式打开文件
fout = open("data/qiutu2.jpg", 'wb')
fout.write(image_data)
fout.close()

