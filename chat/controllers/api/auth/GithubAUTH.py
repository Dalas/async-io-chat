from chat.credentials import GITHUB_CLIENT_ID, GITHUB_CLIENT_SECRET
from chat.models import UsersModel, SessionsModel

from aiohttp.web import HTTPFound


async def github_auth_handler(request):
    print(request)
    code = request.GET.get('code', None)
    gh_client = request.app['gh_client']

    # TODO: Add custom exceptions
    if not code:
        raise Exception('Auth error')

    data = await gh_client.users.get_user_token(GITHUB_CLIENT_SECRET, GITHUB_CLIENT_ID, code)

    # TODO: Add custom exceptions
    if 'access_token' not in data:
        raise Exception('GitHub auth error')

    res = await gh_client.users.get_auth_user(data['access_token'])

    user = await UsersModel.get_or_create_user_by_gh_user(request.app['db'], res)
    session = await SessionsModel.update_or_create_session(request.app['db'], user['_id'])

    # TODO: change this
    response = HTTPFound('/chat')
    response.set_cookie('token', session['token'], secure=True)
    return response
