from server.handler import BaseHandler
from sanic.response import text, html
from sanic import response
from server import utils

class login(BaseHandler):
    '''login'''
    async def get(self, requests):
        render = await self.render('login.html')
        return html(render)

    async def post(self, request):
        '''验证登陆'''
        settings = utils.load_conf('server')
        admin = settings.get('admin', dict())
        dove = settings.get('dove', dict())

        username = request.form.get('username', '') == admin.get('username', '')
        password = utils.md5(request.form.get('password', ''), salt=dove['salt']) \
                    == utils.md5(admin.get('password', ''), salt=dove['salt'])

        if username and password:
            cookie_prefix = dove.get('cookie_prefix', '')
            res = response.redirect('/')
            res.cookies[cookie_prefix+'username'] = admin.get('username', '')
            res.cookies[cookie_prefix+'password'] = utils.md5(admin.get('password', ''))
            return res
        else:
            return html('username or password verification failed, <a href="/login">back login</a>')
