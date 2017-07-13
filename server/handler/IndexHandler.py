from server.handler import BaseHandler
from sanic.response import json, text, html

class index(BaseHandler):

    async def get(self, request):
        render = await self.render('index.html', hello='world')
        return html(render)
