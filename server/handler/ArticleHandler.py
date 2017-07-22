from server.handler import BaseHandler
from sanic.response import json, text, html
import os
from dove import utils, Dove
from dove.app import Article

class index(BaseHandler):

    async def get(self, requests):

        articles = self.articles_model.get_articles()
        render = await self.render('articles/index.html', articles=articles)

        return html(render)

class update(BaseHandler):
    '''
    更新文章
    '''
    async def get(self, requests, article_id):
        article_id = str(article_id)
        article = self.articles_model.find_one({'id':article_id})
        render = await self.render('articles/update.html', article=article)
        return html(render)

    async def post(self, requests, article_id):
        print(requests.form)
        return text("update")

class delete(BaseHandler):
    '''删除'''
    async def post(self, requests):
        try:
            id_ = requests.form.get('id')[0]
        except Exception:
            return text('id 不正确， please don\'t hack')
        id_ = str(id_)
        article = self.articles_model.find_one({'id':id_})
        article.delete()
        self.articles_model.delete({'id':id_})

        return json({'result':True})
