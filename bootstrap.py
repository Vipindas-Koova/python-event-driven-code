from services.messagebus import MessageBus
from services import handlers

def bootstrap() -> MessageBus:
    from adapters.dynamodb.user_repository import UserRepository

    event_handlers = handlers.EVENT_HANDLERS
    command_handlers = handlers.COMMAND_HANDLERS
    
    return MessageBus(
        user_repo=UserRepository(),
        event_handlers=event_handlers,
        command_handlers=command_handlers
    )

def bootstrap_fake() -> MessageBus:
    from adapters.memory.user_repository import UserRepository

    event_handlers = handlers.EVENT_HANDLERS
    command_handlers = handlers.COMMAND_HANDLERS
    
    return MessageBus(
        user_repo=UserRepository(),
        event_handlers=event_handlers,
        command_handlers=command_handlers
    )