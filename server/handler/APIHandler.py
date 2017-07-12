from sanic.views import HTTPMethodView

class APIHandler(HTTPMethodView):
    pass

    @classmethod
    async def authenticated(cls, request):
        '''
        权限认证
        '''
        auth = dict(
            appid = request.raw_args.get('appid', None),
            appkey = request.raw_args.get('appkey', None)
        )

        # return True
        # if request.raw_args.get('appid') is not  None and request.raw_args.get('appkey') is not None:
        #     if user.find(auth) is None:
        #         log.info('Unauthorized')
        #         return json({'msg':'Unauthorized'}, 401)
        # else:
        #     return json({'msg':'Unauthorized'}, 401)
