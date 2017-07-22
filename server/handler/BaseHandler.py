from sanic.views import HTTPMethodView
from jinja2 import TemplateNotFound
from sanic import response
from server import utils
from server.web import Template, Cookie, Database
import functools
from dove import Dove
import os
from server.database import DatabaseFactory
from dove.settings import Setting
from server.model import Articles_model


class BaseHandler(HTTPMethodView):

    def __init__(self):
        dove_conf = Setting('dove')

        # dove 实例
        self.dove = Dove(settings=dove_conf)
        self.cookie = Cookie()

        self.articles_model = Articles_model(self.dove)
        self.articles_model.init()

    @classmethod
    async def authenticated(cls, request):
        '''
        权限认证
        '''
        if utils.load_conf('server').get('login_verification', False) is True:
            settings = utils.load_conf('server')
            admin = settings.get('admin', dict())
            dove = settings.get('dove', dict())

            prefix = settings.get('dove', dict()).get('cookie_prefix', '')
            cookies = request.cookies.get
            username = cookies(prefix+'username', '')
            password = cookies(prefix+'password', '')


            if (username and password) is not None and request.path != '/login' and request.path[:8] != '/static/':
                # 偏函数
                md5 = functools.partial(utils.md5, salt=dove['salt'])
                if username != admin.get('username', '')  \
                    and md5(password) != md5(admin.get('password', '')):
                    return response.redirect('/login')

                    # username = cookies(prefix+'username') == admin.get('username', '')
                    # password = utils.md5(cookies(prefix+'password'), salt=dove['salt']) \
                    #             == utils.md5(admin.get('password', ''), salt=dove['salt'])
                    #
                    # print(username)
                    # print(password)
            # if (username or password) is False:
            #     if request.path != '/login' and request.path[:8] != '/static/':


    async def render(self, tpl_name, **kw):
        '''模板'''
        tmp = Template()
        # try:
        return tmp.render(tpl_name, **kw)
        # except TemplateNotFound:
        #     return response.redirect('/error')

        # return True
        # if request.raw_args.get('appid') is not  None and request.raw_args.get('appkey') is not None:
        #     if user.find(auth) is None:
        #         log.info('Unauthorized')
        #         return json({'msg':'Unauthorized'}, 401)
        # else:
        #     return json({'msg':'Unauthorized'}, 401)
