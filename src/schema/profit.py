from typing import Optional
from pydantic import BaseModel


class ProfitSchema(BaseModel):
    profit_closed_coin: float
    profit_closed_percent_mean: float
    profit_closed_ratio_mean: float
    profit_closed_percent_sum: float
    profit_closed_ratio_sum: float
    profit_closed_percent: float
    profit_closed_ratio: float
    profit_closed_fiat: float
    profit_all_coin: float
    profit_all_percent_mean: float
    profit_all_ratio_mean: float
    profit_all_percent_sum: float
    profit_all_ratio_sum: float
    profit_all_percent: float
    profit_all_ratio: float
    profit_all_fiat: float
    trade_count: int
    closed_trade_count: int
    first_trade_date: str
    first_trade_humanized: str
    first_trade_timestamp: int
    latest_trade_date: str
    latest_trade_humanized: str
    latest_trade_timestamp: int
    avg_duration: str
    best_pair: str
    best_rate: float
    best_pair_profit_ratio: float
    winning_trades: int
    losing_trades: int
    profit_factor: Optional[float]
    winrate: float
    expectancy: float
    expectancy_ratio: float
    max_drawdown: float
    max_drawdown_abs: float
    max_drawdown_start: str
    max_drawdown_start_timestamp: int
    max_drawdown_end: str
    max_drawdown_end_timestamp: int
    trading_volume: float
    bot_start_timestamp: int
    bot_start_date: str


class BotProfitSchema(BaseModel):
    bot_name: str
    profit: ProfitSchema