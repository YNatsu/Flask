# -*- encoding: utf-8 -*- 
# @Contact :  ynatsu233@outlook.com
# @Time    :  2019/5/5 19:03  
# @Author  :  Natsu Yuki

# pip install Flask-Script

from flask_script import Manager

# 本地文件

from flaskScript import app
from dbScripts import dbManager
from flask_migrate import Migrate, MigrateCommand
from exts import db
from models_sql import Book

manager = Manager(app=app)
migrate = Migrate(app=app, db=db)

manager.add_command('db', MigrateCommand)

# python manage.py db init
# python manage.py db migrate
# python manage.py db upgrade


@manager.command
def runserver():
    print('running ...')


# python manage.py runserver


manager.add_command('dbM', dbManager)

# python manage.py dbM init

manager.run()
