from dataclasses import dataclass
from datetime import date
from enum import StrEnum

from .errors import InvalidItemError


class Category(StrEnum):
    pass


@dataclass(frozen=True)
class Obj:
    id: str
    name: str
    category: Category
    created: date

    def __post_init__(self) -> None:
        if not isinstance(self.id, str) or not self.id.strip():
            raise InvalidItemError
        if not isinstance(self.name, str) or not self.name.strip():
            raise InvalidItemError
        if not isinstance(self.category, Category):
            raise InvalidItemError
        if not isinstance(self.created, date):
            raise InvalidItemError
        if self.created > date.today():
            raise InvalidItemError