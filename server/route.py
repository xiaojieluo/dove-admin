from server.handler import IndexHandler as Index
from server.handler import UserHandler as User
from server.handler import ArticleHandler as Article

route = [
    (r'/', Index.index),
    (r'/index', Index.index),
    (r'/login', User.login),
    (r'/logout', User.logout)
]

route += [
    (r'/articles', Article.index),
    (r'/articles/update/<article_id:int>', Article.update),
    (r'/articles/delete', Article.delete)
]
