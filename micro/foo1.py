from flask import Flask
import requests,json

app = Flask(__name__)

@app.route('/foo_give_1', methods=['GET'])
def foo_give_1():
    return str(get_1())

def get_1():
    return 1


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8081, debug=True)