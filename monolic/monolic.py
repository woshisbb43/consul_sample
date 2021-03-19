from flask import Flask, make_response
import requests
import json

app = Flask(__name__)

maintain = 'true'

@app.route('/foo_give_1', methods=['GET'])
def foo_give_1():
    if maintain == 'true':
        return '服务不可用'
    return '返回数值' + str(get_1())


@app.route('/foo_give_2', methods=['GET'])
def foo_give_2():
    if maintain == 'true':
        return '服务不可用'
    return '返回数值' + str(get_2())


@app.route('/foo_give_1plus2', methods=['GET'])
def foo_give_1plus2():
    if maintain == 'true':
        return '服务不可用'
    return '返回1+2的结果： ' + str(get_1() + get_2())


@app.route('/health', methods=['GET'])
def check_health():
    return json.dumps({'success': True}), 200, \
         {'ContentType': 'application/json'}

@app.route('/maintain')
def switch_maintain():
    global maintain
    if maintain == 'true':
        maintain = 'false'
    else:
        maintain = 'true'
    return maintain

@app.route('/service_register')
def service_register():
    url = "http://127.0.0.1:8500/v1/agent/service/register?replace-existing-checks=true"

    payload={  "ID": "monolic2",  "Name": "monolic4",  "Tags": [ "v1"],  "Address": "127.0.0.1",   "Port": 8080 }
    headers = {
        'Content-Type': 'application/json'
    }

    response = requests.request("PUT", url, headers=headers, data=json.dumps(payload))

    return str(response.status_code)
    

def get_1():
    return 1


def get_2():
    return 2


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)