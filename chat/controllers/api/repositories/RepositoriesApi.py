from chat.decorators import login_required


@login_required
async def my_repositories(request):
    repositories = await request.app['gh_client'].repos.get_current_users_repositories(request.session['gh_token'])

    return repositories, 200
