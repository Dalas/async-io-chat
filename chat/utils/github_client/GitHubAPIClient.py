from .Users import Users


class GitHubAPIClient:

    def __init__(self, client):
        self._client = client

        self.users = Users(self._client)
