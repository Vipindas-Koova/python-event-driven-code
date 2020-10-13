import pytest
import sys,os
sys.path.append(os.path.abspath(os.getcwd()))
print(sys.path)
from services.user_service import UserService
from adapters.memory.user_repository import UserRepository
from domain.user import User
from domain.commands import AddUser
import bootstrap

mbus = bootstrap.bootstrap_fake()

@pytest.fixture
def mock_user():
    return AddUser(first_name="a",last_name="b")

def test_create_user(mock_user):
    mbus.handle(mock_user)
    assert len(mbus.user_repo.users) >= 1