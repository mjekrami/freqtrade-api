import uvicorn
import requests as re
import docker

from routes import Bots, Trades, Stats
from models import Base
from database import engine
from requests.auth import HTTPBasicAuth
from auth.oauth2 import router_login

from fastapi import FastAPI, File
from fastapi.middleware.cors import CORSMiddleware

BASIC_AUTH = HTTPBasicAuth("mjekrami", "mamali75")
origins = ["http://localhost:3005"]

app = FastAPI()
app.include_router(Bots)
app.include_router(Trades)
app.include_router(Stats)
app.include_router(router_login)
app.add_middleware(
    CORSMiddleware, allow_origins=origins, allow_methods=["*"], allow_headers=["*"]
)
docker_client = docker.DockerClient(base_url="unix:///var/run/docker.sock")

if __name__ == "__main__":
    Base.metadata.create_all(engine)
    uvicorn.run("main:app", port=3000, host="0.0.0.0", reload=True)
