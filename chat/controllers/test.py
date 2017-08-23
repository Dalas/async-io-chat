from aiohttp.web import Response



async def test(request):
    print(request)
    return Response(text='Test')
