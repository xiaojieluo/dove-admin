from server.handler import IndexHandler as Index
from server.handler import UserHandler as User

route = [
    ('/', Index.index),
    ('/index', Index.index),
    ('/login', User.login),
]
