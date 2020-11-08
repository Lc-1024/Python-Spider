# 使用线程池进行多线程操作

import time
from multiprocessing.dummy import Pool

start_time = time.time()

def wait(n, t=2):
    print(n, 'start')
    time.sleep(t)
    print(n, 'end\n')
name = [1,2,3,4]



pool = Pool(4)
pool.map(wait, name)
pool.close()
pool.join()


end_time = time.time()
cost_time = end_time - start_time
print(cost_time, 's')


