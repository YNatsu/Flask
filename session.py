# -*- encoding: utf-8 -*-
# @Contact :  ynatsu233@outlook.com
# @Time    :  2019/5/5 19:02
# @Author  :  Natsu Yuki


from flask import *
import os
from datetime import timedelta

app = Flask(__name__)

# 24 个字符

app.config['SECRET_KEY'] = os.urandom(24)

app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(days=7)


@app.route('/')
def index():
    session['usename'] = 'natsu'
    session.permanent = True
    return 'Hello World !'


@app.route('/get')
def get():
    return session.get('usename')


@app.route('/delete')
def delete():
    print(session.get('usename'))
    session.pop('usename')
    print(session.get('usename'))
    return 'success ！'


@app.route('/clear')
def clear():
    print(session.get('usename'))
    session.clear()
    print(session.get('usename'))
    return 'success ！'


if __name__ == '__main__':
    app.run(debug=True)
