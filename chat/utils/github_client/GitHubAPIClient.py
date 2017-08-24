from .Users import Users


class GitHubAPIClient:

    def __init__(self, app):
        self._client = app

        self.users = Users(self._client)
