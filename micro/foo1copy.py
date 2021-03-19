from flask import Flask
import requests,json

app = Flask(__name__)

@app.route('/foo_give_1', methods=['GET'])
def foo_give_1():
    return str(get_1())

@app.route('/health', methods=['GET'])
def check_health():
    return json.dumps({'success': True}), 200, \
         {'ContentType': 'application/json'}

@app.route('/service_register')
def service_register():
    url = "http://127.0.0.1:8500/v1/agent/service/register?replace-existing-checks=true"

    payload = {
        "ID": "foo1_cp",
        "Name": "foo1",
        "Tags": ["v1"],
        "Check": {
            "DeregisterCriticalServiceAfter": "90m",
            "HTTP": "http://127.0.0.1:8091/health",
            "Interval": "3s",
            "Timeout": "5s"
        },
        "Address": "127.0.0.1",
        "Port": 8091
    }
    headers = {
        'Content-Type': 'application/json'
    }

    response = requests.request("PUT", url, headers=headers, data=json.dumps(payload))

    return str(response.status_code)

def get_1():
    return 1


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8091, debug=True)