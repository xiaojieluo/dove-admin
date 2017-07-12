from server.handler import IndexHandler as Index

route = [
    ('/', Index.index),
    ('/index', Index.index),
]
