from flask import Flask
import requests,json

app = Flask(__name__)

@app.route('/foo_give_1', methods=['GET'])
def foo_give_1():
    return str(get_1())

@app.route('/foo_give_2', methods=['GET'])
def foo_give_2():
    return str(get_2())

@app.route('/foo_give_1plus2', methods=['GET'])
def foo_give_1plus2():
    return str(get_1() + get_2())

@app.route('/health', methods=['GET'])
def check_health():
    return json.dumps({'success':True}), 200, {'ContentType':'application/json'} 

def get_1():
    return 1

def get_2():
    return 2

# def register():
#     payload = {    
#         "name": 'test',
#         "port": 8080,
#         "check": {
#             "deregistercriticalserviceafter": '90m',
#             "http": "http://127.0.0.1:8080/health",
#             "interval": '10s'
#             }
#     }
#     try:
#         res = requests.put('http://127.0.0.1:8500/v1/agent/service/register', data=payload)
#     except requests.exceptions.RequestException as e:
#         print(e)
#     print(res)
#     print(res.text)

if __name__ == '__main__':
    # register()
    app.run(host='0.0.0.0', port=8080, debug=True)