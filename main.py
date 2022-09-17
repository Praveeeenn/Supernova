import routes
from helpers import utils


async def app(scope, receive, send):

    print("====================================================")
    print(scope)
    print("====================================================")
    path = scope["path"]
    method = scope["method"]
    headers = utils.headers_to_dict(scope["headers"])
    authorization = headers.get("authorization")

    if await routes.is_404(send, path):
        return

    if path == "/":
        await routes.handle_home(send)
    elif path == "/login":
        await routes.handle_login(send, authorization)


# if __name__ == "__main__":
#     config = uvicorn.Config("main:app", port=5000, log_level="info", reload=True)
#     server = uvicorn.Server(config)
#     server.run()
