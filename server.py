from sanic import Sanic
from conf.settings import app_settings
from server.handler.APIHandler import APIHandler
from server import route

def make_app(name=__name__, route=route):
    app = Sanic(name)
    app.config.update(app_settings)

    # 循环导入 route
    for url, view in route:
        app.add_route(view.as_view(), url)

    # 注册中间件
    app.middleware(APIHandler.authenticated)

    return app

if __name__ == '__main__':
    app = make_app(__name__)
    app.run(host=app_settings.get('host', '127.0.0.1'),
            port=app_settings.get('port', 8888),
            workers=app_settings.get('workers', 1),
            debug=app_settings.get('debug', False),
            log_config=None
    )
