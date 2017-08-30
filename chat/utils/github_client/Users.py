from .BaseAPIClient import BaseAPIClient


class Users(BaseAPIClient):
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

        async with self._cli.get(url, data=data, headers=headers) as resp:
            # TODO: add status check
            return await resp.json()

    async def get_auth_user(self, token):
        headers = {
            'Authorization': f'token {token}'
        }

        return await self.get('user', headers=headers)
