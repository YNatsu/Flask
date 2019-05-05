# -*- encoding: utf-8 -*- 
# @Contact :  ynatsu233@outlook.com
# @Time    :  2019/5/5 19:15  
# @Author  :  Natsu Yuki

from flask_script import Manager

dbManager = Manager()


@dbManager.command
def init():
    print('database init ...')


@dbManager.command
def migrate():
    print('migrate success ... ')
