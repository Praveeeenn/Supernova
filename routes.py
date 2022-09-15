import utils

available_routes = ["/", "/login", "/users/profile"]

users = [
    {
        "username": "ashish",
        "password": "abhishek7",
        "first_name": "Ashish",
        "last_name": "SahuJI"
    },
    {
        "username": "praveen",
        "password": "ashish",
        "first_name": "Praveen",
        "last_name": "Rajput"
    }
]


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
        for user in users:
            if user["username"] == username and user["password"] == password:
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


async def handle_profile(send, user):
    await send({
        'type': 'http.response.start',
        'status': 200,
        'headers': [
            [b'content-type', b'text/plain'],
        ],
    })
    await send({
        'type': 'http.response.body',
        'body': f'Welcome to Your Profile, {user["first_name"]}!!)'.encode("utf-8"),
    })
