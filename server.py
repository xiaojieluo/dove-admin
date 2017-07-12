from sanic import Sanic
from server.handler.APIHandler import APIHandler
from server import utils, route

def make_app(name=__name__, route=None, settings=None):
    app = Sanic(name)
    app.config.update(settings)

    # 循环导入 route
    for url, view in route:
        app.add_route(view.as_view(), url)

    # 注册中间件
    app.middleware(APIHandler.authenticated)

    return app

if __name__ == '__main__':
    server_settings = utils.load_conf('server')
    app = make_app(__name__, route=route, settings=server_settings)
    app.run(host=server_settings.get('host', '127.0.0.1'),
            port=server_settings.get('port', 8888),
            workers=server_settings.get('workers', 1),
            debug=server_settings.get('debug', False),
            log_config=None
    )
