

class Users:
    base_url = 'https://api.github.com/'

    def __init__(self, client):
        self._client = client

    async def get_auth_user(self, token):
        headers = {
            'Authorization': f'token {token}'
        }

        async with self._client.get(self.base_url + 'user', headers=headers) as resp:
            # TODO: add status checking
            data = await resp.json()

        return data
