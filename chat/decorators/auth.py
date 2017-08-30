from chat.models import SessionsModel

from aiohttp.web import HTTPFound


def login_required(func):

    async def wrapper(request, *args, **kwargs):
        print('here')
        token = request.cookies.get('token', None)
        if token:
            session = await SessionsModel.get(request.app['db'], {'token': token})
            # TODO: refactor this
            request.session = session
        else:
            return HTTPFound('/')

        return await func(request, *args, **kwargs)

    return wrapper
