# -*- encoding: utf-8 -*- 
# @Contact :  ynatsu233@outlook.com
# @Time    :  2019/5/5 19:25  
# @Author  :  Natsu Yuki

from exts import db


class Book(db.Model):
    __tablename__ = 'book'
    id = db.Column(db.Integer,primary_key=True)
    title = db.Column(db.String(10),primary_key=True)



