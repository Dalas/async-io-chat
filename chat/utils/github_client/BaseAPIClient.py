

MAIN_HEADERS = {
    'Accept': 'application/vnd.github.v3+json'
}


class BaseAPIClient:
    base_url = 'https://api.github.com/'
    headers = MAIN_HEADERS

    def __init__(self, client):
        self._cli = client

    def prepare_headers(self, headers=None):
        if not headers:
            return self.headers
        else:
            return {
                **headers,
                **self.headers
            }

    async def _fetch(self, url, method, headers, data):
        headers = self.prepare_headers(headers)

        async with getattr(self._cli, method)(
            url,
            headers=headers,
            data=data
        ) as resp:
            # TODO: add code checks, exceptions
            return await resp.json()

    async def get(self, url, *, headers=None, data=None):
        return await self._fetch(self.base_url + url, 'get', headers, data)

    async def post(self, url, *, headers=None, data=None):
        return await self._fetch(self.base_url + url, 'post', headers, data)
