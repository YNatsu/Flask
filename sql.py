# -*- encoding: utf-8 -*- 
# @Contact :  ynatsu233@outlook.com
# @Time    :  4/27/2019 10:49 AM  
# @Author  :  Natsu Yuki


# pip install mysqlclient
# pip install flask_sqlalchemy

from flask import *
from flask_sqlalchemy import SQLAlchemy
import config

app = Flask(__name__)

app.config.from_object(config)
db = SQLAlchemy(app=app)


class Article(db.Model):
    __tablename__ = 'article'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)


db.create_all()


@app.route('/')
def index():
    return render_template('index.html')


app.run()
