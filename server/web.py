from jinja2 import Environment, PackageLoader, TemplateNotFound
import jinja2
import yaml
import os
from sanic import response


ROOT_PATH = os.getcwd()
CONF_PATH = os.path.join(ROOT_PATH, 'conf')

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
