import requests as re
import logging

from schema import BotPerformanceSchema, PerformanceSchema

from fastapi import APIRouter
from fastapi.exceptions import HTTPException

from requests.auth import HTTPBasicAuth

from dock import container_pool

logger = logging.getLogger(__name__)
Bots = APIRouter(prefix="/bots", tags=["bots"])

BASE_URL = "http://localhost:8080/api/v1"
BASIC_AUTH = HTTPBasicAuth("mjekrami", "mamali75")


@Bots.get("/")
def get_bots(id: str | None = None, status: str | None = "running"):
    try:
        if id:
            return container_pool.get_bot_by_id(id)
        if status:
            return container_pool.get_bot_by_status(status)

        bots = container_pool.get_running_bots()
        return bots
    except:
        raise HTTPException(404, "could not find any container")


@Bots.get("/performance")
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
