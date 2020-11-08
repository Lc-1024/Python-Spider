# selenium 实现无头浏览器以及规避检测

from selenium import webdriver
# 无头浏览器
from selenium.webdriver.chrome.options import Options
# 规避检测
from selenium.webdriver import ChromeOptions 

chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')

option = ChromeOptions()
option.add_experimental_option('excludeSwitches', ['enabel-automation'])
bro = webdriver.Chrome(executable_path='chromedriver', chrome_options=chrome_options, options=option)

bro.get('https://www.baidu.com')
print(bro.page_source)

bro.quit()
