from flask import Flask
import requests,json

app = Flask(__name__)

# 原本只需要调用内部方法： get_1() 和 get_2()
@app.route('/foo_give_1plus2', methods=['GET'])
def foo_give_1plus2():
    return '返回1+2的结果： '+ str(request_1() + request_2())

def request_1():
    # 请求foo1提供数字1
    try:
        req_url = 'http://{}/foo_give_1'.format(get_service_foo1_info(0))
        res = requests.get(req_url)
        # print('使用foo1 节点0 的数据')
    except requests.exceptions.RequestException as e:
        req_url = 'http://{}/foo_give_1'.format(get_service_foo1_info(1))
        res = requests.get(req_url)
        # print('使用foo1 节点1 的数据')
    return int(res.text)

# 现在需要通过ip+端口去寻找这个服务， 当然也可以通过配置域名去寻找这个服务
def request_2():
    # 请求foo2提供数字2
    res = requests.get('http://127.0.0.1:8082/foo_give_2')
    return int(res.text)

# 发现目标服务
@app.route('/get_service_foo1')
def discover_service():
    res = requests.get('http://127.0.0.1:8500/v1/catalog/service/foo1')
    return res.text

def get_service_foo1_info(index):
    res = requests.get('http://127.0.0.1:8500/v1/catalog/service/foo1')
    service_foo1_info = json.loads(res.text)
    foo1_url = service_foo1_info[index]['ServiceAddress']
    foo1_port = service_foo1_info[index]['ServicePort']
    return foo1_url + ':' + str(foo1_port)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8083, debug=True)