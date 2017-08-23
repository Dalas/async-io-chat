from chat.routes import register_routes

from aiohttp_swagger import setup_swagger
from aiohttp import web

import os


def create_app():
    app = web.Application()

    register_routes(app)
    setup_swagger(app, swagger_from_file=os.path.join(os.path.dirname(__file__), 'api.yaml'))

    return app


def run_app(app):
    web.run_app(app, port=8080)
