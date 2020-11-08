# 多协程的基础操作

import asyncio
import time

start_time = time.time()

# async修饰的函数，调用后返回一个协程对象
async def request(url):
    print("calling", url)
    # 如果异步协程中出现了同步模块的相关代码就无法实现同步
    # time.sleep(2)
    # 当在asyncio中遇到阻塞操作，必须手动挂起
    await asyncio.sleep(2)
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