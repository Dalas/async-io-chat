


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

    async def _fetch(self, url, method, headers, body):
        headers = self.prepare_headers(headers)

        async with getattr(self._cli, method)(
            self.base_url + url,
            headers=headers,
            data=body
        ) as resp:
            # TODO: add code checks, exceptions
            return await resp.json()

    async def get(self, url, *, headers=None, body=None):
        return await self._fetch(url, 'get', headers, body)

    async def post(self, url, *, headers=None, body=None):
        return await self._fetch(url, 'post', headers, body)
