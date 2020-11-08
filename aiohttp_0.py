# 多协程的基础操作
# requests不支持多协程，必须使用aiohttp
# 测试当前代码需要先运行自己的小型服务器，flask_0.py

import aiohttp
import asyncio
import time

start_time = time.time()

# async修饰的函数，调用后返回一个协程对象
async def request(url):
    print("calling", url)
    async with aiohttp.ClientSession() as session:
        async with await session.get(url) as response:
            # text() 返回字符串
            # read() 返回二进制数据
            # json() 返回json对象
            page_text = await response.text()
            print(page_text)

    
urls = ['http://127.0.0.1:5000/1', 'http://127.0.0.1:5000/2', 'http://127.0.0.1:5000/3']

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