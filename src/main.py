from typing import Annotated
import uvicorn
import requests as re
from requests.auth import HTTPBasicAuth
from fastapi import FastAPI, File
import docker

BASE_URL = "http://localhost:8080/api/v1"
BASIC_AUTH = HTTPBasicAuth("mjekrami", "mamali75")

app = FastAPI()
docker_client = docker.DockerClient(base_url="unix:///var/run/docker.sock")


@app.get("/bot/trades")
def get_trades():
    res = re.get(f"{BASE_URL}/trades", auth=BASIC_AUTH)
    return res.json()


@app.get("/bot/edge")
def get_edge():
    res = re.get(f"{BASE_URL}/edge", auth=BASIC_AUTH)
    return res.json()


@app.post("/bot/register")
def register_bot(file: Annotated[bytes, File()]):
    return {"file_size": len(file)}


if __name__ == "__main__":
    uvicorn.run("main:app", port=3000)
