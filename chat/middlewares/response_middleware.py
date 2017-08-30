from chat.exceptions import BaseResponseException

from aiohttp.web import Response, json_response


async def response_middleware(app, handler):

    async def middleware_handler(request):
        try:
            response = await handler(request)

            if isinstance(response, Response):
                return response
            else:
                data, status = response
                return json_response({'data': data, 'error': {}}, status=status)

        except BaseResponseException as e:
            return json_response({'data': {}, 'error': e.error}, status=e.status)

        except Exception as e:
            print(e)  # TODO: add normal logger
            return json_response({'data': {}, 'error': {'code': 1000, 'message': 'Internal server error!'}}, status=500)

    return middleware_handler
