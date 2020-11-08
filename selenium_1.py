# selenium实现浏览器操作

from selenium import webdriver

# 实例化一个浏览器对象
bro = webdriver.Chrome(executable_path="chromedriver")

# 发起一个url请求
url = "https://www.taobao.com/"
bro.get(url)

# 标签定位
search_input = bro.find_element_by_id('q')
# 标签交互
search_input.send_keys('iPhone')
# 点击搜索按钮
btn = bro.find_element_by_css_selector('.btn-search')
btn.click()

# 执行js程序
# bro.execute_script('window.scrollTo(0, document.body.scrollHeight)')

# 后退
bro.back()
# 前进
bro.forward()
# 退出
bro.quit()