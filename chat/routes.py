from chat.controllers import *


def register_routes(app):
    app.router.add_get('/', test, name='test-route')
