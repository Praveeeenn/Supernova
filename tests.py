from helpers import utils
from models.user import User

# plain_password = "ashish_k"
#
# hashed = utils.hashed_password(plain_password)
#
# print("Hashed ", hashed)
#
# print(utils.check_password(plain_password, hashed))
#
user = User.create(first_name="Praveen", last_name="Rajput", email="praveenislive@gmail.com", password="Ashish_k")

#
# User.delete_all()