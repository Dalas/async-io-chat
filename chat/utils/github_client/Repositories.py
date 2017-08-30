from .BaseAPIClient import BaseAPIClient


class Repositories(BaseAPIClient):
    async def get_users_repositories(self, username, token):
        headers = {
            'Authorization': f'token {token}'
        }

        return await self.get(f'user/{username}/repos', headers=headers)

    async def get_current_users_repositories(self, token):
        headers = {
            'Authorization': f'token {token}'
        }

        data = {
            'affiliation': 'owner'
        }

        return await self.get('user/repos', headers=headers, data=data)
