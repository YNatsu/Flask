# -*- encoding: utf-8 -*- 
# @Contact :  ynatsu233@outlook.com
# @Time    :  2019/4/26 16:51  
# @Author  :  Natsu Yuki

from flask import *

app = Flask(__name__)
app.secret_key = '233'


@app.route('/')
def index():
    return render_template('url_index.html')


@app.route('/login')
def login():
    return render_template('url_login.html')


app.run()
