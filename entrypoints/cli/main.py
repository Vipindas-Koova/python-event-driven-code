from services.user_service import UserService
from infrastructure.dynamodb.user_repository import UserRepository
from domain.user import User

if __name__ == "__main__":
    user = User(id="1",first_name="a",last_name="b")
    user_repo = UserRepository()
    UserService(user_repo).create_user(user)