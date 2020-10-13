from domain.user import User
from ports.user_repository import UserAbstractRepository

class UserRepository(UserAbstractRepository):

    def __init__(self):
        pass
        # initialize dynamodb vars

    def create_user(self, user:User):
        # dynamodb put
        pass