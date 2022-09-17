from helpers import utils
from helpers.db import MongoDB


def get_collection():
    mongo_db = MongoDB("master_db")
    return mongo_db.db["session"]


class Session:

    def __init__(self, **kwargs):
        pass

    @staticmethod
    def create(**kwargs):
        values_dict = {
            "token": utils.generate_token(),
            "user_id": kwargs["user_id"]
        }
        inserted = get_collection().insert_one(values_dict)
        record = Session.get_record_by_id(inserted.inserted_id)
        return record

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
    def get_user_by_token(token):
        query = {"token": token}
        record = get_collection().find_one(query)
        return record

    @staticmethod
    def get_record_by_id(record_id):
        query = {"_id": record_id}
        record = get_collection().find_one(query)
        return record
