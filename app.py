from flask import Flask, request, url_for

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World !'


@app.route('/user/<int:id>', methods=['POST', 'GET'])
def user_id(id):
    return 'user id : %s' % id


@app.route('/query_user')
def query_user():
    id = request.args.get('id')
    return 'user id : %s' % id


@app.route('/query_url')
def query_url():
    return 'query url: ' + url_for('user_id', id=233)   # 翻转 url


if __name__ == '__main__':
    app.run(debug=True)
