from flask import Flask
import requests,json

# 原本只需要调用内部方法： get_1() 和 get_2()
@app.route('/foo_give_1plus2', methods=['GET'])
def foo_give_1plus2():
    return str(get_1() + get_2())

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8083, debug=True)