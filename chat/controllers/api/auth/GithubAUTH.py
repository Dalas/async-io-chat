from chat.credentials import GITHUB_CLIENT_ID, GITHUB_CLIENT_SECRET
from chat.models import UsersModel, SessionsModel
from chat.exceptions import BadRequest, ExternalServiceError

from aiohttp.web import HTTPFound


async def github_auth_handler(request):
    code = request.GET.get('code', None)
    gh_client = request.app['gh_client']
    db = request.app['db']

    if not code:
        raise BadRequest('Missed GitHub authentication code!')

    data = await gh_client.users.get_user_token(GITHUB_CLIENT_SECRET, GITHUB_CLIENT_ID, code)

    if 'access_token' not in data:
        raise ExternalServiceError('GitHub authentication failure!')

    res = await gh_client.users.get_auth_user(data['access_token'])

    user = await UsersModel.get_or_create_user_by_gh_user(db, res)
    session = await SessionsModel.update_or_create_session(db, user['_id'])

    # TODO: change this

    response = HTTPFound('/chat')
    response.set_cookie('token', session['token'], secure=True)
    return response
