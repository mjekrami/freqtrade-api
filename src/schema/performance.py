from pydantic import BaseModel
from typing import List


class PerformanceSchema(BaseModel):
    pair: str
    profit: float
    profit_ratio: float
    profit_pct: float
    profit_abs: float
    count: int


class BotPerformanceSchema(BaseModel):
    bot_name: str
    performance: List[PerformanceSchema]
