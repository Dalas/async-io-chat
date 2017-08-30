

class Users:
    base_url = 'https://api.github.com/'

    def __init__(self, client):
        self._client = client

    async def get_user_token(self, gcs, gci, code):
        url = "https://github.com/login/oauth/access_token"

        data = {
            "client_secret": gcs,
            "client_id": gci,
            "code": code
        }

        headers = {
            "Accept": "application/json",
            "X-OAuth-Scopes": "user",
            "X-Accepted-OAuth-Scopes": "user"
        }

        async with self._client.get(url, data=data, headers=headers) as resp:
            assert resp.status == 200
            data = await resp.json()

        return data

    async def get_auth_user(self, token):
        headers = {
            'Authorization': f'token {token}'
        }

        async with self._client.get(self.base_url + 'user', headers=headers) as resp:
            # TODO: add status checking
            data = await resp.json()

        return data
