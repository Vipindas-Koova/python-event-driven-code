# from __future__ import annotations
from dataclasses import asdict
from typing import List, Dict, Callable, Type, TYPE_CHECKING
import cuid
from domain import commands, events
from domain.user import User
from services.user_service import UserService

def add_user_command_handlers( command:commands.AddUser, user_repo):
    UserService(user_repo).create_user(
        User(
            id = cuid.cuid(),
            first_name = command.first_name,
            last_name = command.last_name
        )
    )

def user_added_event_handler( event, user_repo):
    pass

EVENT_HANDLERS = {
    events.UserAdded: [user_added_event_handler]
}  # type: Dict[Type[events.Event], List[Callable]]

COMMAND_HANDLERS = {
    commands.AddUser: [add_user_command_handlers]
    
}  # type: Dict[Type[commands.Command], Callable]