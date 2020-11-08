# selenium实现拖动操作

from selenium import webdriver

# 实例化一个浏览器对象
bro = webdriver.Chrome(executable_path="chromedriver")

# 发起一个url请求
url = "https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable"
bro.get(url)

# 切换标签定位的作用域
bro.switch_to.frame('iframeResult')
div = bro.find_element_by_id('draggable')

# 动作链
action = webdriver.ActionChains(bro)
# 点击长按
action.click_and_hold(div)

for i in range(5):
    # perform 立即执行
    action.move_by_offset(17, 0).perform()

# 释放动作链
action.release()

bro.quit()