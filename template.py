# -*- encoding: utf-8 -*- 
# @Contact :  ynatsu233@outlook.com
# @Time    :  2019/4/26 10:17  
# @Author  :  Natsu Yuki

from flask import *
from models import User

app = Flask(__name__)


@app.route('/')
def index():
    context = 'hello world'
    return render_template('index.html', context=context)


@app.route('/user')
def user_index():
    user = User('natsu', 233)
    return render_template('user_index.html', user=user)


@app.route('/query_user/<int:id>')
def query_user(id):
    user = None
    if id == 1:
        user = User('natsu', 233)
    return render_template('user_id.html', user=user)


@app.route('/users')
def user_list():
    users = []
    for i in range(10):
        user = User('natsu_' + str(i), i)
        users.append(user)
    return render_template('user_list.html', users=users)


@app.route('/one')
def one():
    return render_template('one_base.html')


@app.route('/two')
def two():
    return render_template('two_base.html')


if __name__ == '__main__':
    app.run()
