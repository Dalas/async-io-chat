from chat.routes import register_routes
from chat.utils.github_client import GitHubClient
from chat.db import setup_db

from aiohttp_swagger import setup_swagger
from aiohttp import web, ClientSession

import asyncio
import os


def prepare_client(app):
    app['client'] = ClientSession(loop=app.loop)


def prepare_gh_client(app):
    app['gh_client'] = GitHubClient(app['client'])


def create_app():
    loop = asyncio.get_event_loop()
    app = web.Application(loop=loop, middlewares=[])

    register_routes(app)
    prepare_client(app)
    prepare_gh_client(app)
    setup_db(app)

    setup_swagger(app, swagger_from_file=os.path.join(os.path.dirname(__file__), 'api.yaml'))

    return app


def run_app(app):
    web.run_app(app, port=8080)
