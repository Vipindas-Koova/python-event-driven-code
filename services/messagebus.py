# pylint: disable=broad-except, attribute-defined-outside-init
# from __future__ import annotations
import logging
from typing import Callable, Dict, List, Union, Type, TYPE_CHECKING
from domain import events, commands
from ports.user_repository import UserAbstractRepository

logger = logging.getLogger(__name__)

Message = Union[commands.Command, events.Event]


class MessageBus(object):

    def __init__(
        self,
        user_repo: UserAbstractRepository,
        event_handlers: Dict[Type[events.Event], List[Callable]],
        command_handlers: Dict[Type[commands.Command], Callable]
    ):
        self.user_repo = user_repo
        self.event_handlers = event_handlers
        self.command_handlers = command_handlers

    def handle(self, message: Message):
        self.queue = [message]
        while self.queue:
            message = self.queue.pop(0)
            if isinstance(message, events.Event):
                return self.handle_event(message)
            elif isinstance(message, commands.Command):
                return self.handle_command(message)
            else:
                raise Exception(f'{message} was not an Event or Command')


    def handle_event(self, event: events.Event):
        for handler in self.event_handlers[type(event)]:
            try:
                logger.debug('handling event %s with handler %s', event, handler)
                return handler(event, self.user_repo)
            except Exception:
                logger.exception('Exception handling event %s', event)
                continue


    def handle_command(self, command: commands.Command):
        for handler in self.command_handlers[type(command)]:
            try:
                logger.debug('handling event %s with handler %s', command, handler)
                return handler(command, self.user_repo)
            except Exception:
                logger.exception('Exception handling command %s', command)
                continue