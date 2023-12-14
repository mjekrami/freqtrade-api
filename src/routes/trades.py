import requests as re

from requests.exceptions import ConnectTimeout, ConnectionError

from requests.auth import HTTPBasicAuth
from fastapi import APIRouter, Query
from fastapi.exceptions import HTTPException

from dock import container_pool

from schema import (
    BotTradesSchema,
    TradeSchema,
    BotProfitSchema,
    BotPerformanceSchema,
    PerformanceSchema,
)


Trades = APIRouter(prefix="/trades", tags=["trades"])
BASIC_AUTH = HTTPBasicAuth("mjekrami", "mamali75")
TIMEOUT = 5


@Trades.get("/")
def get_all_trades():
    result = []
    try:
        containers = container_pool.get_running_bots()
        for container in containers:
            response = re.get(
                f"http://{container.name}:8080/api/v1/trades",
                auth=BASIC_AUTH,
                timeout=TIMEOUT,
            )
            trades = response.json()["trades"]
            trades_result = []
            for trade in trades:
                trade = TradeSchema(**trade)
                trades_result.append(trade)
            res = BotTradesSchema(bot_name=container.name, trades=trades_result)
            result.append(res)
        return result
    except ConnectionError or ConnectTimeout:
        raise HTTPException(500, "could not connect")


@Trades.get("/strategy")
def get_trades_by_strategy(strat: str):
    try:
        container_name = container_pool.get_bot_by_name(strat)
        try:
            res = re.get(
                f"http://{container_name}:8080/api/v1/trades",
                auth=BASIC_AUTH,
                timeout=TIMEOUT,
            )
        except ConnectionError or ConnectTimeout:
            raise HTTPException(
                500,
                f"could not connect to container with name {strat}. timeout or error",
            )
        trades = res.json()["trades"]
        trades_result = []
        for trade in trades:
            trade = TradeSchema(**trade)
            trades_result.append(trade)
        res = BotTradesSchema(bot_name=container_name, trades=trades_result)
        return res
    except:
        raise HTTPException(404, f"strategy with name {strat} could not be found")


@Trades.get("/profit")
def get_profit(
    strat: str = Query(
        None, title="Strategy Name", description="Optional strategy parameter"
    )
):
    if strat:
        name = container_pool.get_bot_by_name(strat)
        res = re.get(
            f"http://{name}:8080/api/v1/profit", auth=BASIC_AUTH, timeout=TIMEOUT
        )
        res = res.json()
        return BotProfitSchema(bot_name=name, profit=res)

    result = []
    try:
        containers = container_pool.get_running_bots()
        for container in containers:
            response = re.get(
                f"http://{container.name}:8080/api/v1/profit",
                auth=BASIC_AUTH,
                timeout=TIMEOUT,
            )
            profit = response.json()
            res = BotProfitSchema(bot_name=container.name, profit=profit)
            result.append(res)
        return result
    except ConnectionError or ConnectTimeout:
        raise HTTPException(500, "could not connect")


@Trades.get("/performance")
def get_performance(bot_name: str | None = None):
    if bot_name:
        bot = container_pool.get_bot_by_name(bot_name)
        res = re.get(f"http://{bot}:8080/api/v1/performance", auth=BASIC_AUTH)
        performance = res.json()
        perf_result = []
        for perf in performance:
            perf = PerformanceSchema(**perf)
            perf_result.append(perf)
        return BotPerformanceSchema(bot_name=bot, performance=perf_result)

    bots = container_pool.get_running_bots()
    for bot in bots:
        res = re.get(f"http://{bot.name}:8080/api/v1/performance", auth=BASIC_AUTH)
        performances = res.json()
        perf_result = []
        for perf in performances:
            perf = PerformanceSchema(**perf)
            perf_result.append(perf)
        res = BotPerformanceSchema(bot_name=bot.name, performance=perf_result)
        return res
