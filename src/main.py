import uvicorn
import requests as re
import docker

from routes import Bots, Trades
from models import Base
from database import engine
from requests.auth import HTTPBasicAuth
from fastapi import FastAPI, File


BASIC_AUTH = HTTPBasicAuth("mjekrami", "mamali75")

app = FastAPI()
app.include_router(Bots)
app.include_router(Trades)
docker_client = docker.DockerClient(base_url="unix:///var/run/docker.sock")

if __name__ == "__main__":
    Base.metadata.create_all(engine)
    uvicorn.run("main:app", port=3000, reload=True)
