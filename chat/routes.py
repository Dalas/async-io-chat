import chat.controllers as views


def register_routes(app):
    app.router.add_get('/', views.main_page, name='test-route')

    # Auth
    app.router.add_get('/api/github-callback', views.github_auth_handler, name='github-auth-handler')
