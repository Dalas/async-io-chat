from .Users import Users
from .Repositories import Repositories


class GitHubAPIClient:

    def __init__(self, client):
        self._client = client

        self.users = Users(self._client)
        self.repos = Repositories(self._client)
