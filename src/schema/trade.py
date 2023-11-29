from typing import List, Optional
from pydantic import BaseModel


class OrderSchema(BaseModel):
    amount: float
    safe_price: float
    ft_order_side: str
    order_filled_timestamp: int
    ft_is_entry: bool
    pair: str
    order_id: str
    status: str
    average: float
    cost: float
    filled: float
    is_open: bool
    order_date: str
    order_timestamp: int
    order_filled_date: str
    order_type: str
    price: float
    remaining: float
    ft_fee_base: Optional[float]
    funding_fee: Optional[float]


class TradeSchema(BaseModel):
    trade_id: int
    pair: str
    base_currency: str
    quote_currency: str
    is_open: bool
    exchange: str
    amount: float
    amount_requested: float
    stake_amount: float
    max_stake_amount: float
    strategy: str
    enter_tag: Optional[str]
    timeframe: int
    fee_open: float
    fee_open_cost: float
    fee_open_currency: str
    fee_close: float
    fee_close_cost: float
    fee_close_currency: str
    open_date: str
    open_timestamp: int
    open_rate: float
    open_rate_requested: float
    open_trade_value: float
    close_date: str
    close_timestamp: int
    realized_profit: float
    realized_profit_ratio: float
    close_rate: float
    close_rate_requested: float
    close_profit: float
    close_profit_pct: float
    close_profit_abs: float
    trade_duration_s: int
    trade_duration: int
    profit_ratio: float
    profit_pct: float
    profit_abs: float
    exit_reason: str
    exit_order_status: str
    stop_loss_abs: float
    stop_loss_ratio: float
    stop_loss_pct: float
    stoploss_order_id: Optional[str]
    stoploss_last_update: Optional[str]
    stoploss_last_update_timestamp: Optional[int]
    initial_stop_loss_abs: float
    initial_stop_loss_ratio: float
    initial_stop_loss_pct: float
    min_rate: float
    max_rate: float
    leverage: int
    interest_rate: float
    liquidation_price: Optional[float]
    is_short: bool
    trading_mode: str
    funding_fees: float
    amount_precision: float
    price_precision: float
    precision_mode: int
    contract_size: Optional[int]
    has_open_orders: Optional[bool]
    orders: Optional[List[OrderSchema]]


class BotTradesSchema(BaseModel):
    bot_name: str
    trades: List[TradeSchema]


class TradeListSchema(BaseModel):
    bot_trades: List[BotTradesSchema]
