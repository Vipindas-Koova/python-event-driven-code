from domain.user import User
from ports.user_repository import UserAbstractRepository

class UserRepository(UserAbstractRepository):

    def __init__(self):
        self.users = []

    def create_user(self, user:User):
        self.users.append(user)