from server.handler import BaseHandler
from sanic.response import json, text, html
import os
from dove import utils, Dove
from server.utils import dump

class index(BaseHandler):

    async def get(self, request):
        article_num = self.articles_model.get_articles_num()
        print(article_num)
        # print(self.db)
        # self.db.insert('create table articles (id varchar(20) primary key, path varchar(30))')
        render = await self.render('index.html', article_num = article_num)

        return html(render)
