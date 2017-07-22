from server.database import DatabaseFactory
from dove.settings import Setting
from dove.app import Article

class Articles_model(object):
    '''
    模型类
    '''
    __table__ = 'Articles'

    def __init__(self, dove):
        '''
        dove : dove 实例
        '''
        self.dove = dove
        conf = Setting('server')
        self.db = DatabaseFactory(**conf.database)

    def init(self):
        '''
        初始化数据库
        1. 创建 Articles 表
        2. 扫描博客源文件存储目录，并存入 Articles 表中
        '''
        self.db.create_table(self.__table__, {'id':'integer primary key', 'path':'varchar(20)'})
        # 从 dove 获取所有文章源文件，并存入数据库
        for k in self.dove.articles:
            attr = {'path':k.path}
            if not self.db.find(self.__table__, attr):
                self.db.insert(self.__table__, attr)

    def get_articles(self, attr=None):
        '''
        获取文章
        '''
        if attr is None:
            result = self.db.find(self.__table__, '*')
        else:
            result = self.db.find(self.__table__, attr)

        articles = []
        for k in result:
            post = Article(k[1])
            post.id = k[0]
            articles.append(post)

        return articles

    def find_one(self, attr):
        '''
        返回一个文档
        '''
        result = self.get_articles(attr)

        if len(result) > 0:
            return result[0]
        else:
            return None

    def get_articles_num(self):
        '''
        返回所有文章数目
        '''
        num = len(self.get_articles())
        return num

    def delete(self, where=None):
        '''删除'''
        if where is not None:
            result = self.db.delete(self.__table__, where)
        else:
            result = False
        print("result:{}".format(result))
        return result
