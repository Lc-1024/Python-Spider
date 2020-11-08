# 建立一个简单的服务器用于访问

from flask import Flask
import time

app = Flask(__name__)

@app.route('/1')
def index_1():
    time.sleep(2)
    return "1 is called"

@app.route('/2')
def index_2():
    time.sleep(2)
    return "2 is called"
    
@app.route('/3')
def index_3():
    time.sleep(2)
    return "3 is called"

if __name__ == '__main__':
    app.run(threaded=True)