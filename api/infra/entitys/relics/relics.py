
from pydantic import BeforeValidator
from typing import Annotated

from api.utils import bold_numbers
from api.infra.entitys.relics.extra import Advancement
from api.infra.entitys.base import EntityBase


class Relic(EntityBase):
    name: str
    rarity: str
    description: Annotated[str, BeforeValidator(bold_numbers)] | None = None
    source: Annotated[str, BeforeValidator(bold_numbers)] | None = None
    type: str
    icon: str
    advancement: list[Advancement]
