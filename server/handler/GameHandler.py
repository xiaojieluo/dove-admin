from handler.APIHandler import APIHandler
from sanic.response import json
from web import log
from model import Game
from settings import api_settings

class index(APIHandler):

    async def get(self, request):
        log.info(request.args)

        # args = request.args


        # if args.get('pages', None) is not None:
        #     try:
        #         args['pages'] = int(args.get('pages'))
        #     except ValueError:
        #         break

        game = Game()
        data = game.find({}).skip(0).limit(0)
        games = list()
        for k in data:
            k['_id'] = str(k['_id'])
            games.append(k)
        log.info(games)
        # log.info(game.find({}).skip(), limit(5))
        return json(games)

    async def post(self, request):
        '''
        新增游戏
        '''
        game = Game()
        # print(type(request.json))
        result = game.replace_one(request.json, request.json, True)
        print(result.matched_count)
        print(result.modified_count)
        return json(request.json, 201)
