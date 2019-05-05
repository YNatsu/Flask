# -*- encoding: utf-8 -*- 
# @Contact :  ynatsu233@outlook.com
# @Time    :  2019/5/5 19:02  
# @Author  :  Natsu Yuki


from flask import *
from exts import db
from models_sql import Book
import config

app = Flask(__name__)

app.config.from_object(config)

db.init_app(app)


@app.route('/')
def index():
    return 'Hello World !'


if __name__ == '__main__':
    app.run(debug=True)
