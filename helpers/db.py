import pymongo


class MongoDB:

    def __init__(self, db_name):
        con_string = "mongodb://admin:password@localhost:27017"
        self.client = pymongo.MongoClient(con_string)
        self.db = self.client[db_name]
