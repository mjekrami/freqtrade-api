from pydantic import BaseModel
from typing import Mapping


class ContainerSchema(BaseModel):
    container_id: str
    name: str
    status: str


class TradeSchema(BaseModel):
    pass


class OrderSchema(BaseModel):
    pass
