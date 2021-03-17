from flask import Flask
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


def get_1():
    return 1


def get_2():
    return 2


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)