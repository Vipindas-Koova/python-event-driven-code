import pytest
import sys,os
sys.path.append(os.path.abspath(os.getcwd()))
print(sys.path)
from services.user_service import UserService
from adapters.dynamodb.user_repository import UserRepository
from domain.user import User

@pytest.fixture
def mock_user():
    return User(id="1",first_name="a",last_name="b")

def test_create_user(mock_user):
    user_repo = UserRepository()
    UserService(user_repo).create_user(mock_user)
    assert 1 == 1