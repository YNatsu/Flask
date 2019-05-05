# -*- encoding: utf-8 -*- 
# @Contact :  ynatsu233@outlook.com
# @Time    :  2019/5/5 19:03  
# @Author  :  Natsu Yuki

# pip install Flask-Script

from flask_script import Manager

# 本地文件

from flaskScript import app
from dbScripts import dbManager

manager = Manager(app=app)


@manager.command
def runserver():
    print('running ...')


# python manage.py runserver

manager.add_command('db', dbManager)

# python manage.py db init

manager.run()
