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


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)


class Article(db.Model):
    __tablename__ = 'article'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)

    author_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    author = db.relationship('User', backref=db.backref('articles'))

    # 可进行如下创建

    # a = Article(title='a', content='b')
    # a.author = User.query.filter(User.id == 1).first()


db.create_all()


def add():
    a = Article(title='aaa', content='bbb')
    db.session.add(a)
    db.session.commit()


def search():
    # 单表查询

    s = Article.query.filter(Article.id == 1)

    print(s)

    # SELECT article.id AS article_id, article.title AS article_title, article.content
    # AS article_content FROM article WHERE article.id = % s

    a = s.all()[0]  # a = s.first()

    print(a.title, a.content)

    # aaa bbb

    # 多表查询

    # 必需设置 relationship

    # Article => User

    a = Article.query.filter(Article.id == 1).first()

    print(a.author.name)

    # User => Article

    u = User.query.filter(User.id == 1).first()

    print(u.articles)


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
    return 'Hello world'


app.run()
