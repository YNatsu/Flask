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


def add():
    a = Article(title='aaa', content='bbb')
    db.session.add(a)
    db.session.commit()


def search():
    s = Article.query.filter(Article.id == 1)

    print(s)

    # SELECT article.id AS article_id, article.title AS article_title, article.content
    # AS article_content FROM article WHERE article.id = % s

    a = s.all()[0]  # a = s.first()

    print(a.title, a.content)

    # aaa bbb


def modify():
    article = Article.query.filter(Article.id == 1).first()
    article.title = 'ccc'
    db.session.commit()


def delete():
    article = Article.query.filter(Article.id == 1).first()
    db.session.delete(article)
    db.session.commit()


@app.route('/')
def index():
    delete()
    return 'Hello world'


app.run()
