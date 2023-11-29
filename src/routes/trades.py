import requests as re

from requests.auth import HTTPBasicAuth
from fastapi import APIRouter
from fastapi.exceptions import HTTPException
from dock import ContainerPool
from dock import container_pool

Trades = APIRouter(prefix="/trades", tags=["trades"])
BASIC_AUTH = HTTPBasicAuth("mjekrami", "mamali75")


@Trades.get("/trades")
def get_trades():
    result = []
    try:
        containers = container_pool.get_running_bots()
        for container in containers:
            response = re.get(
                f"http://{container.name}:8080/api/v1/trades", auth=BASIC_AUTH
            )
            result.append(response)
        return result
    except ConnectionError:
        raise HTTPException(500, "could not connect")
