from chat.credentials import GITHUB_CLIENT_ID, GITHUB_CLIENT_SECRET


async def github_auth_handler(request):
    print(request)
    code = request.GET.get('code', None)
    gh_client = request.app['gh_client']

    # TODO: Add custom exceptions
    if not code:
        raise Exception('Auth error')

    data = await gh_client.users.get_user_token(GITHUB_CLIENT_SECRET, GITHUB_CLIENT_ID, code)

    # TODO: add checks
    if 'access_token' not in data:
        pass

    res = await gh_client.users.get_auth_user(data['access_token'])
    print(res)

    #
    # user = self.prepare_github_data(user)
    #
    # user = yield Users.get_or_create_github_user({
    #     "username": "{0}_{1}".format(user['login'], user['id']),
    #     "email": user['email'],
    #     "avatar_url": user['avatar_url'],
    #     "github": user
    # })
    #
    # session = yield Sessions.update_or_create(user['_id'])
    #
    # self.set_secure_cookie('token', session['token'])
    # self.set_secure_cookie('gh_token', response['access_token'])
    #
    # self.redirect('/chat')
#
# def prepare_github_data(self, data):
#     return {
#         'avatar_url': data['avatar_url'],
#         'login': data['login'],
#         'full_name': data['name'],
#         'email': data['email'],
#         'id': data['id'],
#         'account_url': data['html_url']
#     }
