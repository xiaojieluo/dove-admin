import sqlite3

class DatabaseError(Exception):
    pass

class Database(object):
    '''
    数据库抽象接口， 所有继承 Database 的类都必须实现类中的方法
    '''

    def __init__(self,user=None, password=None, **kw):
        self.user = user or kw.get('user')
        self.password = password or kw.get('password')
        self.init(**kw)

    def init(self, **kw):
        '''
        做一些初始化数据库的准备工作
        1. 检查数据库是否存在
        2. 连接数据库，存储连接句柄
        '''
        raise NotImplementedError()

    def connect(self):
        raise NotImplementedError()

    def cursor(self):
        raise NotImplementedError()

    def create(self, *args, **kw):
        '''创建'''
        raise NotImplementedError()

    def find(self, *args, **kw):
        '''查询'''
        raise NotImplementedError()

    def update(self, *args, **kw):
        '''更新'''
        raise NotImplementedError()

    def delete(self, *args, **kw):
        '''删除'''
        raise NotImplementedError()

    def __del__(self):
        '''析构函数'''
        # 关闭数据库连接
        # 关闭数据库句柄
        pass

class Sqlite(Database):

    def init(self, **kw):
        self.db_file = kw.get('db_file')
        self.connect = sqlite3.connect(self.db_file)
        self.cursor = self.connect.cursor()
        self.init = "Init"

    def create_table(self, tbl_name, var):
        '''
        如果指定表不存在，就创建
        '''
        attr = str()
        for k, v in var.items():
            attr += k+' '+v+','

        sql = 'create table if not exists {table_name}({attr})'.format(table_name=tbl_name, attr=attr[:-1])
        self.cursor.execute(sql)
        # data = self.run(sql)

    # def run(self, sql):
    #     data = self.cursor.execute(sql)
    #
    #     return data

    def insert(self, tbl_name, var):
        '''插入'''
        key, value = str(), str()
        for k, v in var.items():
            key +=   str(k) +', '
            value += '"' + str(v) +'", '
        sql = 'insert into {tbl_name} ({key}) values ({value})'.format(tbl_name=tbl_name, value=value[:-2], key=key[:-2])
        # sql = 'insert into Article values (1, "fuck.md")'
        self.cursor.execute(sql)
        return self.cursor.fetchone()

    def find(self, tbl_name, var="*"):
        if var == '*':
            sql = 'select * from {tbl_name}'.format(tbl_name=tbl_name)
        else:
            attr = ' where '
            for k, v in var.items():
                attr += k+'="'+v+'",'
            sql = 'select * from {tbl_name}{attr}'.format(tbl_name=tbl_name, attr=attr[:-1])
        print(sql)
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    def delete(self, tbl_name, var):
        attr = str()
        for k, v in var.items():
            attr += k+'="'+v+'",'
        sql = 'delete from {tbl_name} where {attr}'.format(tbl_name=tbl_name, attr=attr[:-1])
        print(sql)
        self.cursor.execute(sql)
        return self.cursor.fetchall()


    def __del__(self):
        self.connect.commit()
        self.cursor.close()
        self.connect.close()

class Mysql(Database):
    pass


# 工厂模式，生成具体类
def DatabaseFactory(*args, **kw):
    '''
    没有用到 *args, 不过为了以后的拓展，先留着
    '''
    databases = {}
    databases['mysql'] = lambda *args, **kw: Mysql(*args, **kw)
    databases['sqlite'] = lambda *args, **kw: Sqlite(*args, **kw)

    engine = kw.get('engine')

    if engine in databases:
        configure = kw.get(engine)
        return databases[engine](*args, **configure)
    else:
        raise DatabaseError('指定的数据库：{} 暂不支持'.format(engine))

if __name__ == '__main__':
    d = DatabaseFactory(engine='sqlite', sqlite={'db_file':'test.db'})
    d.create_table('Article', {'id':'integer primary key', 'path':'varchar(20)'})
    # sss = d.insert('Article', {'path':'fucks.md'})
    d.delete('Article', {'id':'3'})
    print(d.find('Article'))
    # print(d.cursor.rowcount)
