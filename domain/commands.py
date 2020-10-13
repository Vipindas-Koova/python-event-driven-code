from dataclasses import dataclass
from datetime import date, datetime
from decimal import Decimal
import dataclasses
import json

class Command:
    pass

@dataclass
class AddUser(Command):
    first_name: str
    last_name: str