# 协程的基础操作

import asyncio

# async修饰的函数，调用后返回一个协程对象
async def request(url):
    print("calling", url)
    print(url, "finished")
    return url
c = request("www.baidu.com")

loop = asyncio.get_event_loop()

# 将协程对象加入到loop中，然后运行
# loop.run_until_complete(c)
'''
# task的使用，基于loop
task = loop.create_task(c)
print(task)
loop.run_until_complete(task)
print(task)

# future的使用，基于asynico
task = asyncio.ensure_future(c)
print(task)
loop.run_until_complete(task)
print(task)
'''

def call_back(task):
    # result中返回的就是任务对象中的协程对象函数的返回值，即c的返回值
    print(task.result())

# 绑定回调
task = asyncio.ensure_future(c)
task.add_done_callback(call_back)
loop.run_until_complete(task)


