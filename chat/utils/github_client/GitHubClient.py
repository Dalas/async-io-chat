from .Users import Users


class GitHubClient:

    def __init__(self, app):
        self._client = app

        self.users = Users(self._client)
