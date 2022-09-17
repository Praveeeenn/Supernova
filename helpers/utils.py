import base64
import binascii
import os

import bcrypt


def decode_basic_auth(auth):
    if auth.startswith("Basic "):
        encoded_string = auth.split("Basic ")[1]
        decode_string = base64.b64decode(encoded_string).decode('utf-8').split(":")
        username = decode_string[0]
        password = decode_string[1]
        return username, password
    return None, None


def headers_to_dict(headers):
    dictionary = {}
    for item in headers:
        header_name = item[0].decode('utf-8')
        header_value = item[1].decode('utf-8')
        dictionary[header_name] = header_value
    return dictionary


def hashed_password(plain_password):
    password = bytes(plain_password, 'utf-8')
    hashed_string = bcrypt.hashpw(password, bcrypt.gensalt()).decode('utf-8')
    return hashed_string


def check_password(plain_password, hashed):
    password = bytes(plain_password, 'utf-8')
    hashed_bytes = bytes(hashed, 'utf-8')
    return bcrypt.checkpw(password, hashed_bytes)


def generate_token():
    return "tds_aqua_" + binascii.hexlify(os.urandom(256)).decode()
