from flask import Flask
from gevent import pywsgi

app = Flask(__name__)
@app.route('/test', methods=['get','post'])
def index():
    page = open(file_name, encoding='utf-8')
    res = page.read()
    return res

@app.route('/test1', methods=['get','post'])
def index_1():
    page = open(file, encoding='utf-8')
    res = page.read()
    return res


server = pywsgi.WSGIServer(('127.0.0.1', 5000), app)
server.serve_forever()