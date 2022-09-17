from helpers import utils
from helpers.db import MongoDB


def get_collection():
    mongo_db = MongoDB("master_db")
    return mongo_db.db["user"]


class User:

    def __init__(self, **kwargs):
        pass

    @staticmethod
    def create(**kwargs):
        # validations
        if User.get_user_by_email(kwargs["email"]):
            raise Exception("This email is already exists")

        password = kwargs["password"]
        if password is None or not len(password) >= 8:
            raise Exception("Invalid password")

        # create user
        hashed_password = utils.hashed_password(password)
        user_dict = {
            "first_name": kwargs["first_name"],
            "last_name": kwargs["last_name"],
            "email": kwargs["email"],
            "password": hashed_password,
        }
        user = get_collection().insert_one(user_dict)
        print("User >> ", user)

        return user

    def update(self, **kwargs):
        pass

    def delete(self, **kwargs):
        pass

    @staticmethod
    def delete_all():
        x = get_collection().delete_many({})
        print(x.deleted_count, " documents deleted.")

    @staticmethod
    def read(username, password):
        pass

    @staticmethod
    def get_user_by_email(email):
        query = {"email": email}
        record = get_collection().find_one(query)
        return record
