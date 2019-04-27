# -*- encoding: utf-8 -*- 
# @Contact :  ynatsu233@outlook.com
# @Time    :  2019/4/26 10:47  
# @Author  :  Natsu Yuki

from flask import *

app = Flask(__name__)
app.secret_key = '233'


@app.route('/')
def index():
    flash('404 Not Found !')
    return render_template('exception.html')


@app.route('/login', methods=['POST'])
def login():
    form = request.form
    name = form.get('name')
    password = form.get('password')

    print(name, password)
    if not name:
        flash('Please input name !')
        return render_template('exception.html')
    if not password:
        flash('Please input password !')
        return render_template('exception.html')

    if name == 'natsu' and password == '233':
        flash('successful !')
        return render_template('exception.html')
    else:
        flash('Name or password is falure !')
        return render_template('exception.html')


@app.errorhandler(404)
def not_found(e):
    return render_template('404.html')


if __name__ == '__main__':
    app.run()
