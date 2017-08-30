from .Users import Users


class GitHubClient:

    def __init__(self, client):
        self._client = client

        self.users = Users(self._client)
