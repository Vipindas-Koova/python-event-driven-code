import abc
from abc import abstractmethod
from domain.user import User

class UserAbstractRepository(abc.ABC):

    @abstractmethod
    def create_user(self, user: User):
        pass
