from jinja2 import Environment, PackageLoader, TemplateNotFound
import jinja2
import yaml
import os
from sanic import response
import sqlite3

class Cache(object):
    '''
    刷新缓存
    1. 更新 content 目录下的文件到数据库
    dove 没有删除文件操作
    '''
    def __init__(self):
        pass

    def update(self):
        pass

class Database(object):
    '''sqlite3'''

    def __init__(self, path=""):
        # self.settings = settings
        # self.filename = os.path.join(self.settings.get('path'), self.settings.get('filename'))
        self.path = path
        self.init()

    def init(self):
        '''
        当数据库不存在时初始化数据库
        '''
        if not os.path.exists(self.path):
            self.run('create table articles (id varchar(20) primary key, path varchar(30))')

    @property
    def connect(self):
        return sqlite3.connect(self.path)

    @property
    def cursor(self):
        return self.connect.cursor()

    def __del__(self):
        self.cursor.close()
        self.connect.close()

    def insert(self, sql):
        return self.run(sql)

    def run(self, sql):
        '''运行 sql 语句'''
        self.cursor.execute(sql)
        return self.cursor.fetchall()

class Template(object):
    '''
    模板类
    '''
    def __init__(self):
        self.env = Environment(loader=PackageLoader('server', 'templates'))

    def render(self, tpl_name, **kw):
        '''渲染模板'''
        try:
            template = self.env.get_template(tpl_name)
        except TemplateNotFound:
            template = jinja2.Template('oops, some error: {} not found'.format(tpl_name))
            return template.render()

        return template.render(**kw)

class Cookie(object):
    '''sanic 的 cookie 封装'''
    _keys = {
        "expires": "expires",
        "path": "Path",
        "comment": "Comment",
        "domain": "Domain",
        "max-age": "Max-Age",
        "secure": "Secure",
        "httponly": "HttpOnly",
        "version": "Version",
    }
    def __init__(self):
        pass
    def write(self, res, key, value, **kw):
        ''' 写入 cookies '''

        # res =

        # key = response.redirect('/')
        res.cookies[key] = value
        return res

    def delete(self):
        '''删除 cookie '''
        pass
