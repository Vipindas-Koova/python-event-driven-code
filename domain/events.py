from dataclasses import dataclass
from datetime import date, datetime
from decimal import Decimal
import dataclasses
import json

class Event:
    pass

@dataclass
class UserAdded(Event):
    id: str
    first_name: str
    last_name: str