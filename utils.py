import base64


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
