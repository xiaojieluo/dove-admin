from server.handler.APIHandler import APIHandler
from sanic.response import json, text

class index(APIHandler):

    async def get(self, request):
        print("Hello")
        return text('hello world')
        # print(request.args.get('appid', None))
        # return json({'index':'indexs'})
