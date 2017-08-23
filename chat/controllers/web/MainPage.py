from chat.credentials import GITHUB_CLIENT_ID

from aiohttp.web import Response


async def main_page(request):
    return Response(
        body=f'<a href=https://github.com/login/oauth/authorize?client_id={CLIENT_ID}>Login</a>',
        content_type='text/html'
    )
