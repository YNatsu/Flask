# -*- encoding: utf-8 -*- 
# @Contact :  ynatsu233@outlook.com
# @Time    :  4/27/2019 10:52 AM  
# @Author  :  Natsu Yuki

dialect = 'mysql'
driver = 'mysqldb'
usename = 'root'
password = '123456'
host = '127.0.0.1'
port = '3306'
database = 'db_demo_1'

SQLALCHEMY_DATABASE_URI = '{}+{}://{}:{}@{}:{}/{}?charset=utf8'.format(
    dialect, driver, usename, password, host, port, database
)

SQLALCHEMY_TRACK_MODIFICATIONS = False


