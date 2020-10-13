from domain.user import User

class UserService(object):

    def __init__(self, user_repository):
        self.user_repo = user_repository

    def create_user(self, user: User):
        self.user_repo.create_user(user)