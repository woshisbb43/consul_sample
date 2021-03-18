from flask import Flask
import requests,json

app = Flask(__name__)

# 原本只需要调用内部方法： get_1() 和 get_2()
@app.route('/foo_give_1plus2', methods=['GET'])
def foo_give_1plus2():
    return str(request_1() + request_2())

# 现在需要通过ip+端口去寻找这个服务， 当然也可以通过配置域名去寻找这个服务
def request_1():
    res = requests.get('http://127.0.0.1:8081/foo_give_1')
    return int(res.text)

def request_2():
    res = requests.get('http://127.0.0.1:8082/foo_give_2')
    return int(res.text)

# 发现目标服务
@app.route('/get_service_foo1')
def discover_service():
    res = requests.get('http://127.0.0.1:8500/v1/catalog/service/foo1')
    return res.text

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8083, debug=True)