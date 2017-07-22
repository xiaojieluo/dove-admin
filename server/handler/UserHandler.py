from server.handler import BaseHandler
from sanic.response import text, html
from sanic import response
from server import utils

class login(BaseHandler):
    '''login'''
    async def get(self, requests):
        render = await self.render('login.html')
        return html(render)

    async def post(self, requests):
        '''验证登陆'''
        settings = utils.load_conf('server')
        admin = settings.get('admin', dict())
        dove = settings.get('dove', dict())

        username = requests.form.get('username', '') == admin.get('username', '')
        password = utils.md5(requests.form.get('password', ''), salt=dove['salt']) \
                    == utils.md5(admin.get('password', ''), salt=dove['salt'])

        if username and password:
            cookie_prefix = dove.get('cookie_prefix', '')
            res = response.redirect('/')
            res.cookies[cookie_prefix+'username'] = admin.get('username', '')
            # res.cookies[cookie_prefix+'username']['max-age'] = 60
            res.cookies[cookie_prefix+'password'] = utils.md5(admin.get('password', ''))
            # res.cookies[cookie_prefix+'password']['max-age'] = 60
            return res
        else:
            return html('username or password verification failed, <a href="/login">back login</a>')

class logout(BaseHandler):
    '''退出'''
    async def get(self, requests):
        res = response.redirect('/')
        cookie_prefix = utils.load_conf('server')['dove']['cookie_prefix']
        del res.cookies[cookie_prefix+'username']
        del res.cookies[cookie_prefix+'password']
        return res
