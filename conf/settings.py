# dataabse configure
db_settings = dict(
    host = '127.0.0.1',
    port = 27017,
    database = 'gamerec'
)

app_settings = dict(
    host = '127.0.0.1',
    port = 8888,
    workers = 4,
    debug = False,
    # MOTOR_URI='mongodb://localhost:27017/gamerec',
)

api_settings = dict(
    pages = 1,
    # count = 20, # 默认返回20
)

settings = dict(
    host = '127.0.0.1',
    port = 8888,
    workers = 4,
    debug = True,
)
