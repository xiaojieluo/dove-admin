from sanic import Sanic
from server.handler import BaseHandler
from server import utils, route
from dove.settings import Setting
# from server.settings import Setting

def make_app(name=__name__, route=None, settings=None):
    app = Sanic(name)
    app.config.update(settings)

    # 循环导入 route
    for url, view in route:
        app.add_route(view.as_view(), url)

    # 注册中间件
    app.middleware(BaseHandler.authenticated)

    return app

if __name__ == '__main__':
    server_conf = Setting('server')
    app = make_app(__name__, route=route, settings=server_conf.data)
    # Serves files from the static folder to the URL /static
    app.static('/static', './server/static')
    app.run(host=server_conf.host or '127.0.0.1',
            port=server_conf.port or 8888,
            workers=server_conf.workers or 1,
            debug=server_conf.debug or False,
            log_config=None
    )
