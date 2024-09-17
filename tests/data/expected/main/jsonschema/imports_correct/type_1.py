# generated by datamodel-codegen:
#   filename:  type_1.json
#   timestamp: 2019-07-26T00:00:00+00:00

from __future__ import annotations

from enum import Enum
from typing import Literal

from pydantic import BaseModel, Field


class Type(Enum):
    a = 'a'
    A = 'A'


class Type1(BaseModel):
    type_: Literal['a', 'A'] = Field(..., title='Type')