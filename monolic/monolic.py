from flask import Flask, make_response
import requests
import json

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
    return json.dumps({'success': True}), 200, \
         {'ContentType': 'application/json'}

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