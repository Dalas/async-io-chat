from chat.decorators import login_required


@login_required
async def create_chat(request):
    body = await request.post()
    print(body)

    return {}, 201
