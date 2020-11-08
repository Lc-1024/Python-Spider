# 多协程的基础操作
# requests不支持多协程，必须使用aiohttp

import requests
import asyncio
import time

start_time = time.time()

# async修饰的函数，调用后返回一个协程对象
async def request(url):
    print("calling", url)
    # 如果异步协程中出现了同步模块的相关代码就无法实现同步
    # request.get是基于同步的，不能使用异步协程
    response = requests.get(url)
    print(url, "finished")
    
urls = ['www.baidu.com', 'www.sogou.com', 'www.google.com']

tasks = []
for url in urls:
    c = request(url)
    task = asyncio.ensure_future(c)
    tasks.append(task)

loop = asyncio.get_event_loop()
# 需要将任务list封装到wait中
loop.run_until_complete(asyncio.wait(tasks))


end_time = time.time()
cost_time = end_time - start_time
print(cost_time, 's')