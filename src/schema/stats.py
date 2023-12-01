from pydantic import BaseModel
from enum import Enum
from datetime import date


class TimeUnit(str, Enum):
    daily = "daily"
    weekly = "weekly"
    monthly = "monthly"


class StatSchema(BaseModel):
    date: date
    abs_profit: float
    rel_profit: float
    starting_balance: float
    fiat_value: float
    trade_count: int


class BotStatSchema(BaseModel):
    bot_name: str
    data: list[StatSchema]
    fiat_display_currency: str
    stake_currency: str
