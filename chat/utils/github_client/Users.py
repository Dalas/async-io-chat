from .BaseAPIClient import BaseAPIClient


class Users(BaseAPIClient):
    async def get_auth_user(self, token):
        headers = {
            'Authorization': f'token {token}'
        }

        return await self.get('user', headers)
