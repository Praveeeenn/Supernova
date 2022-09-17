import json

from helpers import utils
from models.session import Session
from models.user import User

available_routes = ["/", "/login", "/users/profile"]


async def handle_home(send):
    await send({
        'type': 'http.response.start',
        'status': 200,
        'headers': [
            [b'content-type', b'text/plain'],
        ],
    })
    await send({
        'type': 'http.response.body',
        'body': b'Welcome to StackNix Advanced Cloud Services',
    })


def get_user(auth):
    if auth:
        username, password = utils.decode_basic_auth(auth)
        user = User.get_user_by_email(username)
        if user and utils.check_password(password, user["password"]):
            return user


async def handle_login(send, auth):
    user = get_user(auth)
    print("handle_login called-------")
    print(f"user {user}")
    if user:
        await handle_profile(send, user)
    else:
        await handle_401(send)


async def handle_401(send):
    print("handle_401 called-------")
    await send({
        'type': 'http.response.start',
        'status': 401,
        'headers': [
            [b'content-type', b'text/plain'],
        ],
    })
    await send({
        'type': 'http.response.body',
        'body': b"401 Unauthorized Requests From Advanced Praveen's Service",
    })


async def is_404(send, path):
    if path not in available_routes:
        await send({
            'type': 'http.response.start',
            'status': 404,
            'headers': [
                [b'content-type', b'text/plain'],
            ],
        })
        await send({
            'type': 'http.response.body',
            'body': b'Page not found!!!!!!',
        })
        return True
    return False


async def handle_profile(send, user_record):
    user_id = user_record["_id"]
    session_record = Session.create(user_id=user_id)
    session_token = session_record["token"]
    response_data = {
        "token": session_token
    }
    await send({
        'type': 'http.response.start',
        'status': 200,
        'headers': [
            [b'content-type', b'application/json'],
        ],
    })
    await send({
        'type': 'http.response.body',
        'body': bytes(json.dumps(response_data), 'utf-8'),
    })
