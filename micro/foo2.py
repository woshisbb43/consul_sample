from flask import Flask
import requests,json

app = Flask(__name__)

@app.route('/foo_give_2', methods=['GET'])
def foo_give_2():
    return str(get_2())

def get_2():
    return 2

    
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8082, debug=True)