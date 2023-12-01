import requests as re

from fastapi import APIRouter
from fastapi.exceptions import HTTPException
from requests.auth import HTTPBasicAuth
from requests.exceptions import ConnectionError
from dock import container_pool


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
