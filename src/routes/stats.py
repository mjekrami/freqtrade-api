import requests as re

from fastapi import APIRouter, Query
from fastapi.exceptions import HTTPException
from requests.auth import HTTPBasicAuth
from requests.exceptions import ConnectTimeout, ConnectionError
from dock import container_pool

from schema import BotStatSchema, StatSchema, TimeUnit

Stats = APIRouter(prefix="/stats", tags=["stats"])
BASIC_AUTH = HTTPBasicAuth("mjekrami", "mamali75")
TIMEOUT = 5


@Stats.get("/")
def get_stats(
    strat: str = Query(None, title="Strategy name"),
    unit: TimeUnit = Query(
        "daily",
        title="Unit to choose",
    ),
    n: int = Query(
        4, title="Number of units", description="Number of units to go back"
    ),
):
    if strat:
        name = container_pool.get_bot_by_name(strat)
        res = re.get(f"http://{name}:8080/api/v1/{unit.name}?n={n}", auth=BASIC_AUTH)
        res = res.json()
        display_currency = res["fiat_display_currency"]
        stake_currency = res["stake_currency"]

        stats = res["data"]
        stats_result = []
        for stat in stats:
            stat = StatSchema(**stat)
            stats_result.append(stat)
        result = BotStatSchema(
            bot_name=name,
            data=stats_result,
            fiat_display_currency=display_currency,
            stake_currency=stake_currency,
        )
        return result

    result = []
    try:
        bots = container_pool.get_running_bots()
        for bot in bots:
            res = re.get(
                f"http://{bot.name}:8080/api/v1/{unit.name}?n={n}",
                auth=BASIC_AUTH,
                timeout=TIMEOUT,
            )
            res = res.json()
            display_currency = res["fiat_display_currency"]
            stake_currency = res["stake_currency"]

            stats = res["data"]
            stats_result = []
            for stat in stats:
                stat = StatSchema(**stat)
                stats_result.append(stat)
            res = BotStatSchema(
                bot_name=bot.name,
                stats=stats_result,
                fiat_display_currency=display_currency,
                stake_currency=stake_currency,
            )
            result.append(res)
        return result
    except ConnectionError or ConnectTimeout:
        raise HTTPException(500, "could not connect")
